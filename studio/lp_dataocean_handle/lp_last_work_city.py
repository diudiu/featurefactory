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
        接口名称：猎聘
        字段名称：dq_name             地点名称

        输出：
        特征名称：dq_name             地点名称
        """

        result = {'last_work_city': '9999'}

        try:
            work_exp_form = self.data['work_exp_form']
            if not isinstance(work_exp_form, list):
                return last_work_city_dic
            result['last_work_city'] = work_exp_form[-1].get('dq_name', None)
        except Exception:
            # TODO log this error
            return result

        return result
