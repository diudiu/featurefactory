# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: ZL
    Date:  2017/01/20
    Change Activity:
"""
import logging

from vendor.utils.defaults import *

logger = logging.getLogger('apps.common')


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
        result = {'pingan_multi_loan_count': PositiveSignedTypeDefault}
        try:

            if self.data.get('result', None) == 0:
                org_count = 0
                records = self.data["data"]["record"]
                for record in records:
                    base_data = record.get("classification", [])
                    for data in base_data:
                        for in_data in data:
                            try:
                                other_org = int(data[in_data]["other"]["orgNums"])
                            except:
                                other_org = 0
                            try:
                                bank_org = int(data[in_data]["bank"]["orgNums"])
                            except:
                                bank_org = 0
                            org_count = org_count + other_org + bank_org

                result['pingan_multi_loan_count'] = org_count

        except Exception as e:
            logging.error(e.message)

        return result




