from django.test import TestCase

from client_interface.util import *


if __name__ == '__main__':
    r = data_filter([{"type": "co2", "pin": 54, "value": 123, "sensor_id": 1}])
    print(r)