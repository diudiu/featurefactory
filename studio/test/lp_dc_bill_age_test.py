# -*- coding:utf-8 -*-

import unittest

from vendor.utils.defaults import *

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

result = [0, 2,0, PositiveSignedTypeDefault]


class TestPlugin(unittest.TestCase):

    def setUp(self):
        self.data = data

    def test_test(self):
        data = self.data.copy()
        for card_data, r in zip(debit_card_account_age_test, result):
            data["result"]["rrx_once_all"]["debit_card_account_age"] = card_data
            handler = Handle(data)
            res = handler.handle()
            assert res.values()[0] == r


if __name__ == '__main__':
    unittest.main()
