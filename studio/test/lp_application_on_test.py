# -*- coding:utf-8 -*-
import unittest
from featurefactory.studio.lp_dataocean_handle.lp_application_on import Handle
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
apply_datas = ['2017-04-01 12:20:10', 'None', '']


class TestPlugin(unittest.TestCase):

    def setUp(self):
        self.data = data

    def test_application_on(self):
        for apply_data in apply_datas:
            data = self.data.copy()
            data["application_on"] = apply_data
            handler = Handle(data)
            res = handler.handle()
            print res