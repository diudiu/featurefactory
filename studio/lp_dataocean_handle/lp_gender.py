# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: LJY
    Date:  2017/01/23
    Change Activity:
"""


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口名称：个人基本信息查询
        字段名称：
        gender 性别

        输出:
        特征名称: 性别
        字段名称:
        'gender': 性别
        """

        result = {
            'gender': 999999,
        }
        try:
            base_data = self.data['content']['sex']
        except Exception as e:
            # TODO log this error
            return result
        if not base_data or not isinstance(base_data, str):
            return result

        result['gender'] = base_data

        return result