# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: S.G
    Date:  2017/02/10
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
        接口名称：91征信接口
        字段名称：loan_infos              申请人借贷信息

        输出：
        特征名称：is_jiuyao_multi_loan    是否命中91多头借贷名单
        """

        result = {'is_jiuyao_multi_loan': BooleanTypeDefault}

        try:
            loan_infos = self.data['loanInfos']
            if loan_infos:
                result['is_jiuyao_multi_loan'] = 1
            else:
                result['is_jiuyao_multi_loan'] = 0
        except Exception as e:
            logging.error(e.message)

        return result
