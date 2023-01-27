# Generated by Django 4.1.5 on 2023-01-27 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_ser', models.CharField(max_length=50)),
                ('sensor_type', models.CharField(max_length=50)),
                ('sensor_value', models.FloatField()),
                ('time_stamp', models.DateTimeField()),
            ],
        ),
    ]