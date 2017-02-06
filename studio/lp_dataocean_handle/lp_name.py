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
        接口名称：猎聘
        字段名称：
        'name': 姓名

        输出:
        特征名称:
        'name': 姓名 str
        """

        result = {
            "name": 999999,
        }
        try:
            base_data = self.data["name"]
        except Exception as e:
            # TODO log this error
            return result
        if not base_data or not isinstance(base_data, str):
            return result

        result["name"] = base_data

        return result
