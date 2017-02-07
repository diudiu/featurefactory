# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: Sun Fei
    Date:  2017/1/18
    Change Activity:
"""


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):
        """
        接口名称：猎聘
        字段名称：edu_exp_form               教育信息
                  degree                     学历code

        输出：
        特征名称：education_degree_code      学历
        """

        education_degree_code_dic = {'education_degree_code': 9999}  # 9999：异常

        try:
            edu_exp_form = self.data['edu_exp_form']
        except Exception:
            # TODO log this error
            return education_degree_code_dic

        if not isinstance(edu_exp_form, list):
            return education_degree_code_dic

        # TODO 计算维度
        degree_list = []
        for edu_exp in edu_exp_form:
            degree = edu_exp.get('degree', None)
            if not isinstance(degree, (str, int)):
                return edu_exp_form
            else:
                degree_list.append(int(degree))

        education_degree_code_dic[
            'education_degree_code'] = str(min(degree_list))

        return education_degree_code_dic
