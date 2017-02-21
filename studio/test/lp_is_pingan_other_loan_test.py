# -*- coding:utf-8 -*-

import unittest
import json
from studio.lp_dataocean_handle.lp_is_pingan_other_loan import Handle

data = {
    "result": 0,
    "message": None,
    "data": {
        "phone": "15821732543",
        "imei": "",
        "imsi": ""
    }
}
test = [0, "0", 1, 3]
result = [1, 0, 0, 0]


class TestPlugin(unittest.TestCase):

    def setUp(self):
        self.data = data

    def test_lp_is_pingan_other_loan(self):
        data = self.data.copy()
        for t, r in zip(test, result):
            data['result'] = t
            handler = Handle(data)
            res = handler.handle()
            assert res.values()[0] == r


if __name__ == '__main__':
    unittest.main()