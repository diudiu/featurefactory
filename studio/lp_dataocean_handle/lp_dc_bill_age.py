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
        接口名称：人人信
        字段名称：'debit_card_account_age': 借记卡账龄 str

        计算逻辑: 直接从接口提取,输出类型为int

        输出:
        特征名称: 'dc_bill_age': 借记卡账龄 int
        """

        result = {
            "dc_bill_age": 9999,
        }
        try:
            base_data = self.data["result"]["rrx_once_all"]["debit_card_account_age"]
            base_data = int(base_data)
            if not base_data or not isinstance(base_data, int):
                return result

            result["dc_bill_age"] = base_data

            return result
        except Exception as e:
            # TODO log this error
            return result

