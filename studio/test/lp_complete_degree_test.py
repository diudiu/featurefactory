# -*- coding:utf-8 -*-

import unittest

from vendor.utils.defaults import *

from studio.lp_dataocean_handle.lp_complete_degree import Handle

data = {
    "complete_degree": 65,
    "cur_status": "string",
    "upload_contact": 0,
    "sns_friends_cnt": 0,
    "sns_sd_friend_cnt": 0,
    "sns_h_fans_cn": 0,
    "sns_skill_tag_list": [
        {
            "skill_tag": "string",
            "certified_num": 0
        }
    ],
}
complete_degree_test = [50, 0, ""]
result = [50, 0, PositiveSignedTypeDefault]


class TestPlugin(unittest.TestCase):

    def setUp(self):
        self.data = data

    def test_lp_complete_degree(self):
        data = self.data.copy()
        data["complete_degree"] = complete_degree_test
        for degree_data, r in zip(complete_degree_test, result):
            data["complete_degree"] = degree_data
            handler = Handle(data)
            res = handler.handle()
            assert res.values()[0] == r


if __name__ == '__main__':
    unittest.main()
