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


def reduce_add(seq):
    result = reduce(lambda x, y: x + y, seq)
    return result


def reduce_sub(seq):
    result = reduce(lambda x, y: x - y, seq)
    return result


def reduce_mul(seq):
    result = reduce(lambda x, y: x * y, seq)
    return result


