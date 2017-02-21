# -*- coding:utf-8 -*-

import unittest

from vendor.utils.defaults import *

from studio.lp_dataocean_handle.lp_creditcard_count import Handle

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
credit_cards_num_test = ["0", "2", ""]

result = [0, 2, PositiveSignedTypeDefault]


class TestPlugin(unittest.TestCase):

    def setUp(self):
        self.data = data

    def test_lp_creditcard_count(self):
        for card_data, r in zip(credit_cards_num_test, result):
            data["result"]["rrx_once_all"]["credit_cards_num"] = card_data
            handler = Handle(data)
            res = handler.handle()
            assert res.values()[0] == r


if __name__ == '__main__':
    unittest.main()
