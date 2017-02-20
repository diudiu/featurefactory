# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.G
    Date: 2017/01/18
    Change Activity:
"""
import logging
logger = logging.getLogger('apps.common')


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):
        """
        接口：联通号码在网时长查询s(unicome_mobile_online_time_s)
        输出：联通手机号在网时长
        """
        try:
            result = {"online_time": '9999'}
            online_time = self.data['content']['online_time']

            if self.data['result'] == u'00':
                if online_time in ["[0-1]", "(1-2]", "[3-6]"]:
                    online_time = "(0,6)"
                elif online_time in "[7-12]":
                    online_time = "[6,12)"
                elif online_time in "[13-24)":
                    online_time = "[12,24)"
                elif online_time in "[25-36),[37,+)":
                    online_time = "[24,+)"
                else:
                    online_time = "-1"
                result['online_time'] = online_time

        except Exception as e:
            logging.error(e.message)

        return result




