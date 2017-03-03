# -*- coding:utf-8 -*-
import os
import sys
import re
import math
from datetime import datetime

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
    seq = float(sum(seq)) / len(seq)
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
            :param city: 地址
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
    seq = int(company_addr_city_code)
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
        raise FeatureProcessError("don't know  max_flight_area code")
    return seq


def m_max_flight_class(seq):
    """
       一年内飞机出行中最多机舱类型的code
        :param seq: [商务舱乘机次数、公务舱乘机次数、经济舱乘机次数]
        :return:    code
        example：
                :seq  [2, 2, 3]
                :return  1
    """
    temp_index = seq.index(max(seq))
    result = ''
    if sum(seq) == 0:
        result = 4
    elif temp_index == 0:
        result = 3
    elif temp_index == 1:
        result = 2
    elif temp_index == 2:
        result = 1
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


def m_get_month_from_now(seq):
    """
    计算时间字符串列表中时间距离今天的最长月数
    计算逻辑为天数除以30
    时间字符串'999999'代表当前  做去除处理
    :param seq: 时间戳列表
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


def m_seq_inx_to_999999(seq, args=0):
    """
        将列表中为‘999999’得提取出来
        :param seq: 列表形成的列表
        :param args: 列表的次序
        :return:    转换后的列表
        example：
                :seq  [['30', 0], ['5', 1]]
                :args   0
                :return  [[30, 0], [5, 1]]
    """
    for i in seq:
        if i[args] == '999999':
            seq = i
        else:
            seq = [i[args], '']
    return seq


def m_r_to_now_work_time(seq, args=0):
    """
    计算传入参数两个时间点距离当前时间的月数
    计算逻辑:
        距离今天的天数除以30得到月数, 时间'999999' 也代表今天
    :param seq: 时间列表
    :param args: 列表元素标记 标记比较接近当前时间的元素下标
    :return:
    """
    now_time = datetime.now()
    end_work_time = datetime.strptime(seq[0], '%Y%m')
    start_work_time = datetime.strptime(seq[1], '%Y%m')
    if seq[args] == '999999':
        seq[args] = now_time
        now_work_time = (now_time - start_work_time).days / 30
    else:
        now_work_time = (end_work_time - start_work_time).days / 30
    return now_work_time


def m_college_type(seq):
    """
    获取学校的类型信息
    当学校的类型是985,211工程院校时：
        :param seq:【“985,211工程院校”，“本科”】
        :return:【“985工程院校”】
    当学校的类型是211工程院校时：
        :param seq:【“211工程院校”，“硕士”】
        :return:【“211工程院校”】
    当学校的类型是普通本科或者专科时：
       如果获取的某人的学历信息是博士、硕士和本科时
       输出的学校类型为普通本科
       :param seq:【“****”，“硕士”】
       :return:【“普通本科”】
       如果获取的某个人的学历信息时专科时：
       输出的学校类型为专科
       :param seq:【“****”，“专科”】
       :return:【“专科”】

    """
    if "985" in seq[0]:
        tmp = ["985工程院校"]
        return tmp
    elif "211" in seq[0] and "985" not in seq[0]:
        tmp = ["211工程院校"]
        return tmp
    else:
        if seq[1] in ["博士", "硕士", "本科"]:
            tmp = ["普通本科"]
            return tmp
        else:
            tmp = ["专科"]
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
    if not res:
        raise FeatureProcessError("don't find %s=% code value" % (feature_name, seq))
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
    feature_code = FeatureCodeMapping.objects.filter(
        feature_name=feature_name,
    )
    num_map = {int(conf.mapped_value): conf.unitary_value for conf in feature_code}
    for key, value in num_map.iteritems():
        if seq[0] == value:
            return key


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

    :param seq:
    :return:
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

if __name__ == '__main__':
    data = [
        {
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
        },
        {
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
    ]
    data = m_del_invalid_value(data, 6)
    print data
