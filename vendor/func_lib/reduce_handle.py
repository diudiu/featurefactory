# -*- coding:utf-8 -*-

from map_handle import *


def r_add(result):
    """加"""
    result = reduce(lambda x, y: x + y, result)
    return result


def r_sub(result):
    """减"""
    result = reduce(lambda x, y: x - y, result)
    return result


def r_mul(result):
    """乘法"""
    result = reduce(lambda x, y: x * y, result)
    return result