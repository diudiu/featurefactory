# -*- coding:utf-8 -*-
import os
import sys
import re
import time
import math
from datetime import datetime, timedelta

reload(sys)
sys.setdefaultencoding('utf-8')
home_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(home_path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'featurefactory.settings')
import django

django.setup()

from vendor.errors.feature import FeatureProcessError
from apps.common.models import FeatureCodeMapping
from apps.common.models import CityCodeField
from apps.common.models import *
from apps.etl.models import P2PTelephoneModel, LoanAgencyModel
from vendor.utils.defaults import *

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


def m_str_to_int_float_in_list(seq):
    """
    转换类表中的数字或浮点数 字符串为 int、float,别的元素不变
    :param seq: 可以为任意值组成的列表
    :return:转换后的列表
    example：
            :seq： [1, 2.1, '2.1', '-2', '-8.8' [] ,'gyf']
            :return： [1, 2.1, 2.1, -2,-8.8, [], 'gyf']
    """
    tmp = []
    for value in seq:
        if str(value).count('.') <= 1 and str(value).replace('.', '').lstrip('-').isdigit():
            tmp.append(eval(str(value)))
        else:
            tmp.append(value)
    return tmp


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


def m_to_len(seq, args=0):
    """
        求序列的长度
        :param seq: 可以为字符串、列表
        :param args: 减数
        :return:    字符串、列表的长度
        example：
                :seq： [1, -2]
                :args  0
                :return： 2
    """
    seq = len(seq) - args
    return seq


def m_list_to_distinct(seq):
    """
        序列去除重复的值
        :param seq: 可以为字符串、列表
        :return:    去重后的字符串、列表
        example：
                :seq： [1, -2， 1]
                :return： [1, -2]
    """
    seq = list(set(seq))
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


def m_to_sort(seq, args=False):
    """
        排序
    """
    seq.sort(key=lambda x: x, reverse=args)
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


def m_get_mon_sub(seq, args=None):
    """
        比较传进来的由两个日期字符串组成的seq之间相差的月数 args保留小数点位数
        :param seq: 日期字符串
        :param args: 保留小数点位数
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
    if args is not None:
        seq = round(seq, args)
    return seq


def m_get_date_to_now_years(seq, args=None):
    """
        返回传进来的时间字符串距离现在的年数 args保留小数点位数
        :param seq: 日期字符串
        :param args: 保留小数点位数
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
    if args is not None:
        seq = round(seq, args)
    return seq


def m_get_date_to_now_days(seq):
    """
        :param seq: 日期字符串
        :return:    距离现在的天数

    """
    try:
        seq = datetime.strptime(seq, "%Y-%m-%d")
    except:
        seq = datetime.strptime(seq, "%Y-%m-%d %H:%M:%S")
    seq = (datetime.now() - seq).days
    return seq


def m_datetime_obj_to_str(seq):
    d = seq.strftime("%Y-%m-%d %H:%M:%S")
    return d


def m_seq_to_agv(seq, args=None):
    """
        返回列表中值的平均值 args保留小数点位数
        :param seq: 整数、浮点数组成的列表
        :param args: 保留小数点位数
        :return:    平均值
        example：
                :seq  [1,2,1.2]
                :args   2
                :return  1.4
    """
    seq = float(sum(seq)) / len(seq)
    if args is not None:
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
    if args is not None:
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


def m_to_recruitment(seq, args=None):
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
    if seq:
        seq = "统招"
    else:
        seq = "非统招"
    return seq


def m_to_bool2_0(seq, args=None):
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
    if args is not None:
        if seq == args:
            seq = "是"
        else:
            seq = "否"
    else:
        if seq:
            seq = "是"
        else:
            seq = "否"
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


def m_folk_x_in_y(seq, args):
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
        seq = "汉族"
    else:
        seq = "少数民族"
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


