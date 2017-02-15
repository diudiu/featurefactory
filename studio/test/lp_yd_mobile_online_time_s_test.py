# -*- coding:utf-8 -*-

import unittest
from  studio.lp_dataocean_handle.lp_yd_mobile_online_time_s import Handle

data = {
    "result": "00",
    "result_message": "检测通过或查询有记录",
    "content": {
        "online_time": "(0,3)"
    }
}
online_times = ["(-2,-1)", "(0,3)", "[3,6)", "[6,12)", "[12,18)", "[18,24]", "(24,+)", "None", 5]
results = ['00', '11', '22', None]

class TestPlugin(unittest.TestCase):

    def setUp(self):
        self.data = data

    def test_lp_yd_mobile_online_time_s(self):
        data = self.data.copy()
        for result in results:
            data["result"] = result
            if data["result"] != '00':
                handler = Handle(data)
                res = handler.handle()
                print res
            elif data["result"] == '00':
                for online_time in online_times:
                    data['content']['online_time'] = online_time
                    handler = Handle(data)
                    res = handler.handle()
                    print res

if __name__ == '__main__':
    unittest.main()