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
import numpy as np

logger = logging.getLogger('apps.common')


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

        result = {'graduate_college': '9999'}

        try:
            edu_exp_form = self.data['edu_exp_form']
            if edu_exp_form:
                end_list = []
                for edu_exp in edu_exp_form:
                    end = edu_exp.get('end', None)
                    end_list.append(int(end))
                result['graduate_college'] = edu_exp_form[
                    np.argmax(end_list)].get('school')
        except Exception:
            logging.error(e.message)
            return result

        return result
