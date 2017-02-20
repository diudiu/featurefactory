# -*- coding:utf-8 -*-

import unittest

from studio.lp_dataocean_handle.lp_dc_bill_age import Handle

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
    }
}
debit_card_account_age_test = ["0", "2", "0.5", ""]


class TestPlugin(unittest.TestCase):

    def setUp(self):
        self.data = data

    def test_lp_cc_bill_age(self):
        data = self.data.copy()
        data["result"]["rrx_once_all"]["debit_card_account_age"] = debit_card_account_age_test
        for card_data in debit_card_account_age_test:
            data["result"]["rrx_once_all"]["debit_card_account_age"] = card_data
            handler = Handle(data)
            res = handler.handle()
            print res


if __name__ == '__main__':
    unittest.main()
