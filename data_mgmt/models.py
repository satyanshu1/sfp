from django.db import models

# Create your models here.
class SensorData(models.Model):
    sensor_ser = models.CharField(max_length=50)
    sensor_type = models.CharField(max_length=50)
    time_stamp = models.DateTimeField()
    sensor_value = models.FloatField()

    def __str__(self) -> str:
        return f"sensor id:{self.sensor_ser}, sensor type: {self.sensor_type}, time stamp: {self.time_stamp}, " \
        f"sensor reading: {self.sensor_value}"
