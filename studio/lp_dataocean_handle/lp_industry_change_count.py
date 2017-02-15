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
        字段名称：work_exp_form               工作信息
                 industry                    公司行业名称

        输出：
        特征名称：industry_change_count       换行次数
        """

        result = {'industry_change_count': 9999}

        try:
            work_exp_form = self.data['work_exp_form']
            if not isinstance(work_exp_form, list):
                return result
            industry_list = []
            for work_exp in work_exp_form:
                industry = work_exp.get('industry', None)
                if not isinstance(industry, (basestring, int)):
                    return result
                else:
                    industry_list.append(int(industry))

            industry_list_duplicated = list(set(industry_list))
            if len(industry_list_duplicated) >= 1:
                industry_change_count = len(industry_list_duplicated) - 1
            else:
                industry_change_count = None
            result['industry_change_count'] = industry_change_count
        except Exception:
            # TODO log this error
            return result

        return result
