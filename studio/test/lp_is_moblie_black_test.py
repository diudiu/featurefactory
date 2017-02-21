# -*- coding:utf-8 -*-

import unittest
from vendor.utils.defaults import *
from studio.lp_dataocean_handle.lp_is_mobile_black import Handle

data = {
    "result": 0,
    "data": {
        "grayscale": {
            # "M0": {},
            # "bank": {
            #     "contactTimes": "3"
            # }
        }
    }
}
test = [0, 2, 3]
result = [1, 0, BooleanTypeDefault]


class TestPlugin(unittest.TestCase):
    def setUp(self):
        self.data = data

    def test_lp_is_pingan_overdue_loan(self):
        data = self.data.copy()
        for t, r in zip(test, result):
            data['result'] = t
            handler = Handle(data)
            res = handler.handle()
            assert res.values()[0] == r


if __name__ == '__main__':
    unittest.main()
