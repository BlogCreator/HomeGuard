# -*- coding: utf-8 -*-
from rest_framework import serializers
from device.models import DeviceModel


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeviceModel
        fields = ('device_id', 'name', 'position', 'user')