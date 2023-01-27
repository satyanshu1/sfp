from django.shortcuts import render
from data_mgmt.models import SensorData


# Create your views here.
def say_hello(request, *args, **kwargs):
    # return render(request, 'hello.html')
    return render(request, 'hello.html', {'name': 'Satya'})

def index(request, *args, **kwargs):
    cols = ['sensor_ser', 'sensor_type', 'time_stamp', 'sensor_value']
    # sensor_data = [SensorData.objects.values_list(x, flat=True) for x in cols]
    sensor_data = [[x[y] for y in cols] for x in SensorData.objects.all().values()]
    hdr = ['sensor id', 'sensor type', 'time stamp', 'sensor reading']
    return render(request, 'index.html', {'tbl_hdr': hdr, 'sensor_data': sensor_data})
