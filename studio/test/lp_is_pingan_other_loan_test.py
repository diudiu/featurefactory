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
results = [0, "0", 1, 3]


class TestPlugin(unittest.TestCase):

    def setUp(self):
        self.data = data

    def test_lp_is_pingan_other_loan(self):
        data = self.data.copy()
        a = open('res.txt', 'w+')
        for result in results:
            data['result'] = result
            handler = Handle(data)
            res = handler.handle()
            a.write(json.dumps(res) + '\n')
        a.close()

if __name__ == '__main__':
    unittest.main()