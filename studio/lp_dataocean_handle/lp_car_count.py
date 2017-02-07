# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: ZL
    Date:  2017/01/18
    Change Activity:
"""


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口名称：人人信
        字段名称：
        'result': 取值范围为[object,null]

        输出:
        特征名称:
        'car_count': 车辆个数 int
        """

        result = {
            "car_count": 999999,
        }
        try:
            base_data = self.data["result"]
        except Exception as e:
            # TODO log this error
            return result
        if not base_data or not isinstance(base_data, list):
            return result

        result["car_count"] = len(base_data)

        return result
