# -*- coding:utf-8 -*-

import unittest

from vendor.utils.defaults import *

from studio.lp_dataocean_handle.lp_pingan_multi_loan_count import Handle

data = {
    "result": 0,
    "message": None,
    "data": {
        "record": [
            {"matchType": "phone",
             "matchValue": "18627180708",
             "matchId": "AA28960E040AE2BB960CD4736012A791",
             "classification": [
                 {
                     "M6": {
                         "other": {
                             "orgNums": 1, "loanAmount": None, "totalAmount": "(200, 500]", "repayAmount": None
                         },
                         "bank": None,
                     }},
                 {
                     "M9": {
                         "other": {"orgNums": 1, "loanAmount": None, "totalAmount": "(0, 200]",
                                   "repayAmount": None},
                         "bank": {"orgNums": 1},
                     }},
                 {
                     "M12": {
                         "other": {"orgNums": 2, "loanAmount": None, "totalAmount": "(500, 1000]",
                                   "repayAmount": None},
                         "bank": {},
                     }},
                 {
                     "M24": {
                         "other": {"orgNums": 2, "loanAmount": None, "totalAmount": "(1000, 2000]",
                                   "repayAmount": None},
                         "bank": None,
                     }}
             ]
             }
        ],
        "phone": "18627180708",
        "imei": "",
        "imsi": ""}}


class TestPlugin(unittest.TestCase):
    def setUp(self):
        self.data = data

    def test_test(self):
        h = Handle(self.data)
        res = h.handle()
        assert res.values()[0] == 7

        self.data['result'] = 1
        h = Handle(self.data)
        res = h.handle()
        assert res.values()[0] == PositiveSignedTypeDefault


if __name__ == '__main__':
    unittest.main()
