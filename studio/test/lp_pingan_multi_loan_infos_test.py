# -*- coding:utf-8 -*-

import unittest

from studio.lp_dataocean_handle.lp_pingan_multi_loan_infos import Handle

data = {
    "result": 0,
    "message": None,
    "data": {
        "record": [
            {"matchType": "phone",
             "matchValue": "18627180708",
             "matchId": "AA28960E040AE2BB960CD4736012A791",
             "classification": [
                 {"M3": {"other": {"loanAmount": None}}},

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
                         "bank": None,
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
             },

        ],
        "phone": "18627180708",
        "imei": "",
        "imsi": ""}}

result = {'pingan_multi_loan_infos': [{'M6': {'other': {'totalAmount': '(200, 500]', 'orgNums': 1}}},
                                      {'M9': {'other': {'totalAmount': '(0, 200]', 'orgNums': 1}}},
                                      {'M12': {'other': {'totalAmount': '(500, 1000]', 'orgNums': 2}}},
                                      {'M24': {'other': {'totalAmount': '(1000, 2000]', 'orgNums': 2}}}]}


class TestPlugin(unittest.TestCase):
    def setUp(self):
        self.data = data

    def test_test(self):
        h = Handle(self.data)
        res = h.handle()
        self.assertEqual(res, result)


if __name__ == '__main__':
    unittest.main()
