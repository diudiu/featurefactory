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
        接口：手机号码归属地查询(mobile_locale)
        输出：手机号码归属地
        """

        result = {"mobile_area": "9999"}

        try:
            mobile_area = self.data['content']['mobile_area']
            result['mobile_area'] = mobile_area
        except Exception:
            # TODO log this error
            return result

        return result



