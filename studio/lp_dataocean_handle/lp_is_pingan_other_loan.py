# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.G
    Date: 2017/01/18
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
        输出：是否命中凭安其他机构借贷名单（近12个月）
        """
        result = {"is_pingan_other_loan": BooleanTypeDefault}
        try:
            if self.data['result'] == 0:
                result['is_pingan_other_loan'] = 1
            else:
                result['is_pingan_other_loan'] = 0
        except Exception as e:
            logging.error(e.message)

        return result



