# -*- coding:utf-8 -*-

import unittest
import json
from studio.lp_dataocean_handle.lp_is_cur_corp_shixin import Handle

data = {
        "result": "00",
        "result_message": "检测通过或查询有记录",
        "content": {}
    }

results = ['00', '11', '22', '', 'None', '-888']


class TestPlugin(unittest.TestCase):

    def setUp(self):
        self.data = data
        self.results = results

    def test_lp_is_cur_corp_shixin(self):
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