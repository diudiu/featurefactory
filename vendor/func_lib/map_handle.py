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

from apps.common.models import CityCodeField
from vendor.errors.feature import FeatureProcessError


def m_to_int(seq):
    """
    转换数字或序列为int类型

    :param seq: 可以为int,float的数字或字符串 或 他们组成的列表
    :return:int或int的列表

    example：
            :seq： [1, 2.1, '2.1', '-2']
            :return： [1, 2, 2, -2]
    """

    if not isinstance(seq, list):
        seq = int(eval(str(seq)))
    else:
        seq = map(lambda x: int(eval(str(x))), seq)
    return seq


def m_to_power(seq):
    """
        转换为值的2次方

        :param seq: 可以为int,float的数字组成的列表
        :return:    列表中对应元素的2次方

        example：
                :seq： [1, -2]
                :return： [1, -4]
    """
    seq = map(lambda x: x ** 2, seq)
    return seq


def m_to_len(seq):
    """
        求序列的长度

        :param seq: 可以为字符串、列表
        :return:    字符串、列表的长度

        example：
                :seq： [1, -2]
                :return： 2
    """
    seq = len(seq)
    return seq


def m_to_sum(seq):
    """
        求序列中值得和

        :param seq: 可以为整数、浮点数组成的列表
        :return:    列表值得和

        example：
                :seq： [1, -2]
                :return： -1
    """
    seq = sum(seq)
    return seq


def m_get_seq_index_value(seq, args):
    """
        获取序列中指定索引的值

        :param seq: 可以为字符串、列表
        :param args: 索引
        :return:    索引值

        example：
                :seq  [1, -2]
                :args   0
                :return  1
    """
    seq = seq[int(args)]
    return seq


