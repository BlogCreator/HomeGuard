# -*- coding: utf-8 -*-
import json

from django.db import transaction
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

from client_interface.exceptions import JsonError
from sensor.models import SensorModel
from device.models import DeviceModel
from time_line.models import TimeLineModel
from sensor_types.models import SensorTypeModel

from client_interface.util import *

try:
    import msg
except ImportError:
    msg = Msg()


"""
{
    "id":"1",
    "time":5410,
    "sensor":[
        {
            "type":"co",
            "pin":54,
            "value":947,
            "sensorId":"1co"
        }
    ]
}
"""


def parse_nonstandard_json(json_string):
    return eval(json_string, type('Dummy', (dict,), dict(__getitem__=lambda s, n: n))())


def parse_request_body(request_body):
    try:
        object = parse_nonstandard_json(request_body)
        new_object = {}
        new_object["device_id"] = object['id']
        new_object["time"] = object['time']
        new_object["additional"] = object.get('additional')
        new_object["sensors"] = []
        for sensor in object['sensor']:
            new_object["sensors"].append({
                "type": sensor['type'],
                "pin": sensor['pin'],
                "value": sensor['value'],
                "sensor_id": sensor['sensorId'],
            })
    except:
        raise JsonError("JSON ERROR")
    else:
        return new_object


@csrf_exempt
def handle_client_request(request):
    try:
        heart_beat = parse_request_body(request.body)
        print(heart_beat)
    except Exception as e:
        return HttpResponseBadRequest(e)
    try:
        with transaction.atomic():
            ref_device = DeviceModel.objects.get(device_id=heart_beat['device_id'])
            for sensor in heart_beat['sensors']:
                ref_sensor = SensorModel.objects.get(sensor_id=sensor['sensor_id'])
                time_line = TimeLineModel(time=heart_beat['time'],
                                          value=sensor['value'],
                                          device=ref_device,
                                          sensor=ref_sensor)
                time_line.save()
    except Exception as e:
        print(e)
        return HttpResponseBadRequest(e)

    resp = {'command': []}

    pro_data = data_filter(heart_beat.get("sensors"))
    if pro_data:
        resp['command'].append("beep 10000")

    message = msg.msgrcv()
    while message:
        resp['command'].append(message)
        message = msg.msgrcv()

    return HttpResponse(json.dumps(resp))