from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from data_mgmt.models import SensorData, UserData
from data_mgmt.serializers import SensorDataSerializer, UserDataSerializer
from django.core.exceptions import ObjectDoesNotExist


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

# rest apis
@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def ph_data(request, *args, **kwargs):
    querry_set = None
    if id := request.data.get('id'):
        try:
            querry_set = SensorData.objects.get(pk=id)
        except:
            pass

    if request.method == 'GET':
        snsr_data = querry_set if querry_set else SensorData.objects.all()

        count = request.data.get('count')
        if not count:
            count = request.query_params.get('count')            
        if count:
            snsr_data = snsr_data.order_by('-id')[:int(count)]  # -id sorts in descending order. Note the -ve sign.

        serializer = SensorDataSerializer(snsr_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method in {'PUT', 'POST'}:
        serializer = SensorDataSerializer(querry_set, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # TODO delete based on filter
        res = querry_set if querry_set else SensorData.objects.all()
        res.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def user_reg(request, *args, **kwargs):
    querry_set = None
    if id := request.data.get('id'):
        try:
            querry_set = UserData.objects.get(pk=id)
        except:
            pass

    if request.method == 'GET':
        user_data = querry_set if querry_set else UserData.objects.all()
        serializer = UserDataSerializer(user_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method in {'PUT', 'POST'}:
        serializer = UserDataSerializer(querry_set, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # TODO delete based on filter
        res = querry_set if querry_set else UserData.objects.all()
        res.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def user_auth(request, *args, **kwargs):
    result = 'nok'
    if request.method == 'GET':
        user = request.data.get('usr')
        if not user:
            user = request.query_params.get('usr')
        pwd = request.data.get('pwd')
        if not pwd:
            pwd = request.query_params.get('pwd')            

        try:
            user_record = UserData.objects.get(user_name=user)
            if user_record.password == pwd:
                result = 'ok'
        except ObjectDoesNotExist:
            pass

        return Response(result, status=status.HTTP_200_OK)