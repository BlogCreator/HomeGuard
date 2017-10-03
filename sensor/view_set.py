from rest_framework import viewsets
from sensor.models import SensorModel
from sensor.serializer import SensorSerializer

class SensorViewSet(viewsets.ModelViewSet):
    queryset = SensorModel.objects.all()
    serializer_class = SensorSerializer