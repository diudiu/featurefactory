# -*- coding:utf-8 -*-

import unittest

from studio.lp_dataocean_handle.lp_is_pingan_multi_loan import Handle

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
                     }},
             ]
             }
        ],
        "phone": "18627180708",
        "imei": "",
        "imsi": "",
    }
}
result_test = ["0", "2", ""]
classification_test = [
    {},
    {"M6": {"other": {"orgNums": 1, "loanAmount": None, "totalAmount": "(200, 500]", "repayAmount": None},
            "bank": None, }}]


class TestPlugin(unittest.TestCase):

    def setUp(self):
        self.data = data

    def test_lp_is_pingan_multi_loan(self):
        data = self.data.copy()
        data["result"] = result_test
        data["data"]["record"][0]["classification"] = classification_test
        for result_data in result_test:
            data["result"] = result_data
            handler = Handle(data)
            res = handler.handle()
            print res


if __name__ == '__main__':
    unittest.main()
