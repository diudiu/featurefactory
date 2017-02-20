# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.G
    Date: 2017/01/18
    Change Activity:
"""
from vendor.utils.defaults import PositiveSignedTypeDefault
import logging

logger = logging.getLogger('apps.common')


class Handle(object):
    def __init__(self, data):
        self.data = data

    def handle(self):
        ''' 接口：手机在网时长查询s(telecom_mobile_online)
            输出：电信手机号在网时长
              '''
        result = {
            "online_time": PositiveSignedTypeDefault
        }

        try:
            online_time = self.data['content']['online_time']
        except Exception:
            # TODO log this error
            online_time = "-1"

        if online_time is "[0-6)":
            online_time = "00"
        elif online_time is "[6-12)":
            online_time = "11"
        elif online_time is "[12-24)":
            online_time = "22"
        else:
            online_time = "33"

        result['online_time'] = online_time
        return result
