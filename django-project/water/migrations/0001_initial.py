# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WaterUsageState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_date', models.DateTimeField(verbose_name='date of check')),
            ],
        ),
    ]