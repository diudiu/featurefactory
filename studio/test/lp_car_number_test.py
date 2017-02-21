# -*- coding:utf-8 -*-

import unittest

from vendor.utils.defaults import *

from studio.lp_dataocean_handle.lp_car_number import Handle

data = {
    "status": "OK",
    "result": [
        {
            "license_no": "豫SFD**",
            "run_miles": "20000.00",
            "ton_count": "0.0000", "use_years": "5",
            "assets_relation": "1",
            "use_nature_code": "家庭⾃⽤",
            "frame_no": "LBEXDA****87X530718",
            "car_kind_code": "客⻋",
            "seat_count": "5",
            "license_color_code": "蓝",
            "usable": "1",
            "exhaust_scale": "1.5990",
            "run_area_code": "中国境内（ 不含港、 澳、 台） ",
            "purchase_price": "5-8万",
            "engine_no": "7B50**12",
            "mobile": "134****7600",
            "enroll_date": "2007-11-03 00:00:00.0",
            "brand_name": "北京现代BH7162MW轿⻋",
            "ccity": "信阳"
        },
        {"license_no": "豫SFD123", },
        {"license_no": "豫SFD456", },

    ]
}

result = ["豫SFD123", "豫SFD456", "豫SFD**"]


class TestPlugin(unittest.TestCase):

    def setUp(self):
        self.data = data

    def test_lp_application_on(self):
        handler = Handle(data)
        res = handler.handle()
        assert res == result
        data["result"] = ''
        handler = Handle(data)
        res = handler.handle()
        assert res.values()[0] == ListTypeDefault


if __name__ == '__main__':
    unittest.main()
