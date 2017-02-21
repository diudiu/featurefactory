# -*- coding: utf-8 -*-

import unittest
import json
from studio.lp_dataocean_handle.lp_cur_company import Handle


data = {
    "product_code": "string",
    "name": "string",
    "card_id": "string",
    "mobile": "string",
    "email": "string",
    "city_code": "string",
    "city_name": "string",
    "now_indust_code": "string",
    "now_indust_name": "string",
    "work_age": 0,
    "complete_degree": 0,
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
    "work_exp_form": [
        {
            "title": "string",
            "has_certified": "string",
            "certified_num": 0,
            "comp_name": "数云",
            "months": 0,
            "salary": 0,
            "work_start": "string",
            "work_end": "20160609",
            "industry": "string",
            "industry_name": "string",
            "dq": "string",
            "dq_name": "string"
        },
        {
            "title": "string",
            "has_certified": "string",
            "certified_num": 0,
            "comp_name": "百度",
            "months": 0,
            "salary": 0,
            "work_start": "string",
            "work_end": "20170605",
            "industry": "string",
            "industry_name": "string",
            "dq": "string",
            "dq_name": "string"
        },
        {
            "title": "string",
            "has_certified": "string",
            "certified_num": 0,
            "comp_name": "腾讯",
            "months": 0,
            "salary": 0,
            "work_start": "string",
            "work_end": "20180809",
            "industry": "string",
            "industry_name": "string",
            "dq": "string",
            "dq_name": "string"
        }
    ],
    "edu_exp_form": [
        {
            "school": "string",
            "start": "string",
            "end": "string",
            "degree": "string",
            "degree_name": "中专",
            "tz": 0
        }
    ]
}

comp_names = ["jiuding", "", "国务院"]


class TestPlugin(unittest.TestCase):

    def setUp(self):
        self.data = data

    def test_lp_cur_company(self):
        data = self.data.copy()
        a = open('res.txt', 'w+')
        for comp_name in comp_names:
            data['work_exp_form'][2]['comp_name'] = comp_name
            handler = Handle(data)
            res = handler.handle()
            a.write(json.dumps(res) + '\n')
        a.close()


if __name__ == '__main__':
    unittest.main()