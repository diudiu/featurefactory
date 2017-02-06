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
        接口名称：联通用户金融画像s   unicom_finance_portrait_s
                  猎聘
        字段名称：last12              最近十二个月的帐动情况
                  charge_off_range    消费金额范围
                  income_range        还款金额范围

        输出：
        特征名称：income_expense_comparison  入账与支出关系
        """

        result = {"income_expense_comparison": 999999}

        income_level = None
        expense_level = None

        try:
            income_level = self.data['content']['last12']['debit']['income_range']
            expense_level = self.data['content']['last12']['debit']['charge_off_range']
        except Exception:
            pass

        amount_list = [str(x) for x in range(0, 10)]
        amount_list = amount_list + ['a', 'b', 'c', 'd', 'e', 'f']
        amount_list = amount_list + [str(x) for x in range(10, 20)]
        amount_list = amount_list + ['1a', '1b', '1c', '1d', '1e', '1f']
        amount_list = amount_list + [str(x) for x in range(20, 26)]
        if income_level is not None and expense_level is not None:
            income_level_index = amount_list.index(income_level)
            expense_level_index = amount_list.index(expense_level)
            ratio = income_level_index/expense_level_index
            if ratio >= 10:
                result['income_expense_comparison'] = 1
            elif 1 < ratio < 10:
                result['income_expense_comparison'] = 2
            elif ratio == 1:
                result['income_expense_comparison'] = 3
            elif 0.1 < ratio < 1:
                result['income_expense_comparison'] = 4
            else:
                result['income_expense_comparison'] = 5

        return result
