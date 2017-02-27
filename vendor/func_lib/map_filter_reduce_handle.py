# -*- coding:utf-8 -*-

from vendor.errors.feature import FeatureProcessError
from datetime import datetime


def m_to_int(result):
    """转换[1, 2.1, '2.1', '2'] 类似序列为 int"""
    result = map(lambda x: int(eval(str(x))), result)
    return result


def m_to_len(result):
    result = len(result)
    return result


def m_get_seq_index_value(result, args):
    """获取序列中指定索引的值"""
    result = result[int(args[0])]
    return result


def m_get_mon_sub(result):
    """比较传进来的由两个日期字符串组成的seq 之间相差的月数"""
    try:
        result = map(lambda x: datetime.strptime(x, "%Y-%m-%d"), result)

    except:
        result = map(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S"), result)

    result = (result[0] - result[1]).days / 30.0
    result = round(result, 2)
    return result


def m_dict_key_sort_in_list(result, args):
    """
    :param result: [{'20160708': 'gyf'}, {'20180505': 'zme'}, {'20170101': 'zkp'}]
    :param args: ['True'] or ['False']
    :return: [{'20180505': 'zme'}, {'20170101': 'zkp'}, {'20160708': 'gyf'}]
    """
    if eval(args[0]):
        result = sorted(result, key=lambda x: x.keys()[0], reverse=True)
    else:
        result = sorted(result, key=lambda x: x.keys()[0])
    return result


def m_seq_inx0_sort_in_list(result, args):
    """
    :param result: [['20160708', 'gyf'], ['20180505', 'zme'],['20170101', 'zkp']]
    :param args: ['True'] or ['False']
    :return: [['20180505', 'zme'], ['20170101', 'zkp'],['20160708', 'gyf']]
    """
    if eval(args[0]):
        result = sorted(result, key=lambda x: x[0], reverse=True)
    else:
        result = sorted(result, key=lambda x: x[0])
    return result


def m_to_slice(result, args):
    """
    :param result: ['abcd','1234556']
    :param args: ['0','3']
    :return: ['abc','123']
    """
    result = map(lambda x: x[int(args[0]):int(args[1])], result)
    return result


def m_string_to_datetime(result):
    try:
        result = map(lambda x: datetime.strptime(x, "%Y-%m-%d"), result)

    except:
        result = map(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S"), result)
    return result


def m_get_dict_value(result, args):
    """

    :param result: [{"work_end": "20170605","industry": "string","comp_name": c,},
                    {"comp_name": "腾讯","work_end": "20180809","industry": "string",}]
    :param args: ['comp_name']
    :return: ['百度'， '腾讯']
    """
    result = map(lambda x: x.get(args[0], None), result)
    return result


def m_get_new_dict(result, args):
    """
    :param result:[{"work_end": "20170605","industry": "string","comp_name": "百度",},
                    {"comp_name": "腾讯","work_end": "20180809","industry": "string",}]

    :param args: ['work_end','comp_name']

    :return:[{"20170605":"百度"},{"20180809":"腾讯"}]

    """
    result = map(lambda x: {x.get(args[0], None): x.get(args[1], None)}, result)
    return result


def m_get_new_list(result, args):
    """
    :param result:[{"work_end": "20170605","industry": "string","comp_name": "百度",},
                    {"comp_name": "腾讯","work_end": "20180809","industry": "string",}]

    :param args:['work_end','comp_name']

    :return:[["20170605","百度"],["20180809","腾讯"]]

    """
    result = map(lambda x: [x.get(args[0], None), x.get(args[1], None)], result)
    return result


def f_not_null(result):
    result = filter(lambda x: x not in (None, '', {}, [], ()), result)
    return result


def f_digit_or_float(result):
    result = filter(lambda x: str(x).count('.') <= 1 and str(x).replace('.', '').isdigit(), result)
    return result


def r_add(result):
    result = reduce(lambda x, y: x + y, result)
    return result


def r_sub(result):
    result = reduce(lambda x, y: x - y, result)
    return result


def r_mul(result):
    result = reduce(lambda x, y: x * y, result)
    return result
