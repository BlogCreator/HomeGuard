from django.contrib import admin
from device.models import DeviceModel

# Register your models here.
class DeviceAdmin(admin.ModelAdmin):
    pass

admin.site.register(DeviceModel, DeviceAdmin)