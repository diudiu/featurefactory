# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: S.G
    Date:  2017/02/10
    Change Activity:
"""


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口名称：数据堂学历信息查询接口
        字段名称：degree                     学历code
        输出：
        特征名称：degree_code                学历
        """

        result = {'education_degree_check': 9999}

        try:
            degree = self.data['data']['result'].get('degree', None)
            if degree:
                education_degree = degree.get('degree', None)
                if '博士后' in education_degree:
                    result['education_degree_check'] = '5'
                elif '博士' in education_degree:
                    result['education_degree_check'] = '10'
                elif 'MBA/EMBA' in education_degree:
                    result['education_degree_check'] = '20'
                elif '硕士' in education_degree:
                    result['education_degree_check'] = '30'
                elif '本科' in education_degree:
                    result['education_degree_check'] = '40'
                elif '大专' in education_degree:
                    result['education_degree_check'] = '50'
                elif '中专' in education_degree:
                    result['education_degree_check'] = '60'
                elif '中技' in education_degree:
                    result['education_degree_check'] = '70'
                elif '高中' in education_degree:
                    result['education_degree_check'] = '80'
                elif '初中' in education_degree:
                    result['education_degree_check'] = '90'
                else:
                    result['education_degree_check'] = '999'
        except Exception:
            # TODO log this error
            return result

        return result
