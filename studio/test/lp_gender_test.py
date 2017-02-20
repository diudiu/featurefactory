# -*- coding:utf-8 -*-

import unittest
from vendor.utils.defaults import *
from studio.lp_dataocean_handle.lp_gender import Handle

data = {
    "result": "00",
    "result_message": "检测通过或查询有记录",
    "content": {
        "constellation": "水瓶座",
        "age": 24,
        "home_address": "江西-九江",
        "sex": "男"
    },
}


class TestPlugin(unittest.TestCase):
    def setUp(self):
        self.data = data

    def test_lp_gender(self):
        data = self.data
        h = Handle(data)
        res = h.handle()
        self.assertEqual(res['gender'], data['content']['sex'])

        data['result'] = '11'
        h = Handle(data)
        res = h.handle()
        self.assertEqual(res['gender'], StringTypeDefault)

        data['content']['sex'] = None

        handler = Handle(data)
        res = handler.handle()
        self.assertEqual(res['gender'], StringTypeDefault)


if __name__ == '__main__':
    unittest.main()
