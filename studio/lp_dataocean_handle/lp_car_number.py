# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2013- DIGCREDIT, All Rights Reserved.
    -----------------------------------------------------------
    Author: Z.L
    Date:  2017/01/24
    Change Activity:
"""


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        输入:
        接口名称：人人信车辆信息查询
        字段名称：'license_no' 车牌号 str

        计算逻辑:从人人信车辆信息接口提取车辆信息列表,输出车牌号列表,类型为list

        输出:
        特征名称: 'car_number' 车牌号 list
        """

        result = {
            "car_number": 9999,
        }
        try:
            base_data = self.data["result"]
            if not base_data or not isinstance(base_data, list):
                return result

            # 遍历车辆信息,提取所有车牌号组成list
            car_list = []
            for data in base_data:
                car_list.append(data.get("license_no"))

            result["car_number"] = car_list
            return result
        except Exception as e:
            # TODO log this error
            return result

