# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2013- DIGCREDIT, All Rights Reserved.
    -----------------------------------------------------------
    Author: Z.L
    Date:  2017/02/17
    Change Activity:
"""
import logging

from vendor.utils.defaults import *

logger = logging.getLogger('apps.common')


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        输入:
        接口名称：人人信车辆信息查询
        字段名称：'license_no' 车牌号 str

        计算逻辑: 从人人信车辆信息接口提取车辆信息列表,列表的每个元素为一辆车的信息,
                 从每辆车的信息中提取车牌号组成list,输出为所有车的车牌号列表,类型为list

        输出:
        特征名称: 'car_number' 车牌号 list
        """

        result = {"car_number": ListTypeDefault}
        try:
            base_data = self.data["result"]
            if base_data and isinstance(base_data, list):  # 判断车辆信息列表不为空且为list
                car_list = [data.get("license_no", '') for data in base_data if data.get("license_no", '')]
                result["car_number"] = car_list

        except Exception as e:
                logging.error(e.message)
        return result

