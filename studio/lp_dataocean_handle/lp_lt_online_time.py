# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2017- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.G
    Date: 2017/02/10
    Change Activity:
"""


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口：联通号码在网时长查询s(unicome_mobile_online_time_s)
        输出：联通手机号在网时长
        """

        result = {"online_time": "9999"}

        try:
            online_time = self.data['content']['online_time']
            if online_time in ["[0-1]", "(1-2]", "[3-6]"]:
                online_time = "00"
            elif online_time in "[7-12]":
                online_time = "11"
            elif online_time in "[13-24)":
                online_time = "22"
            else:
                online_time = "33"
            result['online_time'] = online_time
        except Exception:
            # TODO log this error
            return result

        return result



