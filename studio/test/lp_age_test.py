# -*- coding:utf-8 -*-

import unittest

from vendor.utils.defaults import *

from studio.lp_dataocean_handle.lp_age import Handle

data = {
    'content': {
        'constellation': '水瓶座',
        'age': 24,
        'home_address': '江西 - 九江',
        'sex': '男',
    },
}
age_test = [20, -4, ""]
result = [20, PositiveSignedTypeDefault, PositiveSignedTypeDefault]


class TestPlugin(unittest.TestCase):

    def setUp(self):
        self.data = data

    def test_lp_personal_info(self):
        data = self.data.copy()
        data["content"]["age"] = age_test
        for age_data, r in zip(age_test, result):
            data["content"]["age"] = age_data
            handler = Handle(data)
            res = handler.handle()
            assert res.values()[0] == r


if __name__ == '__main__':
    unittest.main()
