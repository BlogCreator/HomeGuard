from django.db import models


# Create your models here.
class DeviceModel(models.Model):
    device_id = models.CharField(max_length=17, unique=True)
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'devices'