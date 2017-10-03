from django.db import models
from device.models import DeviceModel
from sensor_types.models import SensorTypeModel

# Create your models here.
class SensorModel(models.Model):
    sensor_id = models.CharField(max_length=17, unique=True)
    devices = models.ForeignKey(DeviceModel)
    type = models.ForeignKey(SensorTypeModel, db_column='type')
    pin = models.CharField(max_length=5)

    def __str__(self):
        return self.sensor_id

    class Meta:
        db_table = 'sensors'