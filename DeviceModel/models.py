from django.db import models

# Create your models here.
from django.db import models

class DeviceModel(models.Model):
    db_table  = "devices"

    id        = models.AutoField(primary_key=True)
    device_id = models.CharField(max_length = 17, unique = True)
    name      = models.CharField(max_length = 20)
    position  = models.CharField(max_length = 255)