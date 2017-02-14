# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2017- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.G
    Date: 2017/02/10
    Change Activity:
"""


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口：反欺诈服务接口开发指南——3.借贷信息——3.1逾期信息
        输出：逾期信息
        """

        result = {"pingan_overdue_loan_infos": "9999"}

        try:
            dict = self.data.get('record').get('classification')
            for a in dict.keys():
                for b in a.keys():
                    for c in b.keys():
                        if dict.get(a).get(b).get(c) is None:
                            del dict.get(a).get(b)[c]
            result['pingan_overdue_loan_infos'] = dict
        except Exception:
            return result

        return result



