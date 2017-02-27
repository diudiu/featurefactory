# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2017- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.G
    Date: 2017/02/10
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
        接口：反欺诈服务接口——3借贷信息——3.4其他机构查询情况
        输出：其他信贷机构数量（近6个月）
        """

        result = {"pingan_other_loan_count": PositiveSignedTypeDefault}

        try:
            if self.data['result'] == 0:
                orgNums_list = []
                data = sorted(self.data['data'].items(), key=lambda x: x[0], reverse=True)
                for dates, v in data[0:6]:
                    if v and str(v.get('orgNums', None)).isdigit():
                        orgNums_list.append(int(v['orgNums']))
                pingan_ovredue_corp_count = sum(orgNums_list)

                result['pingan_other_loan_count'] = pingan_ovredue_corp_count
        except Exception as e:
            logging.error(e.message)
        return result
