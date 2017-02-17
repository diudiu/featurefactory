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
        接口名称：猎聘预授信接口
        字段名称：'complete_degree': 简历完成度 int

        计算逻辑: 直接从接口提取,输出类型为int

        输出:
        特征名称: 'complete_degree': 简历完成度 int
        """

        result = {
            "complete_degree": 9999,
        }
        try:
            base_data = self.data["complete_degree"]
            if not isinstance(base_data, int):
                return result

            result["complete_degree"] = base_data

            return result
        except Exception as e:
            # TODO log this error
            return result

