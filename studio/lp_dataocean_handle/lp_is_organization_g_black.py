# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.Junpeng
    Date:  2017/01/20
    Change Activity:
    data = data = {
    "result": "00",
    "result_message": "检测通过或查询有记录",
    "content": [{
        "type": "欺诈",
        "date": "",
        "desc": "",
        "originalRet": {
            "name": "100",
            "pid": "100",
            "mobile": "0",
            "confirm_type": "欺诈",
            "confirm_details": "",
            "confirmed_at": "2014年02月01日",
            "loan_type": "",
            "applied_at": ""
        }
    }]
}
"""
import logging

from vendor.utils.defaults import *

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
        result = {
            'is_organization_g_black': BooleanTypeDefault
        }
        try:

            if self.data['result'] == u'00':
                result['is_organization_g_black'] = 1
            else:
                result['is_organization_g_black'] = 0
        except Exception as e:
            logging.error(e.message)

        return result
