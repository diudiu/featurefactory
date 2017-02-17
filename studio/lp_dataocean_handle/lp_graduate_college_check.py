# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: Z.L
    Date:  2017/02/15
    Change Activity:
"""


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        输入:
        接口名称：education_review_s 数据堂学历信息查询接口
        字段名称：college 院校名称 string

        计算逻辑: 直接从接口提取,输出为string

        输出：
        特征名称：graduate_college_check 学信网查得院校 string
        """

        result = {'graduate_college_check': '9999'}

        try:
            college_name = self.data['content']['degree'].get('college', None)
            if not college_name or not isinstance(college_name, basestring):
                return result
            result['graduate_college_check'] = college_name
            return result
        except Exception:
            # TODO log this error
            return result
