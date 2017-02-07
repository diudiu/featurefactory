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
        'high_way_over_load': 高速超载统计查询
        字段名称：
        'month_times': 超载总次数 str

        输出:
        特征名称:
        'overload_count': 超速次数 int
        """

        result = {
            'overload_count': 999999,
        }

        month_times = 0
        for data in self.data:
            try:
                base_data = self.data[data]["content"]["over_load_list"]
            except Exception as e:
                # TODO log this error
                return result
            if not base_data or not isinstance(base_data, list):
                return result
            for car_data in base_data:
                month_times += int(car_data["month_times"])

        result['overload_count'] = month_times
        return result
