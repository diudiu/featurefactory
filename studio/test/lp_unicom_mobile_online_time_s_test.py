# -*- coding:utf-8 -*-
import unittest
from  featurefactory.studio.lp_dataocean_handle.lp_unicom_mobile_online_time_s import Handle

data = {
    "result": "00",
    "result_message": "检测通过或查询有记录",
    "content": {
        "online_time": ""
    }
}
online_times = ["[0-1]", "(1-2]", "[3-6]", "[7-12]", "[13-24)", "[25-36)", "[37,+)", "None", None]
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