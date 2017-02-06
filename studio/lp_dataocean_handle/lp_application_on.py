# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: ZL
    Date:  2017/01/18
    Change Activity:
"""
from datetime import datetime
import time


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口名称：
        猎聘申请信息上传接口
        字段名称：
        'application_on': 贷款申请时间 str

        输出:
        特征名称:
        'application_on': 申请提交时间 str
        """

        result = {
            'application_on': 999999,
        }
        try:
            apply_data = self.data["application_on"]
        except Exception as e:
            # TODO log this error
            return result
        if not apply_data or not isinstance(apply_data, str):
            return result

        result['application_on'] = apply_data

        return result
