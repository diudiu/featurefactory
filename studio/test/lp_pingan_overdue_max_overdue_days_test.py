# -*- coding:utf-8 -*-

import unittest
import json
from studio.lp_dataocean_handle.lp_pingan_max_overdue_days import Handle

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
M6_otherLoan_max_overdue_days_list = ["1", "2", "5", "100", "", "None"]


class TestPlugin(unittest.TestCase):

    def setUp(self):
        self.data = data

    def test_lp_pingan_max_overdue_days(self):
        data = self.data.copy()
        a = open('res.txt', 'w+')
        for M6_otherLoan_max_overdue_days in M6_otherLoan_max_overdue_days_list:
            data['data']['record'][0]['classification'][1]['M6']['otherLoan']['longestDays'] = M6_otherLoan_max_overdue_days
            handler = Handle(data)
            res = handler.handle()
            a.write(json.dumps(res) + '\n')
        a.close()

if __name__ == '__main__':
    unittest.main()