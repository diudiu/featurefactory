# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: ZL
    Date:  2017/01/18
    Change Activity:
"""


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口名称：
        'personal_info': 个人基本信息查询
        字段名称：
        'age': 年龄 int
        'gender': 性别 str

        输出:
        特征名称:
        'age': 年龄 int
        'gender': 性别 str
        """

        result = {
            'age': 999999,
            'gender': 999999,
        }
        try:
            base_data_age = self.data["content"]["age"]
            base_data_gender = self.data['content']['sex']
        except Exception as e:
            # TODO log this error
            return result
        if not base_data_age or not isinstance(base_data_age, int):
            return result
        if not base_data_gender or not isinstance(base_data_gender, str):
            return result

        result['age'] = base_data_age
        result['gender'] = base_data_gender

        return result
