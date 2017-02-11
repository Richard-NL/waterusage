from django.shortcuts import render
from django.http import HttpResponse
from water.models import WaterUsageState
from django.template.loader import render_to_string
from datetime import datetime, timezone
import json


def index(request):
    first_checkup = WaterUsageState.objects.order_by('date_created').first()
    last_checkup = WaterUsageState.objects.latest('date_created')
    delta = last_checkup.date_created - first_checkup.date_created
    total_usage = last_checkup.usage - first_checkup.usage

    template_vars = {
        'first_checkup': first_checkup,
        'last_checkup': last_checkup,
        'total_usage': last_checkup.usage - first_checkup.usage,
        'average_usage': "{0:.2f}".format(total_usage / delta.days),
        'first_usage': first_checkup.usage,
        'last_usage': last_checkup.usage,
        'days_between': delta.days,
    }

    html = render_to_string('template.html', template_vars)
    return HttpResponse(html)

def test(request):
    months_back = months_back_from_request(request)

    start_date_given = '2017-%d-01' % (int(datetime.now().strftime("%m")) + months_back * -1)
    end_date_given = '2017-%d-01' % (int(datetime.now().strftime("%m")) + 1 + months_back * -1)

    chart_data = create_chart_data(end_date_given, start_date_given)

    allow_back_link = True
    display_datetime = datetime.strptime(start_date_given, "%Y-%m-%d")
    if display_datetime.month == 1:
        allow_back_link = False

    html = render_to_string(
        'template_chart.html',
        {
            'chart_data': json.dumps(chart_data),
            'allow_back_link': allow_back_link,
            'previous_month': months_back + 1,
            'next_month': months_back -1,
            'display_month': display_datetime.strftime("%B")
        }
    )

    return HttpResponse(html)

def months_back_from_request(request):
    months_back_param = request.GET.get('months_back')
    if months_back_param is None:
        return 0
    return int(months_back_param)

def create_chart_data(end_date_given, start_date_given):
    first_available_checkup = WaterUsageState.objects.filter(date_created__lte=start_date_given).last()
    start_datetime = datetime.strptime(start_date_given, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    delta = start_datetime - first_available_checkup.date_created

    first_checkup_cooridnates = get_first_checkup_coordinates(delta, first_available_checkup)

    last_checkup = WaterUsageState.objects.filter(date_created__lt=end_date_given).last();
    chart_data = []
    # not enough data then do not bother
    if first_available_checkup is None or last_checkup is None:
        return chart_data

    # add the first measurement to the chart
    chart_data.append(first_checkup_cooridnates)

    # get all checkups between given date
    checkups_between = WaterUsageState.objects.filter(date_created__gt=start_datetime, date_created__lt=end_date_given).all()
    for checkup in checkups_between:
        chart_data.append({
            'x': (checkup.date_created - start_datetime).days + 1,
            'y': checkup.usage
        })


    # add the last measurement to the chart
    chart_data.append({
        'x': (last_checkup.date_created - start_datetime).days + 1,
        'y': last_checkup.usage
    })
    return chart_data

def get_first_checkup_coordinates(delta, first_checkup):
    if delta.days > 0:
        checkup_end = WaterUsageState.objects.filter(date_created__gte='2017-01-02').first();
        average_left_hand = calculate_average_usage(
            first_checkup.usage,
            checkup_end.usage,
            first_checkup.date_created,
            checkup_end.date_created
        )

        first_checkup_cooridnates = {
            'x': 1,
            'y': calculate_usage(delta.days + 1, average_left_hand) + first_checkup.usage
        }
    else:
        first_checkup_cooridnates = {
            'x': 1,
            'y': first_checkup.usage
        }
    return first_checkup_cooridnates

def calculate_average_usage(usage_start, usage_end, datetime_start, datetime_end):
    delta_for_average = datetime_end - datetime_start
    total_usage = usage_end - usage_start
    return total_usage / delta_for_average.days

def calculate_usage(days_between, average_usage):
    return days_between * average_usage