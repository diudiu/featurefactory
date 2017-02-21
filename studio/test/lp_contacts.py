# -*- coding:utf-8 -*-

import unittest

from studio.lp_dataocean_handle.lp_contacts import Handle
from vendor.utils.defaults import *

data = {
    'product_code': '890wefjf320if0i302f0j3f0f',
    'apply_id': 'APPLY20161011111111890934',
    'callback': 'http://10.20.1.110/api/credit/result/',
    'name': '张三',
    'card_id': '411402198002039872',
    'mobile': '18989821092',
    'longitudu': 23.45678,
    'latitude': 145.23342,
    'contacts': 30,
    'application_on': '2017-02-01 12:20:10'
}


class TestPlugin(unittest.TestCase):
    def setUp(self):
        self.data = data

    def test_lp_contacts_count(self):

        handler = Handle(self.data)
        res = handler.handle()
        assert res.values()[0] == 30

        data['contacts'] = None
        handler = Handle(self.data)
        res = handler.handle()
        assert res.values()[0] == PositiveSignedTypeDefault

if __name__ == '__main__':
    unittest.main()
