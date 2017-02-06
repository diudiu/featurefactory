# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: ZL
    Date:  2017/01/23
    Change Activity:
"""


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口名称：多项身份信息s
        字段名称：
        marital_status 婚姻状况

        输出:
        特征名称: 婚姻状况
        字段名称:
        'marital_status': 婚姻状况
        """

        result = {
            'marital_status': 999999,
        }
        try:
            base_data = self.data['content']['marital_status']
        except Exception as e:
            # TODO log this error
            return result
        if not base_data or not isinstance(base_data, str):
            return result

        result['marital_status'] = base_data

        return result