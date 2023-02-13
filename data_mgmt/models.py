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


class UserData(models.Model):
    user_name = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    organization = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"user_name:{self.user_name}, password: {self.password}, name: {self.name}, " \
        f"email: {self.email}, phone: {self.phone}, organization: {self.organization}"
