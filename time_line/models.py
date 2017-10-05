# -*- coding: utf-8 -*-
from django.db import models
from sensor.models import SensorModel
from device.models import DeviceModel

# Create your models here.
class TimeLineModel(models.Model):
    sensor = models.ForeignKey(SensorModel)
    device = models.ForeignKey(DeviceModel)
    time = models.DateTimeField()
    value = models.CharField(max_length=255)

    class Meta:
       db_table = 'time_line'