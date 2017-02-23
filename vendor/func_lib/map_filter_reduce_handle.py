# -*- coding:utf-8 -*-

from vendor.errors.feature import FeatureProcessError


def map_to_int(seq):
    value = map(lambda x: int(x), seq)
    return value


def map_to_slice(seq, args):
    value = map(lambda x: x[int(args[0]):int(args[1])], seq)
    return value


def map_to_int(seq):
    value = map(lambda x: int(x), seq)
    return value


def reduce_singo_value(seq):
    # if slice:
    #     value = seq[0][int(slice[0]):int(slice[1])]
    # else:
    value = seq[0]
    return value


def reduce_add(seq):
    value = reduce(lambda x, y: x + y, seq)
    return value


def reduce_multiplied(seq):
    value = reduce(lambda x, y: x * y, seq)
    return value
