# -*- coding: utf-8 -*-
from rest_framework import serializers
from sensor_types.models import SensorTypeModel


class SensorTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SensorTypeModel
        fields = ('type', )