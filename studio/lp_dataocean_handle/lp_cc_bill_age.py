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
        'credit_card_account_age': 信用卡账龄 str

        输出:
        特征名称:
        'cc_bill_age': 贷记卡账龄 int
        """

        result = {
            "cc_bill_age": 9999,
        }
        try:
            base_data = self.data["result"]["rrx_once_all"]["credit_card_account_age"]
            base_data = int(base_data)
            if not base_data or not isinstance(base_data, int):
                return result

            result["cc_bill_age"] = base_data

            return result
        except Exception as e:
            # TODO log this error
            return result

