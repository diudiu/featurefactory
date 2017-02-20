# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.Junpeng
    Date:  2017/01/20
    Change Activity:
"""
from vendor.utils.defaults import BooleanTypeDefault
import logging
logger = logging.getLogger('apps.common')


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):
        """
        天网多头借贷
        data_identity: tianwang_multi_loan
        :return:
        """
        result = {
                'is_netsky_multi_loan': BooleanTypeDefault
            }
        try:
            if self.data['result'] == u'00':
                result['is_netsky_multi_loan'] = 1
            else:
                result['is_netsky_multi_loan'] = 0
        except Exception as e:
            logging.error(e.message)
        return result
