from django.db import models
from django.utils import timezone

class WaterUsageState(models.Model):
    usage = models.PositiveIntegerField(default=0)
    date_created = models.DateTimeField('date of check',  default=timezone.now())
    upload = models.FileField(blank=True, upload_to='uploads/')

    def __str__(self):
        return "Usage %d on %s" % (self.usage, self.date_created.strftime("%d-%m-%y %H:%M"))

    class Meta:
        ordering = ['date_created']