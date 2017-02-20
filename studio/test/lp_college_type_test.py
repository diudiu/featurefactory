# -*- coding: utf-8 -*-

import unittest
from studio.lp_dataocean_handle.lp_college_type import Handle

data = {
    "content": {
        "person_base": {
            "original_address": "",
            "id_card_code": "130**24821",
            "name": "甄**",
            "degree": "专科",
            "gender": "女",
            "age": "25",
            "birthday": "19910512",
            "graduate_years": "4"
        },
        "college": {
            "create_data": "",
            "master_pilot": "",
            "manage_dept": "",
            "science_batch": "",
            "school_nature": "本科",
            "school_category": "",
            "post_doctoral_studies": None,
            "art_batch": "",
            "school_level": "",
            "create_years": "",
            "significant_accounts": "",
            "graduate_school": "",
            "school_trade": "",
            "doctor_station": "",
            "address": "",
            "is211": "N",
            "academician_count": "",
            "college_name": "石家庄学院"
        },
        "degree": {
            "degree": "专科",
            "level_no": None,
            "photo": "",
            "start_time": "2010",
            "specialty": "生物技术及应用",
            "graduate_style": "普通",
            "graduate_time": "2013",
            "graduate_result": "毕业",
            "education_approach": "普通全日制",
            "college": "石家庄学院",
            "photo_style": "jpg",
            "is_key_subject": "N"
        }
    },
    "result_message": "检测通过或查询有记录",
    "result": "00"
}

degrees = ["985,211", "211,985", "专科", "本科", "None", "985", "211", ]


class TestPlugin(unittest.TestCase):

    def setUp(self):
        self.data = data

    def test_lp_highest_degree(self):
        data = self.data.copy()
        for degree in degrees:
            data['content']['college']['school_nature'] = degree
            handler = Handle(data)
            res = handler.handle()
            print res

if __name__ == '__main__':
    unittest.main()