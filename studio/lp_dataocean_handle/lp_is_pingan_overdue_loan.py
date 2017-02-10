# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.G
    Date: 2017/01/18
    Change Activity:
"""


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口：反欺诈服务接口——3借贷信息——3.1逾期信息
        输出：是否命中凭安逾期名单（近24个月）
        """

        result = {"is_pingan_overdue_loan": 9999}

        if self.data['result'] == 0:
            result['is_pingan_overdue_loan'] = 1
        else:
            result['is_pingan_overdue_loan'] = 0

        return result



