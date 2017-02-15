# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: S,G
    Date:  2017/02/10
    Change Activity:
"""


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口名称：猎聘
        字段名称：edu_exp_form               教育信息
                  degree                    学历code

        输出：
        特征名称：education_degree_code      学历
        """

        result = {'education_degree_code': 9999}

        try:
            edu_exp_form = self.data['edu_exp_form']
            if not isinstance(edu_exp_form, list):
                return result
            degree_list = []
            for edu_exp in edu_exp_form:
                degree = edu_exp.get('degree', None)
                degree_list.append(degree)

            if "5" in degree_list:
                highest_degree = "1"
            elif "10" in degree_list:
                highest_degree = "1"
            elif "20" in degree_list:
                highest_degree = "2"
            elif "30" in degree_list:
                highest_degree = "2"
            elif "40" in degree_list:
                highest_degree = "3"
            elif "50" in degree_list:
                highest_degree = "4"
            else:
                highest_degree = "5"
            result['education_degree_code'] = highest_degree
        except Exception:
            # TODO log this error
            return result

        return result
