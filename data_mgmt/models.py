from django.db import models

# Create your models here.
class SensorData(models.Model):
    sensor_ser = models.CharField(max_length=50)
    sensor_type = models.CharField(max_length=50)
    time_stamp = models.DateTimeField()
    sensor_value = models.FloatField()