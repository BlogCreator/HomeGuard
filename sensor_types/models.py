# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class SensorTypeModel(models.Model):
    type = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.type

    class Meta:
        db_table = 'sensor_types'