# -*- coding:utf-8 -*-

from map_handle import *


def r_sub(seq):
    """
        减法

        :param seq: 数字列表

        example：
                :seq  [1,2,1.2]
                :return  -2.2
    """
    seq = reduce(lambda x, y: x - y, seq)
    return seq


def r_mul(seq):
    """
        乘法

        :param seq: 数字列表

        example：
                :seq  [1,2,1.2]
                :return  2.4
    """

    seq = reduce(lambda x, y: x * y, seq)
    return seq