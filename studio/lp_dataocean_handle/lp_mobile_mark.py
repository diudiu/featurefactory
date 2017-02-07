# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: ZL
    Date:  2017/01/20
    Change Activity:
"""


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口名称：
        'tags': 电话标记
        字段名称：
        'label': 用户标注标签 str

        输出:
        特征名称:
        'mobile_mark': 用户标注标签 str
        """

        result = {
            'mobile_mark': 999999,
        }
        try:
            base_data = self.data["tags"]["contactMain_IMSI1_IMEI1"]["label"]
        except Exception as e:
            # TODO log this error
            return result
        if not base_data or not isinstance(base_data, str):
            return result

        result['mobile_mark'] = base_data

        return result
