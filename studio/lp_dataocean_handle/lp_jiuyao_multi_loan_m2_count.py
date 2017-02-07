# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: LJY
    Date:  2017/01/18
    Change Activity:
"""


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
            'jiuyao_multi_loan_m2_count': 999999,
        }
        try:
            base_data = self.data['loanInfos']
        except Exception as e:
            # TODO log this error
            return result
        if not base_data or not isinstance(base_data, list):
            return result

        repayState_list = [data.get('repayState', None) for data in base_data]

        repayState_out_list=[]
        for repayState in repayState_list:

            if  repayState>= 3 and repayState<=8:
                repayState_out_list.append(repayState)
        result['jiuyao_multi_loan_m2_count']=len(repayState_out_list)

        return result

