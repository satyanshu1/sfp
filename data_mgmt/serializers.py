from rest_framework import serializers
from .models import SensorData, UserData


class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ['id', 'sensor_ser', 'sensor_type', 'time_stamp', 'sensor_value']


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['user_name', 'password', 'name', 'email', 'phone']
