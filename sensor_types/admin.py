# -*- coding: utf-8 -*-
from django.contrib import admin
from sensor_types.models import SensorTypeModel

# Register your models here.
class SensorTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(SensorTypeModel, SensorTypeAdmin)