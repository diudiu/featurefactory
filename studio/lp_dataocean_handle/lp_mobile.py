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
        'mobile': 手机号 str

        输出:
        特征名称:
        'mobile': 手机号 str
        """

        result = {
            "mobile": 999999,
        }
        try:
            base_data = self.data["mobile"]
        except Exception as e:
            # TODO log this error
            return result
        if not base_data or not isinstance(base_data, str):
            return result

        result["mobile"] = base_data

        return result
