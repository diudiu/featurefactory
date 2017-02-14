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
                if not isinstance(degree, (str, int)):
                    return edu_exp_form
                else:
                    degree_list.append(int(degree))
            result['education_degree_code'] = str(min(degree_list))
        except Exception:
            # TODO log this error
            return result

        return result
