# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: Sun Fei
    Date:  2017/1/19
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

        industry_change_count_dic = {'industry_change_count': 9999}  # 9999：异常

        try:
            work_exp_form = self.data['work_exp_form']
        except Exception:
            # TODO log this error
            return industry_change_count_dic

        if not isinstance(work_exp_form, list):
            return industry_change_count_dic

        # TODO 计算维度
        # 计算所有工作行业表
        industry_list = []
        for work_exp in work_exp_form:
            industry = work_exp.get('industry', None)
            if not isinstance(industry, (str, int)):
                return industry_change_count_dic
            else:
                industry_list.append(int(industry))

        industry_list_duplicated = list(set(industry_list))

        if len(industry_list_duplicated) >= 1:
            industry_change_count = len(industry_list_duplicated) - 1
        else:
            industry_change_count = None

        industry_change_count_dic[
            'industry_change_count'] = industry_change_count

        return industry_change_count_dic
