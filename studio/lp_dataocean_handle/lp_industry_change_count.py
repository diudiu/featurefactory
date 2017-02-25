# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: S,G
    Date:  2017/02/10
    Change Activity:
"""
import logging

from vendor.utils.defaults import *

logger = logging.getLogger('apps.common')


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

        result = {'industry_change_count': PositiveSignedTypeDefault}

        try:
            work_exp_form = self.data['work_exp_form']

            industry_list = []
            for work_exp in work_exp_form:
                industry = work_exp.get('industry', None)
                if str(industry).isdigit():
                    industry_list.append(int(industry))

            industry_list_duplicated = set(industry_list)
            if len(industry_list_duplicated) >= 1:
                industry_change_count = len(industry_list_duplicated) - 1
                result['industry_change_count'] = industry_change_count
        except Exception as e:
            logging.error(e.message)

        return result
