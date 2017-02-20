# -*- coding:utf-8 -*-

import unittest
import json
from studio.lp_dataocean_handle.lp_is_pingan_overdue_loan import Handle

data = {
    "result": 0,
    "message": None,
    "data": {
        "record": [{
            "matchType": "idCard",
            "matchValue": "340825198609101051",
            "matchId": "92a297643fdcd96644cf30942b8a2e5f",
            "classification": [
                {
                    "M3": {
                        "bankCredit": None,
                        "otherLoan": {
                            "orgNums": 12,
                            "recordNums": 1,
                            "maxAmount": "(1000, 2000]",
                            "longestDays": "6"
                        },
                        "otherCredit": None,
                        "bankLoan": None
                        }
                },
                {
                    "M6": {
                        "bankCredit": None,
                        "otherLoan": {
                            "orgNums": 1,
                            "recordNums": 1,
                            "maxAmount": "(1000, 2000]",
                            "longestDays": "1"
                        },
                        "otherCredit": None,
                        "bankLoan": None
                        }
                },
                {
                    "M9": {
                        "bankCredit": None,
                        "otherLoan": {
                            "orgNums": 1,
                            "recordNums": 2,
                            "maxAmount": "(1000, 2000]",
                            "longestDays": "1"
                        },
                        "otherCredit": None,
                        "bankLoan": None
                    }
                },
                {
                    "M24": {
                        "bankCredit": None,
                        "otherLoan": {
                            "orgNums": 1,
                            "recordNums": 1,
                            "maxAmount": "(1000, 2000]",
                            "longestDays": "1"
                        },
                        "otherCredit": None,
                        "bankLoan": None
                    }
                }
            ]
        }
        ],
        "phone": "15821732543",
        "imei": "",
        "imsi": ""}
}
results = [0, "0", 1, 3]


class TestPlugin(unittest.TestCase):

    def setUp(self):
        self.data = data

    def test_lp_is_pingan_overdue_loan(self):
        data = self.data.copy()
        a = open('res.txt', 'w+')
        for result in results:
            data['result'] = result
            handler = Handle(data)
            res = handler.handle()
            b = json.dumps(res)
            a.write(b + '\n')
        a.close()

if __name__ == '__main__':
    unittest.main()