# -*- coding:utf-8 -*-

import unittest

from studio.lp_dataocean_handle.lp_is_unclear_loan import Handle

data = {
    "status": 1,
    "message": "操作成功",
    "res_data": {
        "is_unclear_loan": 0,
    },
}
test_data = [0, 1, '']
result = [0, 1, 9999]


class TestPlugin(unittest.TestCase):
    def setUp(self):
        self.data = data

    def test_lp_is_unclear_loan(self):
        data = self.data.copy()
        for i, j in zip(test_data, result):
            data["res_data"]["is_unclear_loan"] = i
            handler = Handle(data)
            res = handler.handle()
            self.assertEqual(res['is_unclear_loan'], j)

        del data['res_data']
        handler = Handle(data)
        res = handler.handle()
        self.assertEqual(res['is_unclear_loan'], 9999)


if __name__ == '__main__':
    unittest.main()
