# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: S.Junpeng
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
        keys = self.data.keys()
        if 'cc_credit' in keys:
            return self._cc_handle()
        elif 'unicom_finance_portrait_s' in keys:
            return self._uni_handle()

    def _uni_handle(self):
        """
        接口名称：联通用户金融画像s   unicom_finance_portrait_s
                  猎聘
        字段名称：last12              最近十二个月的帐动情况
                  charge_off_range    消费金额范围
                  income_range        还款金额范围

        输出：
        特征名称：income_expense_comparison  入账与支出关系
        """
        result = {
            "income_expense_comparison": PositiveSignedTypeDefault
        }
        ls_dic = {
            '0': 500,
            '1': 1500,
            '2': 2500,
            '3': 3500,
            '4': 4500,
            '5': 5500,
            '6': 6500,
            '7': 7500,
            '8': 8500,
            '9': 9500,
            'a': 15000,
            'b': 25000,
            'c': 35000,
            'd': 45000,
            'e': 55000,
            'f': 65000,
            '10': 75000,
            '11': 85000,
            '12': 95000,
            '13': 150000,
            '14': 250000,
            '15': 350000,
            '16': 450000,
            '17': 550000,
            '18': 650000,
            '19': 750000,
            '1a': 850000,
            '1b': 950000,
            '1c': 1500000,
            '1f': 2500000,

        }
        try:
            if self.data['result'] == u'00':
                income_level = self.data['content']['last12']['debit']['income_range']
                if income_level is not None:
                    income_level_value = ls_dic.get(income_level)
                expense_level = self.data['content']['last12']['debit']['charge_off_range']
                if expense_level is not None:
                    expense_level_value = ls_dic.get(expense_level)
                ratio = income_level_value / expense_level_value
                print ratio
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
        except Exception as e:
            logging.error(e.message)
        return result

    def _cc_handle(self):
        """
        接口名称：人人网数据服务收入类标签接口
                  猎聘
        字段名称：rrx_inc_12m         近12月数据项
                  debit_card_12m_passentry_amount借记卡近12个月入账累计总金额
                  debit_card_12m_chargeoff_amount借记卡近12个月出账累计总金额

        输出：
        特征名称：income_expense_comparison  入账与支出关系
        """
        result = {"income_expense_comparison": PositiveSignedTypeDefault}

        try:
            income_level = self.data['result']['rrx_inc_12m']['debit_card_12m_passentry_amount']
            expense_level = self.data['result']['rrx_inc_12m']['debit_card_12m_chargeoff_amount']

            amount_list = ['0' + str(x) for x in range(0, 10)]
            amount_list = amount_list + [str(x) for x in range(10, 40)]
            if income_level is not None and expense_level is not None:
                income_level_index = amount_list.index(income_level)
                expense_level_index = amount_list.index(expense_level)
                ratio = income_level_index/expense_level_index
                if ratio >= 10:   # 入账远大于支出
                    result['income_expense_comparison'] = 1
                elif 1 < ratio < 10:   # 入账大于支出
                    result['income_expense_comparison'] = 2
                elif ratio == 1:   # 入账接进出账
                    result['income_expense_comparison'] = 3
                elif 0.1 < ratio < 1:   # 入账小于出账
                    result['income_expense_comparison'] = 4
                elif ratio <= 0.1:   # 入账远小于支出
                    result['income_expense_comparison'] = 5
        except Exception as e:
            logging.error(e.message)
            return result

        return result
