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


class TestPlugin(unittest.TestCase):

    def setUp(self):
        self.data = data

    def test_miss_result(self):
        self.data['result'] = None
        handler = Handle(self.data)
        res = handler.handle()
        self.assertEqual(res["is_organization_g_black"], False)

    def test_reslut_value1(self):
        self.data['result'] = '11'
        handler = Handle(self.data)
        res = handler.handle()
        self.assertEqual(res["is_organization_g_black"], False)

    def test_reslut_value2(self):
        self.data['result'] = '00'
        handler = Handle(self.data)
        res = handler.handle()
        self.assertEqual(res["is_organization_g_black"], True)

if __name__ == '__main__':
    unittest.main()
