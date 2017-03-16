
import operator
import json

from django.http import HttpResponse


def get_range_map_val(range_list, input_val):
    """
    [)  (]
    """
    mapping_val = None

    for item in range_list:
        rangex = item.get('range')
        if operator.ge(input_val, rangex[0]) and operator.le(input_val, rangex[1]):
            mapping_val = item.get('mapping_val')
            break

    return mapping_val


def json_dumps(data):
    """json dumps for dict data
    :param data; data to json.dumps, if is not dict just return raw data
    """
    if isinstance(data, dict):
        data = json.dumps(data, encoding="UTF-8", ensure_ascii=False)

    return data


def json_response(data):
    if not (data and isinstance(data, dict)):
        # logger.error("Response data:%s Error", data)
        raise TypeError("Response data Error")

    result = json_dumps(data)
    # logger.info("Response data:%s", result)

    return HttpResponse(result,
                        content_type="application/json;charset=utf-8")