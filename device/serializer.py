from rest_framework import serializers, viewsets
from device.models import DeviceModel


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeviceModel
        fields = ('device_id', 'name', 'position')