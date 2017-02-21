# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2013- DIGCREDIT, All Rights Reserved.
    -----------------------------------------------------------
    Author: Z.L
    Date:  2017/02/17
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
        输入:
        接口名称：'personal_info': 个人基本信息查询
        字段名称：'age': 年龄 int

        计算逻辑: 直接从个人基本信息查询接口提取'年龄'字段并输出, 输出类型为int

        输出:
        特征名称: 'age': 年龄 int
        """

        result = {'age': PositiveSignedTypeDefault}
        try:
            base_data_age = self.data["content"]["age"]    # 提取年龄字段
            if str(base_data_age).isdigit() and 0 <= int(base_data_age) <= 100:  # 判断年龄是否是int且在0-100之间
                result['age'] = int(base_data_age)

        except Exception as e:
                logging.error(e.message)

        return result
