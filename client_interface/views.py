# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from client_interface.exceptions import JsonError, RequestMethodError


def parse_nonstandard_json(json_string):
    return eval(json_string, type('Dummy', (dict,), dict(__getitem__=lambda s, n: n))())


def parse_request_body(request_body):
    # try:
    object = parse_nonstandard_json(request_body)
    new_object = {}
    new_object["device_id"] = object['id']
    new_object["time"] = object['time']
    new_object["sensors"] = []
    for sensor in object['sensor']:
        new_object["sensors"].append({
            "type": sensor['type'],
            "pin": sensor['pin'],
            "value": sensor['value'],
            "sensor_Id": sensor['sensorId'],
        })
        # except:
        #    raise JsonError("JSON ERROR")

        # return new_object


def is_correct_request(request):
    try:
        if request.method != 'POST':
            raise Exception('BAD REQUEST')
    except Exception as e:
        raise RequestMethodError(repr(e))


@csrf_exempt
def handle_client_request(request):
    try:
        # is_correct_request(request)
        parse_request_body(request.body)
    except Exception as e:
        return HttpResponseBadRequest(e.message)
