# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: ZL
    Date:  2017/01/24
    Change Activity:
"""


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口名称：
        'high_way_over_speed': 高速超速统计查询
        字段名称：
        'month_times': 超速次数 str

        输出:
        特征名称:
        'overspeed_count': 超速次数 int
        """

        result = {
            'overspeed_count': 999999,
        }

        month_times = 0
        for data in self.data:
            try:
                base_data = self.data[data]["content"]["over_speed_list"]
            except Exception as e:
                # TODO log this error
                return result
            if not base_data or not isinstance(base_data, list):
                return result
            for car_data in base_data:
                month_times += int(car_data["month_times"])

        result['overspeed_count'] = month_times
        return result
