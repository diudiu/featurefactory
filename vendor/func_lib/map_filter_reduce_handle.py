# -*- coding:utf-8 -*-

from vendor.errors.feature import FeatureProcessError


def reduce_singo_value(seq):
    if not isinstance(seq, list):
        raise FeatureProcessError
    return seq[0]


def reduce_add(seq):
    if not isinstance(seq, list):
        raise FeatureProcessError
    value = reduce(lambda x, y: x + y, seq)

    return value
