from django.contrib import admin
from sensor.models import SensorModel

# Register your models here.
class SensorAdmin(admin.ModelAdmin):
    pass


admin.site.register(SensorModel, SensorAdmin)