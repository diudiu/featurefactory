# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.G
    Date: 2017/01/18
    Change Activity:
"""

import numpy as np


class Handle(object):

    def __init__(self, rrx_data, liepin_data):
        self.rrx_data = rrx_data
        self.liepin_data = liepin_data

    def handle(self):
        """
        接口名称：人人网数据服务收入类标签接口
                  猎聘
        字段名称：rrx_inc_12m         近12月数据项
                  debit_card_12m_passentry_amount借记卡近12个月入账累计总金额
                  income_range        还款金额范围
                  work_exp_form       工作信息
                  months              月薪个数
                  salary              月薪

        输出：
        特征名称：income_level        年入账
        """

        result = {"income_level": 999999}

        rrx_income_level = None
        try:
            income_level_check_bef = self.rrx_data['result'][
                'rrx_inc_12m']['debit_card_12m_passentry_amount']
        except Exception:
            pass

        if income_level_check_bef is not None:
            if income_level_check_bef in ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09']:
                rrx_income_level = 0
            elif income_level_check_bef in ['10', '11', '12', '13']:
                rrx_income_level = 1
            elif income_level_check_bef in ['14', '15', '16', '17', '18']:
                rrx_income_level = 2
            elif income_level_check_bef in ['19', '20', '21', '22']:
                rrx_income_level = 3
            elif income_level_check_bef in ['23', '24', '25', '26', '27']:
                rrx_income_level = 4
            elif income_level_check_bef in [str(x) for x in range(28, 38)]:
                rrx_income_level = 5

        if rrx_income_level is not None:
            result['income_level'] = rrx_income_level
        else:
            work_exp_form = self.liepin_data.get('work_exp_form', None)

            if work_exp_form:
                # 计算最近一份工作的工作行业
                work_end_list = []
                for work_exp in work_exp_form:
                    work_end = work_exp.get('work_end', None)
                    try:
                        work_end_list.append(int(work_end))
                    except Exception:
                        pass

                months = work_exp_form[
                    np.argmax(work_end_list)].get('months', None)
                salary = work_exp_form[
                    np.argmax(work_end_list)].get('salary', None)
                if isinstance(months, (int, str)) and isinstance(salary, (int, str)):
                    lp_income_level = round(
                        int(months) * int(salary) * 0.56, 2)
                    if lp_income_level < 10000:
                        result['income_level'] = '00'
                    elif 10000 < lp_income_level <= 50000:
                        result['income_level'] = '11'
                    elif 50000 < lp_income_level <= 100000:
                        result['income_level'] = '22'
                    elif 100000 < lp_income_level <= 500000:
                        result['income_level'] = '33'
                    elif 500000 < lp_income_level <= 1000000:
                        result['income_level'] = '44'
                    elif 1000000 < lp_income_level:
                        result['income_level'] = '55'

        return result
