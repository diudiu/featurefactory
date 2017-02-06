# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: LJY
    Date:  2017/01/18
    Change Activity:
"""


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):
        """
        接口名称：猎聘金融
        字段名称：result_dict          返回结果

        输出:
        特征名称:  is_pingan_financial_shixin
        字段名称:
        'is_pingan_financial_shixin' 是否命中金融失信名单
        """


        result_dict = {
            'is_pingan_financial_shixin': 999999,
        }
        try:
            base_data_dict = self.data['data']
        except Exception as e:
            # TODO log this error
            return result_dict
        if not base_data_dict or not isinstance(base_data_dict, list):
            return result_dict

        if base_data_dict== '00':
            result_dict['is_pingan_financial_shixin'] = 0
        else:
            result_dict['is_pingan_financial_shixin'] = 1

        return result_dict