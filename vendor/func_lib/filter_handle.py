# -*- coding:utf-8 -*-

from map_handle import *


def f_digit_or_float(result):
    """过滤出数字或float的值"""
    result = filter(lambda x: str(x).count('.') <= 1 and str(x).replace('.', '').isdigit(), result)
    return result


def f_not_null(result):
    """过滤非空值"""
    result = filter(lambda x: x not in (None, '', {}, [], ()), result)
    return result


def f_mobile_m1_m5_sum_max_seq(result, args):
    """获取 mobile字符串在 tags字典中 1月到5月 某些key值sum最大的序列"""
    tags = result[0]
    mobile = result[1]
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