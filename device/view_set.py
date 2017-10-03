from rest_framework import viewsets
from device.models import DeviceModel
from device.serializer import DeviceSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = DeviceModel.objects.all()
    serializer_class = DeviceSerializer