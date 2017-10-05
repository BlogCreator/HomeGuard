# -*- coding: utf-8 -*-
from rest_framework import viewsets
from time_line.models import TimeLineModel
from time_line.serializer import TimeLineSerializer

class TimeLineViewSet(viewsets.ModelViewSet):
    queryset = TimeLineModel.objects.all()
    serializer_class = TimeLineSerializer