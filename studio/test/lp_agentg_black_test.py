# -*- coding:utf-8 -*-
import unittest
from studio.lp_dataocean_handle.lp_agentg_black import Handle

data = {
        "result": "00",
        "result_message": "检测通过或查询有记录",
        "content": [{
            "type": "欺诈",
            "date": "",
            "desc": "",
            "originalRet": {
                "name": "100",
                "pid": "100",
                "mobile": "0",
                "confirm_type": "欺诈",
                "confirm_details": "",
                "confirmed_at": "2014年02月01日",
                "loan_type": "",
                "applied_at": ""
            }
        }]
    }

test = [u'00', u'11', u'22']
result = [1, 0, 0]


class TestPlugin(unittest.TestCase):

    def setUp(self):
        self.data = data
        self.test = test

    def test_agentg_black(self):
        data = self.data.copy()
        for t, r in zip(self.test, result):
            data["result"] = t
            handler = Handle(data)
            res = handler.handle()
            self.assertEqual(res['is_organization_g_black'], r)


if __name__ == '__main__':
    unittest.main()
