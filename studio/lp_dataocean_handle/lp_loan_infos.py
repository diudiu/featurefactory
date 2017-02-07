# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: Sun Fei
    Date:  2017/1/20
    Change Activity:
"""


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):
        """
        接口名称：91征信接口
        字段名称：loan_infos          申请人借贷信息

        输出：
        特征名称：loan_infos          申请人借贷信息
        """

        loan_infos_dic = {'loan_infos': None}

        loan_infos = self.data.get('loanInfos', None)

        if isinstance(loan_infos, list):
            loan_infos_dic['loan_infos'] = loan_infos
        else:
            return loan_infos_dic

        return loan_infos_dic
