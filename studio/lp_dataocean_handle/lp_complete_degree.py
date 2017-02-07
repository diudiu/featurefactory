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
        接口名称：
        猎聘
        字段名称：
        'complete_degree': 简历完成度 int

        输出:
        特征名称:
        'complete_degree': 简历完成度 int
        """

        result = {
            "complete_degree": 999999,
        }
        try:
            base_data = self.data["complete_degree"]
        except Exception as e:
            # TODO log this error
            return result
        if not base_data or not isinstance(base_data, int):
            return result

        result["complete_degree"] = base_data

        return result
