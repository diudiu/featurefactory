# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: ZL
    Date:  2017/01/18
    Change Activity:
"""


import logging

from vendor.utils.defaults import *

logger = logging.getLogger('apps.common')


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口名称：猎聘申请信息上传接口
        字段名称：
        'mobile': 手机号 str

        输出:
        特征名称:
        'mobile': 手机号 str
        """
        result = {'mobile': StringTypeDefault}
        try:
            base_data = self.data.get("mobile", '')
            if str(base_data).isdigit():
                result['mobile'] = base_data

        except Exception as e:
            logging.error(e.message)
        return result
