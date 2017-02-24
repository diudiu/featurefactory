# -*- coding:utf-8 -*-

from vendor.errors.feature import FeatureProcessError
from datetime import datetime


def map_to_int(seq):
    seq = map(lambda x: int(eval(str(1))), seq)
    return seq


def map_to_slice(seq, args):
    seq = map(lambda x: x[int(args[0]):int(args[1])], seq)
    return seq


def map_string_to_datetime(seq):
    try:
        seq = map(lambda x: datetime.strptime(x, "%Y-%m-%d"), seq)

    except:
        seq = map(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S"), seq)
    return seq


def map_get_dict_value(seq, args):
    seq = map(lambda x: x.get(args[0], None), seq)
    return seq


def map_get_new_list(seq, args):
    """
    seq:[{"work_end": "20170605","industry": "string","comp_name": "百度",},
        {"comp_name": "腾讯","work_end": "20180809","industry": "string",}]

    args:['work_end','comp_name']

    return:[["20170605","百度"],["20180809","腾讯"]]

    """
    seq = map(lambda x: [x.get(args[0], None), x.get(args[1], None)], seq)
    return seq


def filter_not_null(seq):
    seq = filter(lambda x: x not in (None, '', {}, [], ()), seq)
    return seq


def filter_digit_or_float(seq):
    seq = filter(lambda x: str(x).count('.') <= 1 and str(x).replace('.', '').isdigit(), seq)
    return seq


def reduce_add(seq):
    result = reduce(lambda x, y: x + y, seq)
    return result


def reduce_sub(seq):
    result = reduce(lambda x, y: x - y, seq)
    return result


def reduce_mul(seq):
    result = reduce(lambda x, y: x * y, seq)
    return result


