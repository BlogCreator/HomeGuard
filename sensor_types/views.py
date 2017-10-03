from rest_framework import viewsets
from sensor_types.models import SensorTypeModel
from sensor_types.serializer import SensorTypeSerializer

class SensorTypeViewSet(viewsets.ModelViewSet):
    queryset = SensorTypeModel.objects.all()
    serializer_class = SensorTypeSerializer