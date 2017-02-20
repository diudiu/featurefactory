# -*- coding:utf-8 -*-

import unittest

from studio.lp_dataocean_handle.lp_cc_bill_age import Handle

data = {
    "status": "OK",
    "result": {
        "rrx_once_all": {
            "banks_num": "开卡银行个数",
            "debit_cards_num": "借记卡张数",
            "credit_cards_num": "1",
            "debit_card_account_age": "2",
            "credit_card_account_age": "3"
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
credit_card_account_age_test = ["0", "2", "0.5", ""]


class TestPlugin(unittest.TestCase):

    def setUp(self):
        self.data = data

    def test_lp_cc_bill_age(self):
        data = self.data.copy()
        data["result"]["rrx_once_all"]["credit_card_account_age"] = credit_card_account_age_test
        for card_data in credit_card_account_age_test:
            data["result"]["rrx_once_all"]["credit_card_account_age"] = card_data
            handler = Handle(data)
            res = handler.handle()
            print res


if __name__ == '__main__':
    unittest.main()
