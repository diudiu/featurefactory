# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/26
    Change Activity:
"""
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'featurefactory.settings')

from apps.etl.dataclean import DataClean
from vendor.utils.constant import cons


def dataocean_test():
    origin_data = {
        "status": 1,
        "message": "操作成功",
        "res_data": {
            "status": "1",
            "message": "操作成功",
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                    "constellation": "狮子座",
                    "age": 26,
                    "home_address": "埃尔文森林-暴风城",
                    "sex": "男"
                }
            }
        }
    }
    cleaner = DataClean(origin_data, cons.LP_DATAOCEAN)
    res = cleaner.worked()
    print res


def cc_credit_test():
    origin_data = {
        "status": 1,
        "message": "操作成功",
        "res_data": {
            "status": "OK",
            "ult": {
                "rrx_once_all": {
                    "banks_num": "开卡银行个数",
                    "debit_cards_num": "借记卡张数",
                    "credit_cards_num": "信用卡张数",
                    "debit_card_account_age": "借记卡账龄",
                    "credit_card_account_age": "信用卡账龄"
                },
                "rrx_inc_3m": {
                    "debit_card_3m_chargeoff_amount": "借记卡近 3 个月出账累计总金额",
                    "debit_card_3m_chargeoff_num": "借记卡近 3 个月出账累计总笔数",
                    "debit_card_3m_passentry_amount": "借记卡近 3 个月入账累计总金额",
                    "debit_card_3m_passentry_num": "借记卡近 3 个月入账累计总笔数",
                    "credit_card_3m_pay_amount": "信用卡近 3 个月信用卡消费总金额",
                    "credit_card_3m_repay_num": "信用卡近 3 个月还款总笔数"
                },
                "rrx_inc_12m": {
                    "debit_card_12m_chargeoff_amount": "借记卡近12个月出账累计总金额",
                    "debit_card_12m_chargeoff_num": "借记卡近12个月出账累计总笔数",
                    "debit_card_12m_pay_amount": "借记卡近12个月消费累计总金额",
                    "debit_card_12m_passentry_amount": "借记卡近12个月入账累计总金额",
                    "debit_card_12m_passentry_num": "借记卡近12个月入账累计总笔数",
                    "credit_card_12m_pay_amount": "信用卡近12个月信用卡消费总金额",
                    "credit_card_12m_pay_num": "信用卡近12个月信用卡消费总笔数",
                    "credit_card_12m_repay_amount": "信用卡近12个月信用卡还款总金额",
                    "credit_card_12m_repay_num": "信用卡近12个月还款总笔数",
                    "credit_card_12m_payables_amount": "信用卡近12个月累计应还总金额",
                    "credit_card_12m_online_pay_amount": "信用卡近12个月信用卡线上消费总金额"
                }
            }
        }
    }
    cleaner = DataClean(origin_data, cons.LP_CC_CAR_CREDIT)
    res = cleaner.worked()
    print res

if __name__ == '__main__':
    cc_credit_test()
