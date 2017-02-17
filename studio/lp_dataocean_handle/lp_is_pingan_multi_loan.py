# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2013- DIGCREDIT, All Rights Reserved.
    -----------------------------------------------------------
    Author: Z.L
    Date:  2017/01/22
    Change Activity:
"""


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        输入:
        接口名称：贷款信息
        字段名称：'result': int

        计算逻辑: 直接从接口提取result值,值为'2'为未命中,否则为命中,输出为int

        输出:
        特征名称:
        'is_pingan_multi_loan': 是否命中多头借贷名单 int
        """

        result = {
            'is_pingan_multi_loan': 9999,
        }
        try:
            base_data = self.data["result"]
            if base_data == "2":
                result['is_pingan_multi_loan'] = 0
            else:
                result['is_pingan_multi_loan'] = 1
            return result
        except Exception as e:
            # TODO log this error
            return result

