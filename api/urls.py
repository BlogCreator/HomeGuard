"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from device.views import DeviceViewSet
from sensor.views import SensorViewSet
from sensor_types.views import SensorTypeViewSet
from time_line.views import TimeLineViewSet
from user.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'device', DeviceViewSet)
router.register(r'sensor', SensorViewSet)
router.register(r'sensor_type', SensorTypeViewSet)
router.register(r'time_line', TimeLineViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]