def m_get_mon_sub(seq, args):
    """
        比较传进来的由两个日期字符串组成的seq之间相差的月数 args保留小数点位数

        :param seq: 日期字符串
        :param args: 保留小数点位数 正整数
        :return:    相差的月数

        example：
                :seq  ['2017-01-01', '2016-01-01']
                :args   2
                :return  12.2
    """
    try:
        seq = map(lambda x: datetime.strptime(x, "%Y-%m-%d"), seq)

    except:
        seq = map(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S"), seq)

    seq = (seq[0] - seq[1]).days / 30.0
    seq = round(seq, args)
    return seq


def m_get_date_to_now_years(seq, args=None):
    """
        返回传进来的时间字符串距离现在的年数 args保留小数点位数

        :param seq: 日期字符串
        :param args: 保留小数点位数 正整数
        :return:    距离现在的年数

        example：
                :seq  '2016-01-01'
                :args   2
                :return  0.16
    """

    try:
        seq = datetime.strptime(seq, "%Y-%m-%d")
    except:
        seq = datetime.strptime(seq, "%Y-%m-%d %H:%M:%S")

    seq = (datetime.now() - seq).days / 365.0
    if args:
        seq = round(seq, args)
    return seq


def m_seq_to_agv(seq, args=None):
    """
        返回列表中值的平均值 args保留小数点位数

        :param seq: 整数、浮点数组成的列表
        :param args: 保留小数点位数 正整数
        :return:    平均值

        example：
                :seq  [1,2,1.2]
                :args   2
                :return  1.4
    """
    seq = sum(seq) / len(seq)
    if args:
        seq = round(seq, args)
    return seq


def m_to_bool(seq, args=None):
    """
        返回bool值0/1

        :param seq: 任意值
        :param args: 可不传 传时seq==args为1
        :return:    0/1

        example：
                :seq  '11'
                :args   '00'
                :return  0
    """
    if args:
        if seq == args:
            seq = 1
        else:
            seq = 0
    else:
        if seq:
            seq = 1
        else:
            seq = 0
    return seq


def m_check_x_in_y(seq, args):
    """
        判断x是否在y中 返回0/1

        :param seq: 字符串、元组、字典、列表
        :param args: 判断元素
        :return:    0/1

        example：
                :seq  '汉族'
                :args   '汉'
                :return  1
    """
    if args in seq:
        seq = 1
    else:
        seq = 0
    return seq


def m_digit_to_floor(seq):
    """
        向下取整

        :param seq: 整数、浮点数后他们的字符串
        :return:    小于seq的最大整数

        example：
                :seq  '-23.4'
                :return  -24
    """
    if isinstance(seq, basestring):
        seq = eval(seq)
    seq = math.floor(seq)
    return int(seq)


def m_marital_status_to_code(seq):
    """
        结婚状态的code值

        :param seq: 整数
        :return:    小于seq的最大整数

        example：
                :seq  '23'
                :return  20
    """
    if isinstance(seq, basestring):
        seq = eval(seq)
    seq = seq / 10 * 10
    return seq


def m_sex_to_code(seq):
    """
        返回性别的code值

        :param seq: 包含性别的字符串
        :return:    code

        example：
                :seq  '男生'
                :return  0
    """
    if '男' in seq:
        seq = 0
    elif '女' in seq:
        seq = 1
    else:
        raise FeatureProcessError("'don't know  sex")

    return seq


def m_dict_key_sort_in_list(seq, args=False):
    """
        对列表中字典按key排序，返回新的列表

        :param seq: 字典形成的列表
        :param args: 是否倒序 True or False
        :return:    排序后的列表

        example：
                :seq  [{'20160708': 'gyf'}, {'20180505': 'zme'}, {'20170101': 'zkp'}]
                :args   True
                :return  [{'20180505': 'zme'}, {'20170101': 'zkp'}, {'20160708': 'gyf'}]
    """

    seq = sorted(seq, key=lambda x: x.keys()[0], reverse=args)
    return seq


def m_seq_inx0_sort_in_list(seq, args=False):
    """
        对列表中单个列表按第一个元素排序，返回新的列表

        :param seq: 列表形成的列表
        :param args: 是否倒序 True or False
        :return:    排序后的列表

        example：
                :seq  [['20160708', 'gyf'], ['20180505', 'zme'],['20170101', 'zkp']]
                :args   True
                :return  [['20180505', 'zme'], ['20170101', 'zkp'],['20160708', 'gyf']]
    """

    seq = sorted(seq, key=lambda x: x[0], reverse=args)
    return seq


def m_to_slice(seq, args):
    """
        分片函数

        :param seq: 分片序列 字符串 列表
        :param args: 截取的范围
        :return:    分片结果

        example：
                :seq  ['abcd','1234556']
                :args   [0,3]
                :return  ['abc','123']
    """

    if not isinstance(seq, list):
        seq = seq[int(args[0]):int(args[1])]
    else:
        seq = map(lambda x: x[int(args[0]):int(args[1])], seq)
    return seq


def m_string_to_datetime(seq):
    """
        时间字符串转化为datetime对象

        :param seq: 日期字符串 或 日期字符串组成的列表
        :return:    datetime对象 或它的列表

        example：
                :seq  ['2017-01-01', '2017-02-28']
                :return  [datetime.datetime(2017, 1, 1, 0, 0), datetime.datetime(2017, 2, 28, 0, 0)]

    """
    if not isinstance(seq, list):
        try:
            seq = datetime.strptime(seq, "%Y-%m-%d")
        except:
            seq = datetime.strptime(seq, "%Y-%m-%d %H:%M:%S")
    else:
        try:
            seq = map(lambda x: datetime.strptime(x, "%Y-%m-%d"), seq)

        except:
            seq = map(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S"), seq)
    return seq


def m_get_dict_value_in_list(seq, args):
    """
        获取列表中字典某个元素的值 返回值得列表

        :param seq: 字典形成的列表
        :param args: 获取的元素
        :return:    获取的元素的值得列表

        example：
                :seq  [{"work_end": "20170605","industry": "string","comp_name": c,},
                        {"comp_name": "腾讯","work_end": "20180809","industry": "string",}]
                :args   'comp_name'
                :return  ['百度'， '腾讯']
    """

    seq = map(lambda x: x.get(args, None), seq)
    return seq


def m_get_new_dict(seq, args):
    """
        对列表中的字典map成 args对应的字典列表
        :param seq: 字典形成的列表
        :param args: 获取的元素列表，只能是两个元素
        :return:    得到的新的字典列表

        example：
                :seq  [{"work_end": "20170605","industry": "string","comp_name": "百度",},
                        {"comp_name": "腾讯","work_end": "20180809","industry": "string",}]
                :args   ['work_end','comp_name']
                :return  [{"20170605":"百度"},{"20180809":"腾讯"}]
    """

    seq = map(lambda x: {x.get(args[0], None): x.get(args[1], None)}, seq)
    return seq


def m_get_new_list(seq, args):
    """
            对列表中的字典map成 args对应的列表的列表
            :param seq: 字典形成的列表
            :param args: 获取的元素列表，只能是两个元素
            :return:    得到的新的 列表形成的列表

            example：
                    :seq  [{"work_end": "20170605","industry": "string","comp_name": "百度",},
                            {"comp_name": "腾讯","work_end": "20180809","industry": "string",}]

                    :args   ['work_end','comp_name']
                    :return  [["20170605","百度"],["20180809","腾讯"]]
    """
    seq = map(lambda x: [x.get(args[0], None), x.get(args[1], None)], seq)
    return seq


def m_get_mobile_m1_m5_key_seq(mobilestr, tags, key_list):

    """
        获取 mobile字符串在 tags字典中 1月到5月存在的key_list中key值的和的列表

        :param mobilestr: 查询的手机字符串
        :param tags:      含多种手机信息的字典
        :param key_list:   查询的字段
        :return:        该手机号1月到5月 在key_list中值的和 形成的列表

        example：
                :mobilestr  18920019796_8a404758b8f8b87c70006b8e9f4614db_
                :targs {
                        '18920019796_8a404758b8f8b87c70006b8e9f4614db_': {
                        'M5': {'callTimes': 3,'calledTimes': 2},
                        'M4': {'callTimes': 8,'calledTimes': 20},
                        'M3': {'month': '201610'}},}}

                :args   ['callTimes', 'calledTimes']
                :return  [28, 5]
    """
    tmp = []
    m_list = ['M1', 'M2', 'M3', 'M4', 'M5']
    for i in m_list:
        if i in tags[mobilestr]:
            value_list = []
            for key in key_list:
                value = tags[mobilestr].get(i, {}).get(key, '')
                if str(value).replace('.', '').isdigit():
                    value_list.append(value)
            if value_list:
                tmp.append(sum(value_list))

    return tmp


def m_get_mobile_stability(seq):
    """获取手机号的稳定度"""
    total_calltimes_ave = m_seq_to_agv(seq)
    mobile_stability = (sum([i ** 2 for i in seq]) / len(seq)) ** 0.5
    mobile_stability = mobile_stability / total_calltimes_ave
    return round(mobile_stability, 4)


def m_get_city_name(address):
    """
        提取公司所在地址的城市名称

        :param address: 地址
        :return:    城市

        example：
                :address  '日照市黄海一路兴业国际商城001号楼01单元903号'
                :return  '日照'

                :address  '广州'
                :return  '广州'

    """
    city_name = ''
    if "-" in address:
        city_name = address.split('-')[1]
    else:
        for tip in ['市', '盟', '州']:
            if tip in address:
                index = address.find(tip)
                city_name = address[:index]
                city_name = city_name.encode('utf-8')
                if len(city_name) == 3:
                    city_name += tip
                break
    return city_name


def m_get_city_name1(city):
    """
           m_get_city_name 包含 m_get_city_name1 这个弃用
            提取公司所在地址的城市名称

            :param address: 地址
            :return:    城市

            example：
                    :address  'beijing'
                    :return  '北京'

                    :address  '广州'
                    :return  '广州'

    """
    if "-" in city:
        city = city.split('-')[1]
    if ('市' in city) or ('盟' in city) or ('州' in city and len(city) > 6):
        city = city[:-3]
    return city


def m_city_name_to_code(city_name):
    """
       获取城市名所对应的Code

        :param city_name: 城市
        :return:    code

        example：
                :address  '北京'
                :return  1
    """
    ccf = CityCodeField.objects.filter(
        city_name_cn=city_name,
        is_delete=False
    )
    if not ccf:
        raise FeatureProcessError('not find %s code config in database table' % city_name)
    company_addr_city_level = ccf[0].city_level
    if not str(company_addr_city_level).isdigit():
        raise FeatureProcessError('%s city_level config error in database table' % city_name)
    seq = int(company_addr_city_level)
    return seq


def m_max_flight_area(seq):
    """
       一年内飞机出行中最多出行区域的code

        :param seq: 飞行次数、国内次数、国外次数
        :return:    飞行次数==0 返回3    国内次数>国外次数 返回1 国外次数>国内次数 返回2

        example：
                :seq  [2, 2, 3]
                :return  2
    """
    """"""
    flight_times = seq[0]
    inland_count = seq[1]
    international_count = seq[2]

    if int(flight_times) == 0:
        seq = 3
    elif int(inland_count) >= int(international_count):
        seq = 1
    elif int(inland_count) < int(international_count):
        seq = 2
    else:
        raise FeatureProcessError("'don't know  max_flight_area code")
    return seq


if __name__ == '__main__':
    print m_dict_key_sort_in_list([{'20160708': 'gyf'}, {'20180505': 'zme'}, {'20170101': 'zkp'}],True)

