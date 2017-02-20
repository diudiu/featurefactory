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
from datetime import datetime

from vendor.utils.defaults import *

logger = logging.getLogger('apps.common')


class Handle(object):
    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口名称：
        猎聘申请信息上传接口
        猎聘预授信接口
        字段名称：
        'registration_on': 用户注册时间 str
        'application_on': 贷款申请时间 str

        输出:
        特征名称:
        'apply_register_duration': 注册时间长度 float
        """
        result = {
            'apply_register_duration': UnsignedFloatTypeDefault,
        }
        try:
            apply_data = self.data["apply_data"]["application_on"][:10]
            register_data = self.data["portrait_data"]["registration_on"][:10]
            apply_data = datetime.strptime(apply_data, "%Y-%m-%d")
            register_data = datetime.strptime(register_data, "%Y-%m-%d")
            apply_register = (apply_data - register_data).days / 30.0
            if apply_register >= 0:
                result['apply_register_duration'] = apply_register

        except Exception as e:
            logging.error(e.message)

        return result
