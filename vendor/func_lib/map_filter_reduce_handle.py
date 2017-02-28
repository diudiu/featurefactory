# -*- coding:utf-8 -*-

import os
import sys
import math
from datetime import datetime
reload(sys)
sys.setdefaultencoding('utf-8')

home_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(home_path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'featurefactory.settings')
import django
django.setup()

from vendor.utils.defaults import PositiveSignedTypeDefault
from apps.common.models import CityCodeField
from vendor.errors.feature import FeatureProcessError


def m_to_int(result):
    """转换[1, 2.1, '2.1', '2'] 类似序列为 int"""
    if not isinstance(result, list):
        result = int(eval(str(result)))
    else:
        result = map(lambda x: int(eval(str(x))), result)
    return result


def m_to_power(result):
    result = map(lambda x: x ** 2, result)
    return result


def m_to_len(result):
    result = len(result)
    return result


def m_to_sum(result):
    result = sum(result)
    return result


def m_get_seq_index_value(result, args):
    """获取序列中指定索引的值"""
    result = result[int(args)]
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


def m_get_date_to_now_years(result):
    """比较传进来的['2016-01-01'] or '2016-01-01' 距离现在的年数"""
    if isinstance(result, list):
        result = result[0]
    try:
        result = datetime.strptime(result, "%Y-%m-%d")
    except:
        result = datetime.strptime(result, "%Y-%m-%d %H:%M:%S")

    result = (datetime.now() - result).days / 365.0
    result = round(result, 2)
    return result


def m_seq_to_agv(result):
    """返回列表的值得平均数"""
    result = sum(result) / len(result)
    return result


def m_to_bool(result, args=None):
    if args:
        if result == args:
            result = 1
        else:
            result = 0
    else:
        if result:
            result = 1
        else:
            result = 0
    return result


def m_check_x_in_y(result, args):
    if args in result:
        result = 1
    else:
        result = 0
    return result


def m_digit_to_floor(result):
    if isinstance(result, basestring):
        result = eval(result)
    result = math.floor(result)
    return int(result)


def m_marital_status_to_code(result):
    if isinstance(result, basestring):
        result = eval(result)
    result = result/10*10
    return result


def m_sex_to_code(result):
    if '男' in result:
        result = 0
    elif '女' in result:
        result = 1
    return result


def m_dict_key_sort_in_list(result, args):
    """
    :param result: [{'20160708': 'gyf'}, {'20180505': 'zme'}, {'20170101': 'zkp'}]
    :param args: True or False
    :return: [{'20180505': 'zme'}, {'20170101': 'zkp'}, {'20160708': 'gyf'}]
    """
    if args:
        result = sorted(result, key=lambda x: x.keys()[0], reverse=True)
    else:
        result = sorted(result, key=lambda x: x.keys()[0])
    return result


def m_seq_inx0_sort_in_list(result, args):
    """
    :param result: [['20160708', 'gyf'], ['20180505', 'zme'],['20170101', 'zkp']]
    :param args: True or False
    :return: [['20180505', 'zme'], ['20170101', 'zkp'],['20160708', 'gyf']]
    """
    if args:
        result = sorted(result, key=lambda x: x[0], reverse=True)
    else:
        result = sorted(result, key=lambda x: x[0])
    return result


def m_to_slice(result, args):
    """
    :param result: ['abcd','1234556']
    :param args: [0,3]
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
    :param args: 'comp_name'
    :return: ['百度'， '腾讯']
    """
    result = map(lambda x: x.get(args, None), result)
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


def map_get_mobile_m1_m5_key_seq(mobilestr, tags, key_list):
    """
     获取 mobile字符串在 tags字典中 1月到5月存在的key值，返回一个值得列表
    """
    tmp = []
    m_list = ['M1', 'M2', 'M3', 'M4', 'M5']
    for i in m_list:
        if i in tags[mobilestr]:
            value_list = []
            for key in key_list:
                value = tags[mobilestr].get(i, {}).get(key, 0)
                if not str(value).replace('.', '').isdigit():
                    value = 0
                value_list.append(value)
            tmp.append(sum(value_list))
    return tmp


def f_mobile_m1_m5_sum_max_seq(result):
    """获取 mobile字符串在 tags字典中 1月到5月 某个key值和最大的序列"""
    tags = result[0]
    mobile = result[1]
    tel_str = '%s__' % mobile
    if tel_str in tags:
        m1_m5_max = map_get_mobile_m1_m5_key_seq(tel_str, tags, ['callTimes', 'calledTimes'])

    # 其他情况，以前5月加和最大值取m1-m5
    else:
        m1_m5_max = []
        for strs in tags:
            m1_m5 = map_get_mobile_m1_m5_key_seq(strs, tags, ['callTimes', 'calledTimes'])
            if sum(m1_m5) > sum(m1_m5_max):
                m1_m5_max = m1_m5
    return m1_m5_max


def m_get_mobile_stability(result):
    """获取手机号的稳定度"""
    total_calltimes_ave = m_seq_to_agv(result)
    mobile_stability = (sum([i ** 2 for i in result]) / len(result)) ** 0.5
    mobile_stability = mobile_stability / total_calltimes_ave
    return round(mobile_stability, 4)


def m_get_company_addr_city_name(address):
    city_name = ''
    for tip in ['市', '盟', '州']:
        if tip in address:
            index = address.find(tip)
            city_name = address[:index]
            city_name = city_name.encode('utf-8')
            if len(city_name) == 3:
                city_name += '州'
            break
    return city_name


def m_city_name(city):
    if "-" in city:
        city = city.split('-')[1]
    if ('市' in city) or ('盟' in city) or ('州' in city and len(city) > 6):
        city = city[:-3]
    return city


def m_city_name_to_code(city_name):
    ccf = CityCodeField.objects.filter(
        city_name_cn=city_name,
        is_delete=False
    )
    if not ccf:
        raise FeatureProcessError('not find %s code config in database table' % city_name)
    company_addr_city_level = ccf[0].city_level
    if not str(company_addr_city_level).isdigit():
        raise FeatureProcessError('%s city_level config error in database table' % city_name)
    result = int(company_addr_city_level)
    return result


def m_max_flight_area(result):
    flight_times = result[0]
    inland_count = result[1]
    international_count = result[2]
    if int(flight_times) == 0:
        result = 3
    elif int(inland_count) >= int(international_count):
        result = 1
    elif int(inland_count) < int(international_count):
        result = 2
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


if __name__ == '__main__':
    print m_get_date_to_now_years(['2016-01-01'])
