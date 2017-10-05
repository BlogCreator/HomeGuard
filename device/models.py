# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class DeviceModel(models.Model):
    device_id = models.CharField(max_length=17, unique=True)
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=255)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'devices'