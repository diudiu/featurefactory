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
        接口名称：多项身份信息s  multi_id_card_info_s
        字段名称：
        nation 民族
        marital_status 婚姻状况

        输出:
        特征名称:
        'folk': 民族
        'marital_status': 婚姻状况
        """

        result = {
            'folk': 999999,
            'is_hanzu':999999,
            'marital_status': 999999,
        }
        try:
            base_data_folk = self.data['content']['nation']
            base_data_marital = self.data['content']['marital_status']
        except Exception as e:
            # TODO log this error
            return result
        if not base_data_folk or not isinstance(base_data_folk, str):
            return result
        if not base_data_marital or not isinstance(base_data_marital, str):
            return result
        result['folk'] = base_data_folk
        if result['folk'] == '1':   # 1为汉族；
            result['is_hanzu'] = 1
        else:
            result['is_hanzu'] = 0
        result['marital_status'] = base_data_marital

        return result