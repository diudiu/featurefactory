# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2017- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.G
    Date: 2017/02/17
    Change Activity:
"""

import logging
logger = logging.getLogger('apps.common')
from vendor.utils.defaults import PositiveSignedTypeDefault

class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口：猎聘预授信接口

        字段：edu_exp_form   教育信息
              degree         学历code值

        计算逻辑：遍历edu_exp_form的所有元素，将元素的degree组成一个degree_list，遍历code_list中的code（按学位从高到低遍历），
                  如果某code在degree_list中，则确定为其最高学历的code并跳出循环

        输出:简历最高学历
        """

        result = {"highest_degree": PositiveSignedTypeDefault}
        code_list = ["5", "10", "20", "30", "40", "50", "60", "70", "80", "90"]  # 按学位从高到低排列
        degree_list = []

        try:
            edu_exp_form = self.data['edu_exp_form']

            for a in range(len(edu_exp_form)):     # 遍历edu_exp_form的所有元素，将元素的degree组成一个degree_list
                degree_list.append(edu_exp_form[a].get('degree'))
            for code in code_list:  # 遍历code_list中的code（按学位从高到低遍历）
                if code in degree_list:  # 如果某code在degree_list中，则确定为其最高学历的code并跳出循环
                    result['highest_degree'] = code
                    break
        except Exception as e:
            logging.error(e.message)
        finally:
            return result




