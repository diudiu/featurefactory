# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2013- DIGCREDIT, All Rights Reserved.
    -----------------------------------------------------------
    Author: Z.L
    Date:  2017/02/17
    Change Activity:
"""
from vendor.utils.defaults import UnsignedIntTypeDefault

import logging

logger = logging.getLogger('apps.common')


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        输入:
        接口名称：人人信车辆信息查询
        字段名称：'result': 取值范围为[object,null]

        计算逻辑:提取人人信返回车辆信息的列表,列表的每个元素为一辆车的信息,
                计算列表长度即为车辆个数,输出类型为int

        输出:
        特征名称: 'car_count': 车辆个数 int
        """

        result = {"car_count": UnsignedIntTypeDefault}
        try:
            base_data = self.data["result"]
            for data in base_data:
                if not data:
                    base_data.remove(data)  # 删除列表中为空的元素
            if base_data and isinstance(base_data, list):
                result["car_count"] = len(base_data)  # 计算列表长度

        except Exception as e:
                logging.error(e.message)
        finally:
            return result