def m_marital_status(seq):
    """
        结婚状态
        :param seq: 整数
        :return:    小于seq的最大10的倍数
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
                :return  '男'
    """
    if '男' in seq:

        seq = '男'
    elif '女' in seq:
        seq = '女'
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
                :seq  [['20160708', 'gyf'], ['20180505', 'zme'], ['20170101', 'zkp']]
                :args   True
                :return  [['20180505', 'zme'], ['20170101', 'zkp'], ['20160708', 'gyf']]
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


def m_datetime_only_hour_minute(seq):
    """
        时间字符串只保留时分

        :param seq: 日期字符串 或 日期字符串组成的列表
        :return:    日期字符串只保留时分

        example：
                :seq  ['2017-01-01 12:20:00', '2017-02-28 09:10:30']
                :return  ['12:20', '09:10']

    """
    if not isinstance(seq, list):
        try:
            seq = datetime.strptime(seq, "%Y-%m-%d %H:%M:%S")
        except:
            raise FeatureProcessError('%s time format error ' % seq)
    else:
        try:
            seq = map(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S"), seq)
        except:
            raise FeatureProcessError('%s time format error ' % seq)

    seq = float(str(seq.hour) + '.' + str(seq.minute))
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


def m_get_mobile_m1_m5_key_seq(seq, tags, key_list):
    """
        获取 mobile字符串在 tags字典中 1月到5月存在的key_list中key值的和的列表

        :param seq: 查询的手机字符串
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
        if i in tags[seq]:
            value_list = []
            for key in key_list:
                value = tags[seq].get(i, {}).get(key, '')
                if str(value).replace('.', '').isdigit():
                    value_list.append(value)
            if value_list:
                tmp.append(sum(value_list))
    return tmp


def m_get_mobile_m1_m5_key_seq1(mobilestr, tags, key_list):
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
    mobile_stability = (sum([(i - total_calltimes_ave) ** 2 for i in seq]) / len(seq)) ** 0.5
    mobile_stability_a = mobile_stability / total_calltimes_ave
    return round(mobile_stability_a, 4)


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
    city_name = address
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


def m_city_name_to_level(city_name):
    """
       获取城市名所对应的level
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
        raise FeatureProcessError('not find %s level config in database table' % city_name)
    company_addr_city_level = ccf[0].city_level
    if not str(company_addr_city_level).isdigit():
        raise FeatureProcessError('%s city_level config error in database table' % city_name)
    seq = int(company_addr_city_level)
    return seq


def m_city_name_to_level2_0(city_name):
    """
       获取城市名所对应的level
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
        raise FeatureProcessError('not find %s level config in database table' % city_name)
    company_addr_city_level = ccf[0].city_level
    if not str(company_addr_city_level).isdigit():
        raise FeatureProcessError('%s city_level config error in database table' % city_name)
    seq = int(company_addr_city_level)
    if seq == 1:
        seq = "一线"
    elif seq == 2:
        seq = "二线"
    elif seq == 3:
        seq = "三线"
    elif seq == 4:
        seq = "四线"
    elif seq == 5:
        seq = "其他"
    return seq


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
    company_addr_city_code = ccf[0].city_code
    if not str(company_addr_city_code).isdigit():
        raise FeatureProcessError('%s city_code config error in database table' % city_name)
    seq = company_addr_city_code
    return seq


def m_max_flight_area(seq):
    """
       一年内飞机出行中最多出行区域
        :param seq: 飞行次数、国内次数、国外次数
        :return:    飞行次数==0 返回0    国内次数>国外次数 返回inland 国外次数>国内次数 返回international
        example：
                :seq  [2, 2, 3]
                :return  international
    """
    """"""
    flight_times = seq[0]
    inland_count = seq[1]
    international_count = seq[2]
    if int(flight_times) == 0:
        seq = 0
    elif int(inland_count) >= int(international_count):
        seq = 'inland'
    elif int(inland_count) < int(international_count):
        seq = 'international'
    else:
        raise FeatureProcessError("don't know  max_flight_area code")
    return seq


def m_max_flight_class(seq):
    """
       一年内飞机出行中最多机舱类型
        :param seq: [商务舱乘机次数、公务舱乘机次数、经济舱乘机次数]
        :return:    乘机次数==0 返回0    乘坐商务舱最多 返回business_class 乘坐公务舱最多 executive_class 乘坐经济舱最多 返回tourist_class
        example：
                :seq  [2, 2, 3]
                :return  tourist_class
    """
    temp_index = seq.index(max(seq))
    result = ''
    if sum(seq) == 0:
        result = 0
    elif temp_index == 0:
        result = 'business_class'
    elif temp_index == 1:
        result = 'executive_class'
    elif temp_index == 2:
        result = 'tourist_class'
    return result


def m_get_work_status_map(seq, feature_name):
    """
    对seq数据针对工作状态匹配相应code码
    :param seq: 工作状态(汉子字符串)
    :param feature_name: 特征名称分
    :return: 工作状态code码
    """
    fcm = FeatureCodeMapping.objects.filter(
        feature_name=feature_name
    )
    work_status_tags = seq[0].encode('utf-8')[-12:]
    status_map = {conf.mapped_value: conf.unitary_value for conf in fcm}
    for key, value in status_map.iteritems():
        if work_status_tags in value:
            return int(key)


def m_get_max_month_to_now(seq):
    """
    计算时间字符串列表中时间距离今天的最长月数
    计算逻辑为天数除以30
    时间字符串'999999'代表当前  做去除处理
    :param seq: 时间列表
    :return: 传入列表中距离当前时间最长的月数
    """

    if '999999' in seq:
        seq.remove('999999')
    today = datetime.today()
    days_list = []
    for str_date in seq:
        dates = datetime.strptime(str_date, '%Y%m')
        days_list.append((today - dates).days)
    return max(days_list) / 30


def m_seq_inx_to_int(seq, args=0):
    """
        将列表中单个列表中元素转成int，返回新的列表
        :param seq: 列表形成的列表
        :param args: 列表的次序
        :return:    转换后的列表
        example：
                :seq  [['30', 0], ['5', 1]]
                :args   0
                :return  [[30, 0], [5, 1]]
    """
    for i in seq:
        i[args] = int(i[args])
    return seq


def m_now_industry_code(seq):
    """
        获取当前工作行业
        :param seq: 历史工作列表 行业结束时间为999999时代表当前从事行业
        :return:    当前工作行业 当前没有工作返回空
        example：
                :seq  [['30', 0], ['5', 1],['999999', 1]]
                :return  1
    """
    tmp = ''
    for i in seq:
        if i[0] == '999999':
            tmp = i[1]
            break
    return tmp


def m_industry_code_to_str(seq, feature_name):
    feature_code = FeatureCodeMapping.objects.filter(
        feature_name=feature_name,
    )
    num_map = {int(conf.mapped_value): conf.feature_desc for conf in feature_code}
    for key, value in num_map.iteritems():
        if seq == key:
            return value


def m_r_to_now_work_time(seq):
    """
    计算传入参数两个时间点距离当前时间的月数
    计算逻辑:
        距离今天的天数除以30得到月数, 时间'999999' 也代表今天
    :param seq: 时间列表
    :param args: 列表元素标记 标记比较接近当前时间的元素下标
    :return:
    """

    now_time = datetime.now()
    if '999999' in seq:
        now_work_time = (now_time - datetime.strptime(seq[1], '%Y%m')).days / 30
        return now_work_time
    else:
        now_work_time = (datetime.strptime(seq[0], '%Y%m') - datetime.strptime(seq[1], '%Y%m')).days / 30
        return now_work_time


def m_college_type(seq):
    """
    获取学校的类型信息
    当学校的类型是985,211工程院校时：
        :param seq:【“985,211工程院校”，“本科”】
        :return:“985工程院校”
    当学校的类型是211工程院校时：
        :param seq:【“211工程院校”，“硕士”】
        :return:“211工程院校”
    当学校的类型是普通本科或者专科时：
       如果获取的某人的学历信息是博士、硕士和本科时
       输出的学校类型为普通本科
       :param seq:【“****”，“硕士”】
       :return:“普通本科”
       如果获取的某个人的学历信息时专科时：
       输出的学校类型为专科
       :param seq:【“****”，“专科”】
       :return:“专科”

    """
    if "985" in seq[0]:
        tmp = "985,211工程院校"
        return tmp
    elif "211" in seq[0] and "985" not in seq[0]:
        tmp = "211工程院校"
        return tmp
    else:
        if seq[1] in ["博士", "硕士", "本科"]:
            tmp = "本科"
            return tmp
        else:
            tmp = "专科"
            return tmp


def m_education_degree_check(seq, feature_name):
    """
       获取单值匹配(不是区间)所对应的Code

        :param feature_name: 特征名称
        :param seq: 特征对应的返回值
        :return:    code

        example：
                :feature_name education_degree_check
                :data: 30
                :return  2
    """
    feature_code = FeatureCodeMapping.objects.filter(
        feature_name=feature_name,
    )
    num_map = {int(conf.mapped_value): conf.unitary_value for conf in feature_code}
    for key, value in num_map.iteritems():
        if seq == value:
            return key


def m_del_dict_invalid_value(seq, args=1):
    """
    删除列表中的无效值 None '' {} [] 0 False
    :param seq: 原始字典
    :param args: 字典深度即循环的次数
    :return: 转换后的字典
    example：
                :seq  data = {
                                "matchType": "",
                                "matchValue": "",
                                "matchId": "",
                                "classification": [
                                    {
                                        "M3": {
                                            "bankCredit": 0,
                                            "otherLoan": {
                                                "longestDays": ''
                                            },
                                            "otherCredit": None,
                                            "bankLoan": None
                                        }
                                    },
                                    {}
                                ]
                            }
                :args   5
                :return  {}
    """
    for i in xrange(args):
        tmp = seq.copy()
        for key, value in tmp.items():
            if not value:
                del seq[key]

            elif isinstance(value, dict):
                m_del_dict_invalid_value(value, 1)
            elif isinstance(value, list):
                m_del_invalid_value(value, 1)
    return seq


def m_del_invalid_value(seq, args=1):
    """
        删除列表中的无效值 None '' {} [] 0 False
        :param seq: 原始序列 list
        :param args: seq深度即循环的次数
        :return:    转换后的列表
        example：
                :seq  data = [{
                                "matchType": "",
                                "matchValue": "",
                                "matchId": "",
                                "classification": [
                                    {
                                        "M3": {
                                            "bankCredit": 0,
                                            "otherLoan": {
                                                "longestDays": ''
                                            },
                                            "otherCredit": None,
                                            "bankLoan": None
                                        }
                                    },
                                    {}
                                ]
                            }]
                :args   6
                :return  []
    """
    for i in xrange(args + len(seq)):
        for data in seq:
            if not data:
                seq.remove(data)
            if isinstance(data, dict):
                m_del_dict_invalid_value(data, 1)
            elif isinstance(data, list):
                m_del_invalid_value(data, 1)
    return seq


def m_check_code(seq, args=None):
    """
    将数值转化成对应的code
    :param seq:  上一步得到的数据
    :param args:  [feature_name,操作符]
    :return:  对应code

    example：
                :data:         20
                :args         ['education_degree_code','gte_lt']
                :return         2
    """
    if not seq:
        return []
    feature_name = args[0]
    op = args[1]
    fcm = FeatureCodeMapping.objects.filter(
        feature_name=feature_name,
    )
    res = ''
    num_map = {int(conf.mapped_value): [conf.unitary_value, conf.dual_value] for conf in fcm}
    for key, value in num_map.iteritems():

        if op == 'gte_lt':
            if float(value[0]) <= float(seq) < float(value[1]):
                res = key
                break
        elif op == 'gt_lte':
            if float(value[0]) < float(seq) <= float(value[1]):
                res = key
                break
        elif op == 'in':
            if seq in value[0]:
                res = key
                break
        elif op == 'eq':
            if seq == value[0]:
                res = key
                break
    if res in ('', None):
        raise FeatureProcessError("don't find %s=%s code value" % (feature_name, seq))
    return res


def m_to_code(seq, args=None):
    """
    将数值转化成对应的code
    :param seq:  上一步得到的数据
    :param args:  feature_name
    :return:  对应code

    example：
                :data:         20
                :args         'education_degree_code'
                :return         2
    """
    if not seq and seq != 0:
        return []
    if isinstance(seq, list):
        seq = seq[0]
    feature_name = args
    fcm = FeatureCodeMapping.objects.filter(
        feature_name=feature_name,
        is_delete=False
    )
    res = ''
    num_map = {int(conf.mapped_value): [conf.unitary_value, conf.dual_value, conf.arithmetic_type, conf.feature_desc]
               for conf in fcm}
    for key, value in num_map.iteritems():
        arithmetic_type = value[2]
        if arithmetic_type == '[)':
            if float(value[0]) <= float(seq) < float(value[1]):
                res = key
                break
        elif arithmetic_type == '(]':
            if float(value[0]) < float(seq) <= float(value[1]):
                res = key
                break
        elif arithmetic_type == '()':
            if float(value[0]) < float(seq) < float(value[1]):
                res = key
                break
        elif arithmetic_type == '>=':
            if float(seq) >= float(value[0]):
                res = key
                break
        elif arithmetic_type == '<=':
            if float(seq) <= float(value[0]):
                res = key
                break
        elif arithmetic_type == 'in':
            if seq in value[0]:
                res = key
                break
        elif arithmetic_type == '==':
            if str(seq) == value[0]:
                res = value[3]
                break
    if res in ('', None):
        raise FeatureProcessError("don't find %s=%s code value" % (feature_name, seq))
    return res


def m_mobile_id_judge(seq):
    """
    对手机号码三元素认证进行结果输出
    分流逻辑特殊处理
    :param seq: 传入数据
    :return: 判断结果 列表
    """
    if seq and seq[0] == '00':
        return [1]
    else:
        return [0]


def m_single_check_code(seq, feature_name):
    """
       获取单值匹配(不是区间)所对应的Code

        :param feature_name: 特征名称
        :param seq: 特征对应的返回值
        :return:    code

        example：
                :feature_name education_degree_code
                :seq: 20
                :return  2
    """
    if not seq:
        return []
    res = ''
    feature_code = FeatureCodeMapping.objects.filter(
        feature_name=feature_name,
    )
    num_map = {int(conf.mapped_value): conf.unitary_value for conf in feature_code}
    for key, value in num_map.iteritems():
        if seq[0] == value:
            res = key
            break
    if res in ('', None):
        raise FeatureProcessError("don't find %s=%s code value" % (feature_name, seq))
    return res


def m_yd_online_time(seq):
    """
       获取移动手机在网时长所对应的code

        :param seq: 移动在网时长区间
        :return:    code

        example：
                :seq: (0,3)
                :return  1
    """
    if not seq:
        return []
    if seq[0] in ["(0,3)", "[3,6)"]:
        seq = [1]
    elif seq[0] in ["[6,12)"]:
        seq = [2]
    elif seq[0] in ["[12,18)", "[18,24]"]:
        seq = [3]
    elif seq[0] in ["(24,+)"]:
        seq = [4]
    return seq


def m_unicom_online_time(seq):
    """
       获取联通手机在网时长所对应的code

        :param seq: 联通在网时长区间
        :return:    code

        example：
                :seq: [0-1]
                :return  1
    """
    if not seq:
        return []
    if seq[0] in ["[0-1]", "(1-2]", "[3-6]"]:
        seq = [1]
    elif seq[0] in ["[7-12]"]:
        seq = [2]
    elif seq[0] in ["[13-24]"]:
        seq = [3]
    elif seq[0] in ["[25-36]", "[37,+)"]:
        seq = [4]
    return seq


def m_telecom_online_time(seq):
    """
       获取电信手机在网时长所对应的code

        :param seq: 电信在网时长区间
        :return:    code

        example：
                :seq: [0-6)
                :return  1
    """
    if not seq:
        return []
    if seq[0] in ["[0-6)"]:
        seq = [1]
    elif seq[0] in ["[6-12)"]:
        seq = [2]
    elif seq[0] in ["[12-24)"]:
        seq = [3]
    elif seq[0] in ["[24-36)", "[36,+]"]:
        seq = [4]
    return seq


def m_yd_online_time2_0(seq):
    """
       获取移动手机在网时长所对应的code

        :param seq: 移动在网时长区间
        :return:    code

        example：
                :seq: (0,3)
                :return  1
    """
    if not seq:
        return []
    if seq[0] in ["(0,3)", "[3,6)"]:
        seq = ["(0_6)"]
    elif seq[0] in ["[6,12)"]:
        seq = ["[6_12)"]
    elif seq[0] in ["[12,18)", "[18,24]"]:
        seq = ["[12_24)"]
    elif seq[0] in ["(24,+)"]:
        seq = ["[24_+)"]
    return seq


def m_unicom_online_time2_0(seq):
    """
       获取联通手机在网时长所对应的code

        :param seq: 联通在网时长区间
        :return:    code

        example：
                :seq: [0-1]
                :return  1
    """
    if not seq:
        return []
    if seq[0] in ["[0-1]", "(1-2]", "[3-6]"]:
        seq = ["(0_6)"]
    elif seq[0] in ["[7-12]"]:
        seq = ["[6_12)"]
    elif seq[0] in ["[13-24]"]:
        seq = ["[12_24)"]
    elif seq[0] in ["[25-36]", "[37,+)"]:
        seq = ["[24_+)"]
    return seq


def m_telecom_online_time2_0(seq):
    """
       获取电信手机在网时长所对应的code

        :param seq: 电信在网时长区间
        :return:    code

        example：
                :seq: [0-6)
                :return  1
    """
    if not seq:
        return []
    if seq[0] in ["[0-6)"]:
        seq = ["(0_6)"]
    elif seq[0] in ["[6-12)"]:
        seq = ["[6_12)"]
    elif seq[0] in ["[12-24)"]:
        seq = ["[12_24)"]
    elif seq[0] in ["[24-36)", "[36,+]"]:
        seq = ["[24_+)"]
    return seq


def m_lp_income(seq, discount):
    """
       获取猎聘返回的用户年收入,即最近一份工作的月薪个数与月薪的乘积,乘以折扣比率,保留两位小数

        :param seq: 职业信息列表
        :param discount: 年薪的折扣比率

        :return:  年收入

        example：
                :seq: ["work_exp_form": [{
                        "months": 13,
                        "salary": 6000,
                        "work_end": "201006",
                    },
                    {
                        "months": 12,
                        "salary": 12000,
                        "work_end": "200806",
                    },
                    {
                        "months": 12,
                        "salary": 5000,
                        "work_end": "999999",}]]

                :discount: 0.56
                :return  33600
    """
    if not seq:
        return []
    work_end_map = {int(i['work_end']): [i['salary'], i['months']] for i in seq[0]}
    last_work = work_end_map.keys()
    last_work = max(last_work)

    income = round((work_end_map[last_work][0] * work_end_map[last_work][1] * discount), 2)
    return [income]


def m_single_to_list(seq):
    """
    转换单值为列表
    :param seq: 5
    :return:[5]
    """
    if isinstance(seq, list):
        return seq
    return [seq]


def m_to_str(seq):
    """

    :param seq:
    :return:
    """
    res = []
    if isinstance(seq, list):
        for i in seq:
            res.append(str(i))
        return res
    return str(seq)


def m_code_to_collage_type(seq):
    if seq == '1':
        seq = "专科"
    elif seq == '2':
        seq = "普本"
    elif seq == '3':
        seq = "211院校"
    elif seq == '4':
        seq = "985院校"
    return seq


def m_get_income_expense_comparison(seq, args=None):
    """
       获取用户的入账与支出关系

        :param seq: 入账和支出信息

        :return:  入账/支出的比率或空列表


    """
    amount_dict = {'0': 500, '1': 1500, '2': 2500, '3': 3500, '4': 4500, '5': 5500, '6': 6500, '7': 7500, '8': 8500,
                   '9': 9500, 'a': 15000, 'b': 25000, 'c': 35000, 'd': 45000, 'e': 55000, 'f': 65000, '10': 75000,
                   '11': 85000, '12': 95000, '13': 150000, '14': 250000, '15': 350000, '16': 450000, '17': 550000,
                   '18': 650000, '19': 750000, '1a': 850000, '1b': 950000, '1c': 1500000, '1d': 2500000, '1e': 3500000,
                   '1f': 4500000, '20': 5500000, '21': 6500000, '22': 7500000, '23': 8500000, '24': 9500000,
                   '25': 15000000
                   }

    ratio = ''
    income_level = ''
    expense_level = ''
    if isinstance(seq, list) and seq:
        seq = seq[0]
    if not (seq and isinstance(seq, dict)):
        return [ratio]
    if args == 'unicome':
        income_level = amount_dict.get(seq.get('income_range'))
        expense_level = amount_dict.get(seq.get('charge_off_range'))
    if args == 'cc_credit':
        income_level = seq.get('debit_card_12m_passentry_amount')
        expense_level = seq.get('debit_card_12m_chargeoff_amount')
    if income_level and expense_level:
        if income_level == expense_level:
            ratio = 1
        else:
            ratio = float(income_level) / float(expense_level)
    return [ratio]


def m_to_nature_card(seq):
    code = seq
    cmap = {
        "00": "UNKNOWN",
        "01": "借记卡",
        "02": "贷记卡",
        "03": "准贷记卡",
        "04": "借贷合一卡",
        "05": "预付费卡",
    }
    return cmap[code]


def m_d_c_s_r_l003(seq):
    if seq[0] in ['02']:
        return int(seq[1])
    else:
        return PositiveSignedTypeDefault


def m_list_average(seq):
    sum_num = sum(seq)
    return sum_num / len(seq)


def m_get_max(seq):
    return max(seq)


def m_time_to_string_bfm(seq):
    time_code = int(seq[0])
    # today = datetime.today()
    # base_time = datetime(today.year, today.month, today.day, 0, 0, 0)
    time_hour_min = time.strftime("%H:%M", time.localtime(time_code))
    # base_time_num = int(time.mktime(time.strptime(base_time.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")))
    # difference = int(time_code) - base_time_num
    #
    # if (difference > 0) and (difference <= 25200):
    #     seq = '00:01 - 7:00'
    # elif (difference > 25200) and (difference <= 32400):
    #     seq = '7:01 - 9:00'
    # elif (difference > 32400) and (difference <= 41400):
    #     seq = '9:01 - 11:30'
    # elif (difference > 41400) and (difference <= 50400):
    #     seq = '11:31 - 14:00'
    # elif (difference > 50400) and (difference <= 61200):
    #     seq = '14:01 - 17:00'
    # elif (difference > 61200) and (difference <= 79200):
    #     seq = '17:01 - 22:00'
    # elif (difference > 79200) and (difference <= 86400):
    #     seq = '22:01 - 00:00'
    # else:
    #     seq = 'UNKNOWN'
    if (time_hour_min > '00:01') and (time_hour_min <= '07:00'):
        seq = '00:01 - 7:00'
    elif (time_hour_min > '07:01') and (time_hour_min <= '09:00'):
        seq = '7:01 - 9:00'
    elif (time_hour_min > '09:01') and (time_hour_min <= '11:30'):
        seq = '9:01 - 11:30'
    elif (time_hour_min > '11:31') and (time_hour_min <= '14:00'):
        seq = '11:31 - 14:00'
    elif (time_hour_min > '14:01') and (time_hour_min <= '16:00'):
        seq = '14:01 - 16:00'
    elif (time_hour_min > '16:01') and (time_hour_min <= '18:30'):
        seq = '16:01 - 18:30'
    elif (time_hour_min > '18:31') and (time_hour_min <= '21:30'):
        seq = '18:31 - 21:30'
    elif (time_hour_min > '21:31') and (time_hour_min <= '23:59'):
        seq = '21:31 - 00:00'
    elif time_hour_min == '00:00':
        seq = '21:31 - 00:00'
    else:
        seq = 'UNKNOWN'
    return seq


def m_first_equal_next(seq):
    if seq[0] == seq[1]:
        return "是"
    else:
        return "否"


def m_yes_no(seq):
    if seq[0] == "yes":
        return "是"
    else:
        return "否"


def m_first_in_next(seq):
    if seq[0] in seq[1]:
        return "是"
    else:
        return "否"


def m_bfm_risk(seq, risk_list):
    for i in seq:
        if i in risk_list:
            return "是"
    return "否"


def m_c_d_t_b268(seq):
    c_d_t_b268 = seq[0]
    home_address = seq[1]
    if not isinstance(c_d_t_b268, unicode):
        c_d_t_b268 = unicode(c_d_t_b268)
    if not isinstance(home_address, unicode):
        home_address = unicode(home_address)
    if c_d_t_b268[-1] == u"市":
        c_d_t_b268 = c_d_t_b268[:-1]

    if c_d_t_b268 in home_address:
        return "是"

    return "否"


def m_p2p_count(seq):
    count = P2PTelephoneModel.objects.filter(telephone__in=seq).values_list("telephone").distinct().count()
    return count


def m_loan_agency_count(seq):
    count = LoanAgencyModel.objects.filter(telephone__in=seq).values_list("telephone").distinct().count()
    return count


def m_car_room_code(seq):
    m = {
        1: "有车",
        2: "可能有车",
        3: "无法判断"
    }
    if seq in m:
        return m[seq]
    else:
        return "UNKNOWN"


def m_room_code(seq):
    m = {
        1: "有购房交易",
        2: "可能购房交易",
        3: "无法判断"
    }
    if seq in m:
        return m[seq]
    else:
        return "UNKNOWN"


def m_call_time_type(seq):
    days = [x.hour for x in seq]
    trans = [1 if x in range(6, 22) else 2 for x in days]
    type1 = trans.count(1)
    type2 = trans.count(2)
    if type1 >= type2:
        return "生活型"
    elif type1 < type2:
        return "夜话型"


def m_a_per_in_b(seq, args):
    args_count = seq.count(args)
    return args_count / len(seq)


def m_date_less_x_days(seq, args):
    t = datetime.now() - timedelta(args)
    l = [i for i in seq if i >= t]
    return l


def m_true_false_to_sf(seq):
    if seq[0]:
        return '是'
    else:
        return '否'


if __name__ == '__main__':
    data = [
        {
            "res": 9,
            "product_code": "string",
            "name": "string",
            "card_id": "string",
            "mobile": "string",
            "email": "string",
            "registration_on": "2016-10-01 12:20:10",
            "city_code": "string",
            "city_name": "string",
            "now_indust_code": "string",
            "now_indust_name": "string",
            "work_age": 0,
            "complete_degree": 0,
            "cur_work_status": "string",
            "upload_contact": 0,
            "sns_friends_cnt": 0,
            "sns_sd_friend_cnt": 0,
            "sns_h_fans_cn": 0,
            "sns_skill_tag_list": [
                {
                    "skill_tag": "string",
                    "certified_num": 0
                }
            ],
            "work_exp_form": [
                {
                    "title": "string",
                    "has_certified": "string",
                    "certified_num": 0,
                    "comp_name": "string",
                    "months": 0,
                    "salary": 0,
                    "work_start": "201605",
                    "work_end": '999999',
                    "industry": "数云普惠",
                    "industry_name": "string",
                    "dq": "string",
                    "dq_name": "string"
                },

            ],
            "edu_exp_form": [
                {
                    "school": "string",
                    "start": "string",
                    "end": "string",
                    "degree": "5",
                    "degree_name": "string",
                    "tz": 0
                },
                {
                    "school": "string",
                    "start": "string",
                    "end": "string",
                    "degree": "30",
                    "degree_name": "string",
                    "tz": 1
                }
            ]
        },
    ]
    # data = m_r_to_now_work_time()
    data = m_to_slice("5%", [0, -1])
    print data
