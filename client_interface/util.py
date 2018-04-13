data_ranges = {"CH4": [0, 0], "co": [0, 1000], "yan": [0, 0]}


def data_filter(data):
    """
    :param data: [{"type": "co", "pin": 54, "value": 123, "sensor_id": 1}]
    :return:
    """
    pro_data = []
    for i in data:
        data_range = data_ranges.get(i.get("type"), [0,0])
        if i.get("value") < data_range[0] \
                or i.get("value") > data_range[1]:
            pro_data.append(i.get("type"))
    return pro_data


class Msg:
    @staticmethod
    def msgrecv(self):
        return None

    @staticmethod
    def msgsnd(self, msg):
        pass