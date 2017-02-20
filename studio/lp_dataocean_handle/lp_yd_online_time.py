# -*- coding:utf-8 -*-
from vendor.utils.defaults import StringTypeDefault
import logging
logger = logging.getLogger('apps.common')
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
        接口：移动号码在网时长查询s(yd_mobile_online_time_s)
        输出：移动手机号在网时长
        """
<<<<<<< HEAD
        result = {"online_time": StringTypeDefault}
=======

        result = {"online_time": "9999"}

>>>>>>> 93eae5a35dfbc9189db8c57ec4bcfb3d4da864cd
        try:
            online_time = self.data['content']['online_time']
            if online_time in ["(0,3)", "[3,6)"]:
                online_time = "00"
            elif online_time in "[6,12)":
                online_time = "11"
            elif online_time in ["[12,18)", "[18,24]"]:
                online_time = "22"
            else:
                online_time = "33"
            result['online_time'] = online_time
        except Exception as e:
            logging.error(e.message)
        return result



