# -*- coding:utf-8 -*-

import re
import datetime as dt

from map_handle import *


def f_digit_or_float(seq):
    """过滤出数字或float的值"""
    seq = filter(lambda x: str(x).count('.') <= 1 and str(x).replace('.', '').isdigit(), seq)
    return seq


def f_not_null(seq):
    """过滤非空值"""
    seq = filter(lambda x: x not in (None, '', {}, [], ()), seq)
    return seq


def f_mobile_m1_m5_sum_max_seq(seq, args):
    """获取 mobile字符串在 tags字典中 1月到5月 某些key值sum最大的序列"""
    tags = seq[0]
    mobile = seq[1]
    tel_str = '%s__' % mobile
    if tel_str in tags:
        m1_m5_max = m_get_mobile_m1_m5_key_seq(tel_str, tags, args)

    # 其他情况，以前5月加和最大值取m1-m5
    else:
        m1_m5_max = []
        for strs in tags:
            m1_m5 = m_get_mobile_m1_m5_key_seq(strs, tags, args)
            if sum(m1_m5) > sum(m1_m5_max):
                m1_m5_max = m1_m5
    return m1_m5_max


def f_days_greater_than_args(result, args):
    """
    过滤掉时间距离现在大于指定天数的元素
    :param result: 时间戳列表
    :param args: 指定天数
    :return: 时间戳列表
    """
    now = dt.datetime.today()
    res = []
    for stamp in result:
        length = len(str(stamp))
        if length > 10:
            stamps = stamp / (10 ** (length - 10))
        else:
            stamps = stamp
        date = dt.datetime.utcfromtimestamp(stamps)
        days = (now - date).days
        if days <= args:
            res.append(stamp)
    return res


def f_inside_stipulate_scope(result, args):
    """
    过滤不在指定范围内的列表元素
    :param result: 原始列表
    :param args: 指定元素范围值  (列表)
    :return: 过滤后列表
    """
    res = []
    for i in result:
        if i in args:
            res.append(i)
    return res


def f_get_workplace_now(result):
    length = len(result)
    workplace_list = result[:length / 2]
    date_list = result[length / 2:]
    for i in range(length / 2):
        if '999999' == date_list[i]:
            return workplace_list[i]


def f_plate_number(seq):
    """
        过滤列表中合法的车牌号

        :param seq: 车牌号列表
        :return:    合法的车牌号列表

        example：
                :seq  ['冀BF876R', u'京BF688R', '京123456']

                :return  ['冀BF876R', '京BF688R']
    """
    m = r'^[京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼使领]{3}[A-Z]{1}[A-Z0-9]{4}[A-Z0-9挂学警港澳]{1}$'
    tmp = []
    for plate in seq:
        if len(plate) != 9:
            plate = plate.encode("utf8")
        if re.match(m, plate):
            tmp.append(plate)
    return tmp


if __name__ == '__main__':
    print f_plate_number(['冀BF876R', u'京BF688R', '京123456'])
