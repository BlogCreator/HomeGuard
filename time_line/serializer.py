from rest_framework import serializers
from time_line.models import TimeLineModel


class TimeLineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TimeLineModel
        fields = ('sensor', 'device', 'time', 'value')