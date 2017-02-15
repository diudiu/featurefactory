# -*- coding:utf-8 -*-

import unittest

from studio.lp_dataocean_handle.lp_overspeed_count import Handle

data = {
    "XXXX1234":
        {
            "result": "00",
            "result_message": "检测通过或查询有记录",
            "content": {
                "license_plate": "渝FC8***",
                "start_time": "201401",
                "end_time": "201412",
                "over_speed_times": 2,
                "over_speed_list": [{
                    "count_month": "201506",
                    "month_times": '',
                    "section": "北京通州站-河北燕郊站，河北廊坊站-天津蓟县站",}
                ]
            }
        },
    "XXXX5678":
        {
            "result": "00",
            "result_message": "检测通过或查询有记录",
            "content": {
                "license_plate": "渝FC8***",
                "start_time": "201401",
                "end_time": "201412",
                "over_speed_times": 1,
                "over_speed_list": [{
                    "count_month": "201506",
                    "month_times": 2,
                    "section": "北京通州站-河北燕郊站，河北廊坊站-天津蓟县站",}
                ]
            }
        },
        "XXXX5679":
        {
            "result": "11",
            "result_message": "检测通过或查询有记录",
            "content": {
                "license_plate": "渝FC8***",
                "start_time": "201401",
                "end_time": "201412",
                "over_speed_times": 2,
                "over_speed_list": [{
                    "count_month": "201506",
                    "month_times": 2,
                    "section": "北京通州站-河北燕郊站，河北廊坊站-天津蓟县站",}
                ]
            }
        },
}


class TestPlugin(unittest.TestCase):
    def setUp(self):
        self.data = data

    def test_test(self):
        h = Handle(self.data)
        res = h.handle()
        print res


if __name__ == '__main__':
    unittest.main()
