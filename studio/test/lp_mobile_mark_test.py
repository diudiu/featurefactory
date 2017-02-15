# -*- coding:utf-8 -*-

import unittest

from studio.lp_dataocean_handle.lp_mobile_mark import Handle

data = {
    "tags": {
        "contactMain_IMSI1_IMEI1":
            {
                "city": "上海市上海市",
                "label": "未被标记",
                "operator": "上海移动",
            },
    },
}


class TestPlugin(unittest.TestCase):

    def setUp(self):
        self.data = data

    def test_test(self):
        data = self.data
        h = Handle(data)
        res = h.handle()
        self.assertEqual(res['mobile_mark'], data['tags']['contactMain_IMSI1_IMEI1']['label'])

        data['tags']['contactMain_IMSI1_IMEI1']['label'] = None
        h = Handle(data)
        res = h.handle()
        print res

if __name__ == '__main__':
    unittest.main()
