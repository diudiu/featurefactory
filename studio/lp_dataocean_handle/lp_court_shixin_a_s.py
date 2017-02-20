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
        法院失信被执行人
        data_identity: court_shixin_a_s
        :return:
        """
        result = {
            'is_court_shixin': BooleanTypeDefault
        }
        try:
            if self.data['result'] == '00':
                result['is_court_shixin'] = 1
            else:
                result['is_court_shixin'] = 0

        except Exception as e:
            logging.error(e.message)

        return result
