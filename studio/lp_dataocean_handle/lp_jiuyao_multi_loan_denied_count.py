# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: ZL
    Date:  2017/01/18
    Change Activity:
"""
from datetime import datetime
import time


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

        result = {
            'jiuyao_multi_loan_denied_count': 999999,
        }
        try:
            base_data = self.data['loanInfos']

        except Exception as e:
            # TODO log this error
            return result
        if not base_data or not isinstance(base_data, list):
            return result

        base_time_list = [data.get('contractDate', 1) for data in base_data]
        register_duration_list=[]
        index_list=[]
        index = 0
        for base_time in base_time_list:

            time_now = datetime.now()
            value = time.localtime(base_time / 1000)
            base_time = time.strftime('%Y-%m-%d %H:%M:%S', value)
            base_time = datetime.strptime(base_time, '%Y-%m-%d %H:%M:%S')
            register_duration = (time_now - base_time).days
            register_duration_list.append(register_duration)

        for register_duration in register_duration_list:
            if register_duration <= 180:
                index_list.append(index)
            index += 1

        denied_loan_list = []
        for index in index_list:
            denied_loan_list.append(base_data[index].get('borrowState', None))

        result['jiuyao_multi_loan_denied_count'] = denied_loan_list.count(1)
        return result
