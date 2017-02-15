# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: ZL
    Date:  2017/02/15
    Change Activity:
"""


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口名称：education_review_s 数据堂学历信息查询接口
        字段名称：education_approach 学习形式
        输出：
        特征名称：is_recruitment 是否统招
        """

        result = {'is_recruitment': 9999}

        try:
            education_info = self.data['content']['degree'].get('education_approach', None)
            if not education_info or not isinstance(education_info, basestring):
                return result
            if '全日制' in education_info:
                result['is_recruitment'] = 1
            else:
                result['is_recruitment'] = 0
            return result
        except Exception:
            # TODO log this error
            return result
