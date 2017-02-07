# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: ZL
    Date:  2017/01/20
    Change Activity:
"""


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口名称：贷款信息
        字段名称：
        'org_names': 涉及机构数 int

        输出:
        特征名称:
        'pingan_multi_loan_count': 多头借贷公司数量 int
        """

        result = {
            'pingan_multi_loan_count': 999999,
        }
        try:
            base_data = self.data["data"]["record"]["classification"]
        except Exception as e:
            # TODO log this error
            return result
        if not base_data:
            result['pingan_multi_loan_count'] = 0
            return result
        if isinstance(base_data, list):
            return result

        org_count = 0
        for data in base_data:
            for in_data in data:
                try:
                    other_org = data[in_data]["other"]["orgNums"]
                except Exception as e:
                    # TODO log this error
                    other_org = 0
                try:
                    bank_org = data[in_data]["bank"]["orgNums"]
                except Exception as e:
                    # TODO log this error
                    bank_org = 0
                org_count = org_count + other_org + bank_org

        result['pingan_multi_loan_count'] = org_count
        return result
