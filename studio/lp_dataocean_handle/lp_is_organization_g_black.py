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
        机构G黑名单
        data_identity: agentg_black
        :return:
        """
        try:
            result = {
                'is_organization_g_black': False
            }
            if self.data['result'] == '00':
                result['is_organization_g_black'] = True
        except Exception as e:
            logging.info(e.message)

        return result
