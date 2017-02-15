# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: ZL
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
                'repayState': 7,
                'arrearsAmount': 0,
                'companyCode': 'P2P4HJK0000100010'
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
from datetime import datetime
import time
import logging

logger = logging.getLogger('apps.common')


class Handle(object):
    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口名称：91征信查询
        字段名称：
        borrowState 借款状态
        contractDate 借款年月

        输出:
        特征名称: 拒贷次数
        字段名称:
        'jiuyao_multi_loan_denied_count': 拒贷次数
        """
        try:
            result = {
                'jiuyao_multi_loan_denied_count': 9999,
            }
            count = 0
            base_data = self.data['loanInfos']
            assert type(base_data) == list
            for data in base_data:
                base_time = data.get('contractDate', '')
                if not str(base_time).isdigit():
                    continue
                times = int(time.time()) - (base_time / 1000)
                if times <= 180 * 3600:
                    count += 1
            result['jiuyao_multi_loan_denied_count'] = count

        except Exception as e:
            logging.info(e.message)

        return result

