# -*- coding:utf-8 -*-

import unittest
from vendor.utils.defaults import *
from studio.lp_dataocean_handle.lp_geo_location import Handle

data = {
    "content": {
        "status": 0,
        "result": {
            "location": {
                "lng": 114.23075168099999,
                "lat": 29.57908754899005
            },
            "formatted_address": "湖北省咸宁市崇阳县G56(杭瑞高速)",
            "business": "",
            "addressComponent": {
                "country": "中国",
                "country_code": 0,
                "province": "湖北省",
                "city": "咸宁市",
                "district": "崇阳县",
                "adcode": "421223",
                "street": "G56(杭瑞高速)",
                "street_number": "",
                "direction": "",
                "distance": ""
            },
            "pois": [],
            "poiRegions": [],
            "sematic_description": "大屋沈家南210米",
            "cityCode": 362
        }
    },
    "result_message": "检测通过或查询有记录",
    "result": "00"
}


class TestPlugin(unittest.TestCase):
    def setUp(self):
        self.data = data

    def test_test(self):
        h = Handle(self.data)
        res = h.handle()
        assert res.values()[0] == "咸宁市"

        self.data['result'] = '11'
        h = Handle(self.data)
        res = h.handle()
        assert res.values()[0] == StringTypeDefault


if __name__ == '__main__':
    unittest.main()
