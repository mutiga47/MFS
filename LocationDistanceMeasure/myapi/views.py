# from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PointsConnectorSerializer
from .models import PointsConnector

class PointsConnectorViewSet(viewsets.ModelViewSet):
    queryset = PointsConnector.objects.all()
    serializer_class = PointsConnectorSerializer