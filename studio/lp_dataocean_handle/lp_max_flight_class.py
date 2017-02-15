# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: Sun Fei
    Date:  2017/1/23
    Change Activity:
"""
import logging
from featurefactory.vendor.errors.fecture_error import MyException
logger = logging.getLogger('apps.common')


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):
        """
        接口名称：乘机人信息查询  airline_passenger_info
        字段名称：flight_times               一年中飞行次数
                  business_class_count       商务舱乘机次数
                  executive_class_count      公务舱乘机次数
                  tourist_class_count        经济舱乘机次数

        输出：
        特征名称：max_flight_class           一年内飞机出行中最多机舱类型
        """
        try:
            result = {'max_flight_class': '9999'}  # 9999：异常
            tip = self.data.get('result', None)
            if not tip:
                raise MyException(message='get (result) fail')
            if self.data['result'] == u'00':
                content = self.data.get('content', None)
                if content:
                    business_class_count = content.get('business_class_count', None)
                    executive_class_count = content.get('executive_class_count', None)
                    tourist_class_count = content.get('tourist_class_count', None)
                    count_list = []
                    count_list.append(int(tourist_class_count))
                    count_list.append(int(executive_class_count))
                    count_list.append(int(business_class_count))
                    temp_index = count_list.index(max(count_list))
                    if sum(count_list) == 0:
                        result['max_flight_class'] = '乘机次数为零'
                    elif temp_index == 0:
                        result['max_flight_class'] = '经济舱'
                    elif temp_index == 1:
                        result['max_flight_class'] = '公务舱'
                    elif temp_index == 2:
                        result['max_flight_class'] = '商务舱'
        except MyException as e:
            logging.error(e.message)
        except Exception as e:
            logging.error(e.message)
        finally:
            return result
