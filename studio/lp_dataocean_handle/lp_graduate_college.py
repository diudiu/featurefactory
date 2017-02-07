# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: Sun Fei
    Date:  2017/1/18
    Change Activity:
"""

import numpy as np


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):
        """
        接口名称：猎聘
        字段名称：edu_exp_form               教育信息
                  school                     毕业院校

        输出：
        特征名称：graduate_college           院校
        """

        result = {'graduate_college': 999999}  # 999999：异常

        try:
            edu_exp_form = self.data['edu_exp_form']
        except Exception:
            # TODO log this error
            pass

        # TODO 计算维度
        if edu_exp_form:
            end_list = []
            for edu_exp in edu_exp_form:
                end = edu_exp.get('end', None)
                try:
                    end_list.append(int(end))
                except Exception:
                    pass

        result['graduate_college'] = edu_exp_form[
            np.argmax(end_list)].get('school')

        return result
