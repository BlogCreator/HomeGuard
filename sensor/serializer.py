from rest_framework import serializers
from sensor.models import SensorModel


class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SensorModel
        fields = ('sensor_id', 'devices', 'type', 'pin')