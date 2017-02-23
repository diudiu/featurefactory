# -*- coding:utf-8 -*-

from vendor.errors.feature import FeatureProcessError
from datetime import datetime


def map_to_int(seq):
    seq = map(lambda x: int(x), seq)
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


def filter_not_null(seq):
    seq = filter(lambda x: x not in (None, '', {}, [], ()), seq)
    return seq


def reduce_singo_value(seq):
    # if slice:
    #     seq = seq[0][int(slice[0]):int(slice[1])]
    # else:
    value = seq[0]
    return value


def reduce_add(seq):
    value = reduce(lambda x, y: x + y, seq)
    return value


def reduce_sub(seq):
    value = reduce(lambda x, y: x - y, seq)
    return value


# def reduce_sub_datetime(seq):
#     value =
#     return value


def reduce_mul(seq):
    value = reduce(lambda x, y: x * y, seq)
    return value


# def reduce_list_len(seq):
#     value = len(seq)
#     return value