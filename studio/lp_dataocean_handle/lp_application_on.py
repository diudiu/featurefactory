# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2013- DIGCREDIT, All Rights Reserved.
    -----------------------------------------------------------
    Author: Z.L
    Date:  2017/02/20
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
        接口名称：
        猎聘申请信息上传接口
        字段名称：
        'application_on': 贷款申请时间 str

        计算逻辑: 直接从猎聘申请信息上传接口提取贷款申请时间,输出类型为string

        输出:
        特征名称:
        'application_on': 申请提交时间 str
        """
        result = {
                'application_on': StringTypeDefault,
            }
        try:
            apply_data = self.data["application_on"]
            if apply_data and isinstance(apply_data, basestring):
                result['application_on'] = apply_data
        except Exception as e:
            logging.error(e.message)
        return result
