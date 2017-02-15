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
from vendor.errors.fecture_error import MyException
logger = logging.getLogger('apps.common')


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):
        """
        接口名称：乘机人信息查询  airline_passenger_info
        字段名称：flight_times               一年中飞行次数
                  inland_count               国内飞行次数
                  international_count        国外飞行次数

        输出：
        特征名称：max_flight_area            一年内飞机最多出行区域
        """
        try:
            result = {'max_flight_area': 9999}  # 9999：异常
            tip = self.data.get('result', None)
            if not tip:
                raise MyException(message='get (result) fail')
            if self.data['result'] == u'00':
                content = self.data.get('content', None)
                if content:
                    flight_times = content.get('flight_times', None)
                    inland_count = content.get('inland_count', None)
                    international_count = content.get('international_count', None)
                    if int(flight_times) == 0:
                        result['max_flight_area'] = '乘机次数为零'
                    elif int(inland_count) >= int(international_count):
                        result['max_flight_area'] = '国内'
                    elif int(inland_count) < int(international_count):
                        result['max_flight_area'] = '国外'
        except MyException as e:
            logging.error(e.message)
        except Exception as e:
            logging.error(e.message)
        finally:
            return result


