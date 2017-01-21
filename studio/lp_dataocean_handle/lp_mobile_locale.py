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
        接口：手机号码归属地查询(mobile_locale)
        输出：手机号码归属地
        :return:
        """
        result = {
             "mobile_area": "",
        }
        try:
            mobile_area = self.data['content']['mobile_area']
        except Exception:
            # TODO log this error
            mobile_area = "NONE"

        result['mobile_area'] = mobile_area

        return result
