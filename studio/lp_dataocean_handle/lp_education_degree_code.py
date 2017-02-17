# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: Z.L
    Date:  2017/02/10
    Change Activity:
"""


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        输入:
        接口名称：猎聘预授信接口
        字段名称：edu_exp_form     教育信息
                  degree          学历code

        计算逻辑: 提取猎聘学历信息并标准化为编码, 编码需要与学信网编码一致, 输出类型为int

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

            degree_code = {
                '5': '1',
                '10': '1',
                '20': '2',
                '30': '2',
                '40': '3',
                '50': '4',
                '60': '5',
                '70': '5',
                '80': '5',
                '90': '5',
                '999': '5',
            }
            # 匹配学历编码
            for degree_data in degree_code:
                if degree_data in degree_list:
                    result['education_degree_code'] = degree_code['degree_data']
            # 无匹配结果返回其他
            if result['education_degree_code'] == 9999:
                result['education_degree_code'] = '5'
        except Exception:
            # TODO log this error
            return result

        return result
