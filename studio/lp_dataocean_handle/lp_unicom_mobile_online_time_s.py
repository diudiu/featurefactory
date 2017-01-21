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
        接口：联通号码在网时长查询s(unicome_mobile_online_time_s)
        输出：联通手机号在网时长
        """
        result = {"online_time": 999999999}

        try:
            online_time = self.data['content']['online_time']
        except Exception:
            # TODO log this error
            online_time = "-1"

        if online_time in ["[0-1]", "(1-2]", "[3-6]"]:
            online_time = "(0,6)"
        elif online_time is "[7-12]":
            online_time = "[6,12)"
        elif online_time is "[13-24)":
            online_time = "[12,24)"
        else:
            online_time = "[24,+)"

        result['online_time'] = online_time
        return result



