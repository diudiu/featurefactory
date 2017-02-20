# -*- coding:utf-8 -*-

import unittest

from studio.lp_dataocean_handle.lp_car_count import Handle

data = {
    "status": "OK",
    "result": [
        {
            "license_no": "豫SFD**",
            "run_miles": "20000.00",
            "ton_count": "0.0000", "use_years": "5",
            "assets_relation": "1",
            "use_nature_code": "家庭⾃⽤",
        },
    ]
}
result_test = [data["result"], ""]


class TestPlugin(unittest.TestCase):

    def setUp(self):
        self.data = data

    def test_lp_car_count(self):
        data = self.data.copy()
        data["result"] = result_test
        for result_data in result_test:
            data["result"] = result_data
            handler = Handle(data)
            res = handler.handle()
            print res


if __name__ == '__main__':
    unittest.main()
