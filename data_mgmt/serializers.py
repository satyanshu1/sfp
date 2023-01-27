from rest_framework import serializers
from .models import SensorData


class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ['id', 'sensor_ser', 'sensor_type', 'time_stamp', 'sensor_value']