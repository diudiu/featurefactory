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
        接口：反欺诈服务接口开发指南——3.借贷信息——3.4其他机构查询情况
        输出：其他机构借贷信息
        """

        result = {'pingan_other_loan_infos': '9999'}

        try:
            dict = self.data
            for a in dict.keys():
                for b in a.keys():
                    if dict.get(a).get(b) is None:
                            del dict.get(a)[b]
            result['pingan_other_loan_infos'] = dict
        except Exception:
            return result

        return result



