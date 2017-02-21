# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.Junpeng
    Date:  2017/01/20
    Change Activity:
"""
import logging
from vendor.utils.defaults import BooleanTypeDefault

logger = logging.getLogger('apps.common')


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):
        """
        贷款中介
        data_identity: loan_agency
        :return:
        """
        result = {
            'is_loan_agency': BooleanTypeDefault
        }
        try:
            if self.data['result'] == u'00':
                result['is_loan_agency'] = 1
            else:
                result['is_loan_agency'] = 0
        except Exception as e:
            logger.error(e.message)
        return result
