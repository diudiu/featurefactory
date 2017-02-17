# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2013- DIGCREDIT, All Rights Reserved.
    -----------------------------------------------------------
    Author: Z.L
    Date:  2017/01/18
    Change Activity:
"""

import logging

logger = logging.getLogger('apps.common')


class Handle(object):
    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        输入:
        接口名称：猎聘申请信息上传接口
        字段名称：'application_on' 贷款申请时间 str

        计算逻辑: 直接从接口提取申请时间

        输出:
        特征名称:
        'application_on': 申请提交时间 str
        """

        try:
            result = {
                'application_on': '9999',
            }
            apply_data = self.data["application_on"]  # 提取申请时间字段

            if not apply_data:
                raise Exception(message='get (label) fail')
            if not isinstance(apply_data, basestring):
                raise Exception(message='get (label) data format error')
            result['application_on'] = apply_data
        except Exception as e:
                logging.error(e.message)

        return result
