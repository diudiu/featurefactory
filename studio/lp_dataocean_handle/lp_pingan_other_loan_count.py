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
        接口：反欺诈服务接口——3借贷信息——3.4其他机构查询情况
        输出：其他信贷机构数量（近6个月）
        """

        result = {"pingan_overdue_corp_count": 9999}

        try:
            data_list = self.data.keys().reverse()
            orgNums_list = []
            for a in range(6):
                orgNums_list.append(self.data.get(data_list[a]).get('orgNums'))
            pingan_ovredue_corp_count = sum(orgNums_list)

            result['pingan_overdue_corp_count'] = pingan_ovredue_corp_count
        except Exception:
            return result

        return result



