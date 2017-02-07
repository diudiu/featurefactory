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
        接口名称：人人信
        字段名称：
        'credit_cards_num': 信用卡张数 str

        输出:
        特征名称:
        'creditcard_count': 信用卡张数 str
        """

        result = {
            "creditcard_count": 999999,
        }
        try:
            base_data = self.data["result"]["rrx_once_all"]["credit_cards_num"]
        except Exception as e:
            # TODO log this error
            return result
        if not base_data or not isinstance(base_data, str):
            return result

        result["creditcard_count"] = base_data

        return result
