# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: Z.L
    Date:  2017/02/10
    Change Activity:
"""
import logging

logger = logging.getLogger('apps.common')


class Handle(object):
    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        输入:
        接口名称：数据堂学历信息查询接口
        字段名称：degree   学历 str

        计算逻辑:将学历标准化为编码,输出为int

        输出：
        特征名称：degree_code   学信网学历 int
        """

        result = {'education_degree_check': '9999'}

        try:
            degree = self.data['content'].get('degree', None)
            if degree:
                education_degree = degree.get('degree', None)
                degree_code = {
                    '博士': '1',
                    '硕士': '2',
                    '本科': '3',
                    '专科': '4',
                    '其他': '5',
                }
                # 匹配学历信息与编码
                for degree_data in degree_code:
                    if degree_data in education_degree:
                        result['education_degree_check'] = degree_code['degree_data']
                # 若无匹配结果,输出其他
                if result['education_degree_check'] == 9999:
                    result['education_degree_check'] = '5'

        except Exception:
            # TODO log this error
            return result
