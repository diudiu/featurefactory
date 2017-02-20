# -*- coding:utf-8 -*-

import unittest

from studio.lp_dataocean_handle.lp_court_shixin_a_s import  Handle

data = {
    "result_message": "检测通过或查询有记录",
    "result": "00",
    "content": {}

}
test = [u'00', u'11', u'22']
result = [1, 0, 0]


class TestPlugin(unittest.TestCase):
    def setUp(self):
        self.data = data

    def test_court_shixin_a_s(self):
        data = self.data.copy()
        for t, r in zip(test, result):
            data["result"] = t
            handler = Handle(data)
            res = handler.handle()
            assert res.values()[0] == r


if __name__ == '__main__':
    unittest.main()
