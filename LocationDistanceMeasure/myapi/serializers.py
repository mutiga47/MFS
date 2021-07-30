#Serialier for the Points Connector class

from rest_framework import serializers
from .models import PointsConnector

class PointsConnectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PointsConnector()
        fields = ('id', 'points_list', 'closest_points_pair')