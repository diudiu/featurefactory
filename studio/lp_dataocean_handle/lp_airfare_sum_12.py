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

logger = logging.getLogger('apps.common')


class Handle(object):
    def __init__(self, data):
        self.data = data

    def handle(self):
        """
        接口名称：乘机人信息查询  airline_passenger_info
        字段名称：average_price              平均票价
                  flight_times               一年中飞行次数

        输出：
        特征名称：airfare_sum_12             一年中乘机总票价
        """
        try:
            result = {
                'airfare_sum_12': 9999
            }

            if self.data['result'] == '00':
                average_price = self.data['content'].get('average_price', None)
                flight_times = self.data['content'].get('flight_times', None)
                if average_price and flight_times:
                    result['airfare_sum_12'] = average_price * flight_times

        except Exception as e:
            logging.error(e.message)

        return result
