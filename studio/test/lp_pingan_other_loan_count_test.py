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
            "orgNums": "28",
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
M6_orgNums_list = [1, 2, 5, 100, '',  'None']


class TestPlugin(unittest.TestCase):

    def setUp(self):
        self.data = data

    def test_lp_pingan_other_laon_count(self):
        data = self.data.copy()
        a = open('res.txt', 'w+')
        for M6_orgNums in M6_orgNums_list:
            data['data']['201601']['orgNums'] = M6_orgNums
            handler = Handle(data)
            res = handler.handle()
            a.write(json.dumps(res) + '\n')
        a.close()

if __name__ == '__main__':
    unittest.main()