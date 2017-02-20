# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: LJY
    Date:  2017/01/18
    Change Activity:
    data={
        'loanInfos':[
            {
                'borrowType': 1,
                'borrowState': 2,
                'borrowAmount': 3,
                'contractDate': 1343779200000,
                'loanPeriod': 24,
                'repayState': '',
                'arrearsAmount': 0,
                'companyCode': 'P2P4HJK0000100010'
            },
            {
                'borrowType': 1,
                'borrowState': 1,
                'borrowAmount': 3,
                'contractDate': 1343779200000,
                'loanPeriod': 24,
                'repayState': 2,
                'arrearsAmount': 0,
                'companyCode': 'P2P4HJK0000100011'
            },
            {
                'borrowType': 1,
                'borrowState': 1,
                'borrowAmount': 3,
                'contractDate': 1343779200000,
                'loanPeriod': 24,
                'repayState': 7,
                'arrearsAmount': 0,
                'companyCode': 'P2P4HJK0000100011'
            }
        ]
    }
"""
import logging

from vendor.utils.defaults import *

logger = logging.getLogger('apps.common')


class Handle(object):
    def __init__(self, data):
        self.data = data

    def handle(self):
        """
        接口名称：猎聘金融
        字段名称：
        repayState  当前状态

        输出:
        特征名称:  repayState
        字段名称:
        'jiuyao_multi_loan_m2_count'   M2及M2以上次数
        """
        result = {
            'jiuyao_multi_loan_m2_count': PositiveSignedTypeDefault,
        }
        try:
            count = 0
            base_data = self.data['loanInfos']
            if type(base_data) == list:
                for data in base_data:
                    times = data.get('repayState', 0)
                    if 3 <= times <= 8:
                        count += 1
            result['jiuyao_multi_loan_m2_count'] = count
        except Exception as e:
            logging.error(e.message)
        return result


