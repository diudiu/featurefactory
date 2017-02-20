# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2013- DIGCREDIT, All Rights Reserved.
    -----------------------------------------------------------
    Author: Z.L
    Date:  2017/02/20
    Change Activity:
"""

from vendor.utils.defaults import *

import logging

logger = logging.getLogger('apps.common')


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口名称：猎聘申请信息上传接口
        字段名称：
        'mobile': 手机号 str

        计算逻辑: 从猎聘信息上传接口提取用户手机号并输出,输出类型为string

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
