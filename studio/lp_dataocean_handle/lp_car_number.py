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
        接口名称：人人信
        字段名称：
        'license_no': 车牌号 str

        输出:
        特征名称:
        'car_number': 车牌号 list
        """

        result = {
            "car_number": 999999,
        }
        try:
            base_data = self.data["result"]
        except Exception as e:
            # TODO log this error
            return result
        if not base_data or not isinstance(base_data, list):
            return result

        car_list = []
        for data in base_data:
            car_list.append(data.get("license_no"))

        result["car_number"] = car_list
        return result
