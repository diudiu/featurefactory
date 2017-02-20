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

from vendor.utils.defaults import *

logger = logging.getLogger('apps.common')


class Handle(object):
    def __init__(self, data):
        self.data = data

    def handle(self):
        """
        个人不良信息
        data_identity: negative_info_s
        :return:
        """
        result = {'has_negative_info': BooleanTypeDefault}
        try:
            if self.data['result'] == u'00':
                result['has_negative_info'] = 1
            else:
                result['has_negative_info'] = 0

        except Exception as e:
            logging.error(e.message)

        return result
