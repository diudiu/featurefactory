# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: Sun Fei
    Date:  2017/1/18
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

        last_work_city_dic = {'last_work_city': 9999}  # 9999：异常

        try:
            work_exp_form = self.data['work_exp_form']
        except Exception:
            # TODO log this error
            return last_work_city_dic

        if not isinstance(work_exp_form, list):
            return last_work_city_dic

        # TODO 计算维度
        last_work_city_dic[
            'last_work_city'] = work_exp_form[-1].get('dq_name', None)

        return last_work_city_dic
