# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: ZL
    Date:  2017/01/22
    Change Activity:
"""


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口名称：贷款信息
        字段名称：
        'result': int

        输出:
        特征名称:
        'is_pingan_multi_loan': 是否命中多头借贷名单 int
        """

        result = {
            'is_pingan_multi_loan': 999999,
        }
        try:
            base_data = self.data["result"]
        except Exception as e:
            # TODO log this error
            return result
        if base_data == "2":
            result['is_pingan_multi_loan'] = 0

        result['is_pingan_multi_loan'] = 1
        return result
