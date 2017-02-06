# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.G
    Date: 2017/01/18
    Change Activity:
"""
# TODO


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):
        """
        接口：移动号码在网时长查询s(yd_mobile_online_time_s)
        输出：移动手机号在网时长
        :return:
        """
        result = {"online_time": 999999999}

        try:
            online_time = self.data['content']['online_time']
        except Exception:
            # TODO log this error
            online_time = "-1"

        if online_time in ["(0,3)", "[3,6)"]:
            online_time = "00"
        elif online_time is "[6,12)":
            online_time = "11"
        elif online_time in ["[12,18)", "[18,24]"]:
            online_time = "22"
        else:
            online_time = "33"

        result['online_time'] = online_time
        return result



