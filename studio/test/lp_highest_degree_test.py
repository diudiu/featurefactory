# -*- coding: utf-8 -*-

import unittest
import json
from studio.lp_dataocean_handle.lp_highest_degree import Handle


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
            "comp_name": "string",
            "months": 0,
            "salary": 0,
            "work_start": "string",
            "work_end": "string",
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
        },
        {
            "school": "string",
            "start": "string",
            "end": "string",
            "degree": "30",
            "degree_name": "",
            "tz": 0
        },
        {
            "school": "string",
            "start": "string",
            "end": "string",
            "degree": "20",
            "degree_name": "中专",
            "tz": 0
        }
    ]
}

degrees = ["5", "10", "20", "30", "40", "50", "60", "70", "80", "90", "None", ""]


class TestPlugin(unittest.TestCase):

    def setUp(self):
        self.data = data

    def test_lp_highest_degree(self):
        data = self.data.copy()
        a = open('res.txt', 'w+')
        for degree in degrees:
            data['edu_exp_form'][0]['degree'] = degree
            handler = Handle(data)
            res = handler.handle()
            a.write(json.dumps(res) + '\n')
        a.close()


if __name__ == '__main__':
    unittest.main()