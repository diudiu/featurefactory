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
        接口名称：'personal_info': 个人基本信息查询
        字段名称：'age': 年龄 int

        计算逻辑: 直接从接口提取年龄,输出类型为int

        输出:
        特征名称: 'age': 年龄 int
        """

        result = {
            'age': '9999',
        }
        try:
            base_data_age = self.data["content"]["age"]    # 提取年龄字段
            if not base_data_age or not isinstance(base_data_age, int):
                return result

            result['age'] = base_data_age
            return result
        except Exception as e:
            # TODO log this error
            return result

