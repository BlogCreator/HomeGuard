# -*- coding: utf-8 -*-
from django.contrib import admin
from time_line.models import TimeLineModel

# Register your models here.
class TimeLineAdmin(admin.ModelAdmin):
    pass


admin.site.register(TimeLineModel, TimeLineAdmin)