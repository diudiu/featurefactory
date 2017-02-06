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
        接口名称：人人网数据服务收入类标签接口
                  猎聘
        字段名称：rrx_inc_12m         近12月数据项
                  debit_card_12m_passentry_amount借记卡近12个月入账累计总金额
                  debit_card_12m_chargeoff_amount借记卡近12个月出账累计总金额

        输出：
        特征名称：income_expense_comparison  入账与支出关系
        """

        result = {"income_expense_comparison": 999999999}

        income_level = None
        expense_level = None

        try:
            income_level = self.data['result'][
                'rrx_inc_12m']['debit_card_12m_passentry_amount']
            expense_level = self.data['result'][
                'rrx_inc_12m']['debit_card_12m_chargeoff_amount']
        except Exception:
            pass

        amount_list = ['0' + str(x) for x in range(0, 10)]
        amount_list = amount_list + [str(x) for x in range(10, 40)]
        if income_level is not None and expense_level is not None:
            income_level_index = amount_list.index(income_level)
            expense_level_index = amount_list.index(expense_level)
            ratio = income_level_index/expense_level_index
            if ratio >= 10:  #入账远大于支出
                result['income_expense_comparison'] = 1
            elif 1 < ratio < 10:  #入账大于支出
                result['income_expense_comparison'] = 2
            elif ratio == 1:  #入账接进出账
                result['income_expense_comparison'] = 3
            elif 0.1 < ratio < 1:  #入账小于出账
                result['income_expense_comparison'] = 4
            elif ratio <= 0.1:  #入账远小于支出
                result['income_expense_comparison'] = 5
        return result
