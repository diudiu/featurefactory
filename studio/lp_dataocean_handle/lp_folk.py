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
        接口名称：多项身份信息s
        字段名称：
        folk 民族

        输出:
        特征名称: 民族
        字段名称:
        'nation': 民族
        """

        result = {
            'folk': 999999,
        }
        try:
            base_data = self.data['content']['nation']
        except Exception as e:
            # TODO log this error
            return result
        if not base_data or not isinstance(base_data, str):
            return result
        result['folk'] = base_data
        if result['folk'] == '1':   # 1为汉族；
            result['folk'] = 1
        else:
            result['folk'] = 0

        return result