# -*- coding:utf-8 -*-

import unittest

from studio.lp_dataocean_handle.lp_personal_info import Handle

data = {
    'content': {
        'constellation': '水瓶座',
        'age': 24,
        'home_address': '江西 - 九江',
        'sex': '男',
    },
}
age_test = [20, ""]


class TestPlugin(unittest.TestCase):

    def setUp(self):
        self.data = data

    def test_lp_personal_info(self):
        data = self.data.copy()
        data["content"]["age"] = age_test
        for age_data in age_test:
            data["content"]["age"] = age_data
            handler = Handle(data)
            res = handler.handle()
            print res


if __name__ == '__main__':
    unittest.main()
