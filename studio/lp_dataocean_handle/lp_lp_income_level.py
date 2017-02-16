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
import logging
logger = logging.getLogger('apps.common')

class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):
        """
        接口名称：猎聘
        字段名称：work_exp_form       工作信息
                  months              月薪个数
                  salary              月薪

        输出：
        特征名称：income_level        年入账
        """
        try:
            result = {'income_level': 9999}  # 999999：异常
            work_exp_form = self.data.get('work_exp_form', None)
            work_end_list = []
            for work_exp in work_exp_form:
                work_end = work_exp.get('work_end', None)
                work_end_list.append(int(work_end))
                months = work_exp_form[np.argmax(work_end_list)].get('months', None)
                salary = work_exp_form[np.argmax(work_end_list)].get('salary', None)
                if int(months) and int(salary):
                    lp_income_level = round(int(months) * int(salary) * 0.56, 2)
                    if lp_income_level < 10000:
                        result['income_level'] = 0
                    elif 10000 < lp_income_level <= 50000:
                        result['income_level'] = 1
                    elif 50000 < lp_income_level <= 100000:
                        result['income_level'] = 2
                    elif 100000 < lp_income_level <= 500000:
                        result['income_level'] = 3
                    elif 500000 < lp_income_level <= 1000000:
                        result['income_level'] = 4
                    elif 1000000 < lp_income_level:
                        result['income_level'] = 5

        except Exception as e:
                logging.error(e.message)
        return result
