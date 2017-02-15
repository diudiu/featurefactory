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

logger = logging.getLogger('apps.common')


class Handle(object):
    def __init__(self, data):
        self.data = data

    def handle(self):
        """
        天网黑名单
        data_identity: tianwang_black
        :return:
        """
        try:
            result = {
                'is_netsky_black': False
            }

            if self.data['result'] == u'00':
                result['is_netsky_black'] = True

        except Exception as e:
            logging.error(e.message)

        return result
