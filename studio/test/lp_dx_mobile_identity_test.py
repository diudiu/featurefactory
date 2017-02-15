# -*- coding:utf-8 -*-

import unittest
from studio.lp_dataocean_handle.lp_dx_mobile_identity import Handle

data = {
    "result_message": "检测通过或查询有记录",
    "result": "00",
    "content": {}

}
results = [u'00', u'11', u'22', '']


class TestPlugin(unittest.TestCase):
    def setUp(self):
        self.data = data
        self.results = results

    def test_court_shixin_a_s(self):
        data = self.data.copy()
        for result in results:
            data["result"] = result
            if data["result"] != '00':
                handler = Handle(data)
                res = handler.handle()
                print res
            elif data["result"] == '00':
                handler = Handle(data)
                res = handler.handle()
                print res


if __name__ == '__main__':
    unittest.main()
