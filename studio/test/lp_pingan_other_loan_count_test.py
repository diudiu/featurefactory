# -*- coding:utf-8 -*-

import unittest
import json
from studio.lp_dataocean_handle.lp_pingan_other_loan_count import Handle

data = {
    "result": 0,
    "message": None,
    "data": {
        "201603": {
            "orgNums": "23",
            "queryNums": "123"
        },
        "201602": None,
        "201601": {
            "orgNums": None,
            "queryNums": "123"
        },
        "201512": {
            "orgNums": "29",
            "queryNums": "123"
        },
        "201511": {
            "orgNums": "",
            "queryNums": "123"
        },
        "201510": {
            "orgNums": "12",
            "queryNums": "123"
        },
        "201509": {
            "orgNums": "22",
            "queryNums": "123"
        },
        "201508": {
            "orgNums": "23",
            "queryNums": "123"
        },
        "201507": {
            "orgNums": "33",
            "queryNums": "123"
        },
        "201506": {
            "orgNums": "20",
            "queryNums": "123"
        },
        "201505": {
            "orgNums": "2",
            "queryNums": "123"
        },
        "201504": {
            "orgNums": "3",
            "queryNums": "123"
        }
    }
}


class TestPlugin(unittest.TestCase):

    def setUp(self):
        self.data = data

    def test_lp_pingan_other_laon_count(self):

        handler = Handle(data)
        res = handler.handle()
        assert res.values()[0] == 64


if __name__ == '__main__':
    unittest.main()