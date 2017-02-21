# -*- coding:utf-8 -*-

import unittest

from vendor.utils.defaults import *

from studio.lp_dataocean_handle.lp_card_id import Handle

data = {
    "product_code": "890wefjf320if0i302f0j3f0f",
    "apply_id": "APPLY20161011111111890934",
    "callback": "http://10.20.1.110/api/credit/result/",
    "name": "张三",
    "card_id": "411402198002039872",
    "mobile": "18989821092",
    "longitudu": 23.45678,
    "latitude": 145.23342,
    "contacts": 30,
    "application_on": "2017-02-01 12:20:10",
}
card_id_test = ["12345625545", "235643225451X", ""]


class TestPlugin(unittest.TestCase):

    def setUp(self):
        self.data = data

    def test_lp_card_id(self):
        handler = Handle(self.data)
        res = handler.handle()
        assert res.values()[0] == self.data['card_id']

        self.data['card_id'] = ''
        handler = Handle(self.data)
        res = handler.handle()
        assert res.values()[0] == StringTypeDefault


if __name__ == '__main__':
    unittest.main()
