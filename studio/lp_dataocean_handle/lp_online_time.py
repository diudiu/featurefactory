# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2017- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.G
    Date: 2017/02/10
    Change Activity:
"""
from vendor.utils.defaults import StringTypeDefault, PositiveSignedTypeDefault
import logging


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):
        if 'telecom_mobile_online_time_s' in self.data.keys():
            self.data = self.data['telecom_mobile_online_time_s']
            return self._telecom_handle()
        if 'yd_mobile_online_time_s' in self.data.keys():
            self.data = self.data['yd_mobile_online_time_s']
            return self._yd_handle()
        if 'unicome_mobile_online_time_s' in self.data.keys():
            self.data = self.data['unicome_mobile_online_time_s']
            return self._unicome_handle()

    def _yd_handle(self):
        """
        接口：移动号码在网时长查询s(yd_mobile_online_time_s)
        输出：移动手机号在网时长
        :return:
        """
        result = {"online_time": StringTypeDefault}
        try:
            if self.data['result'] == u'00':
                online_time = self.data['content']['online_time']
                if online_time in ["(0,3)", "[3,6)"]:
                    online_time = "00"
                elif online_time in "[6,12)":
                    online_time = "11"
                elif online_time in ["[12,18)", "[18,24]"]:
                    online_time = "22"
                elif online_time in ["(24,+)"]:
                    online_time = "33"
                else:
                    online_time = StringTypeDefault
                result['online_time'] = online_time
        except Exception as e:
            logging.error(e.message)
        return result

    def _unicome_handle(self):
        """
        接口：联通号码在网时长查询s(unicome_mobile_online_time_s)
        输出：联通手机号在网时长
        """
        result = {"online_time": StringTypeDefault}
        try:
            online_time = self.data['content']['online_time']

            if self.data['result'] == u'00':
                if online_time in ["[0-1]", "(1-2]", "[3-6]"]:
                    online_time = "00"
                elif online_time in "[7-12]":
                    online_time = "11"
                elif online_time in "[13-24)":
                    online_time = "22"
                elif online_time in "[25-36),[37,+)":
                    online_time = "33"
                else:
                    online_time = StringTypeDefault
                result['online_time'] = online_time

        except Exception as e:
            logging.error(e.message)
        return result

    def _telecom_handle(self):
        """
        接口：手机在网时长查询s(telecom_mobile_online)
        输出：电信手机号在网时长
        """
        result = {
            "online_time": StringTypeDefault
        }
        try:
            online_time = self.data['content']['online_time']
            if online_time in ["[0-6)"]:
                online_time = "00"
            elif online_time in ["[6-12)"]:
                online_time = "11"
            elif online_time in ["[12-24)"]:
                online_time = "22"
            elif online_time in ["[24-36)", "[36,+)"]:
                online_time = "33"
            else:
                online_time = StringTypeDefault

            result['online_time'] = online_time
        except Exception as e:
            # TODO log this error
            logging.error(e.message)
        return result
