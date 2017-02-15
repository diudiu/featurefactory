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
        字段名称：degree                     学历
        输出：
        特征名称：degree_code                学历code
        """

        result = {'education_degree_check': 9999}

        try:
            degree = self.data['content'].get('degree', None)
            if degree:
                education_degree = degree.get('degree', None)
                if '博士' in education_degree:
                    result['education_degree_check'] = '1'
                elif '硕士' in education_degree:
                    result['education_degree_check'] = '2'
                elif '本科' in education_degree:
                    result['education_degree_check'] = '3'
                elif '专科' in education_degree:
                    result['education_degree_check'] = '4'
                else:
                    result['education_degree_check'] = '5'
        except Exception:
            # TODO log this error
            return result

        return result
