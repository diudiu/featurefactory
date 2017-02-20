# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.G
    Date: 2017/01/18
    Change Activity:
"""
from vendor.utils.defaults import StringTypeDefault
import logging

logger = logging.getLogger('apps.common')


class Handle(object):
    def __init__(self, data):
        self.data = data

    def handle(self):
        """
        接口：手机号码归属地查询(mobile_locale)
        输出：手机号码归属地
        :return:
        """
        result = {
                "mobile_area": StringTypeDefault,
            }
        try:
            if self.data['result'] == u'00':
                mobile_area = self.data['content']['mobile_area']
                if mobile_area != "":
                    result = mobile_area
        except Exception as e:
            logging.error(e.message)
        return result
