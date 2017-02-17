# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2013- DIGCREDIT, All Rights Reserved.
    -----------------------------------------------------------
    Author: Z.L
    Date:  2017/01/18
    Change Activity:
"""


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        输入:
        接口名称：人人信车辆信息查询
        字段名称：'result': 取值范围为[object,null]

        计算逻辑:提取人人信返回车辆信息的列表,计算列表长度,输出类型为int

        输出:
        特征名称: 'car_count': 车辆个数 int
        """

        result = {
            "car_count": 9999,
        }
        try:
            base_data = self.data["result"]
            if not base_data or not isinstance(base_data, list):
                return result
            result["car_count"] = len(base_data)  # 计算列表长度

            return result
        except Exception as e:
            # TODO log this error
            return result

