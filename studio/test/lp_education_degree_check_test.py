# -*- coding:utf-8 -*-
import unittest
from studio.lp_dataocean_handle.lp_education_degree_check import Handle

data = {
    "result": "00",
    "result_message": "检测通过或查询有记录",
    "content": {
        "degree": {
            "is_key_subject": "N",
            "photo_style": "JPG",
            "graduate_time": "2014",
            "level_no": "106471201405000624",
            "graduate_result": "毕业",
            "graduate_style": "普通",
            "education_approach": "普通全日制",
            "photo": '',
            "college": "长江师范学院",
            "start_time": "20120907",
            "specialty": "财务管理",
            "degree": "本科"
        },
        "person_base": {
            "degree": "本科",
            "age": "25",
            "name": "李洁",
            "original_address": "重庆市渝北区",
            "id_card_code": "50011219910630066X",
            "birthday": "19910630",
            "gender": "2",
            "graduate_years": "2"
        },
        "college": {
            "school_category": "师范",
            "school_level": "本科",
            "school_nature": "普通高等教育",
            "graduate_school": "长江师范学院",
            "post_doctoral_studies": "0",
            "create_data": "2006",
            "master_pilot": "0",
            " science_batch": "本科第二批",
            "school_trade": "公办",
            "college_name": "长江师范学院",
            "is211": "N",
            "doctor_station": "0",
            "art_batch": "本科第二批",
            "address": "重庆市",
            "significant_accounts": "0",
            "manage_dept": "重庆市",
            "create_years": "10",
            "academician_count": "0"
        },
    },
}

test_data = ['博士后', '博士', 'MBA/EMBA', '硕士', '本科', '大专', '中专', '中技', '高中', '初中', 'None']
result = ['5', '10', '20', '30', '40', '50', '60', '70', '80', '90', '999']


class TestPlugin(unittest.TestCase):
    def setUp(self):
        self.data = data

    def test_test(self):
        data = self.data.copy()
        for d, value in zip(test_data, result):
            data["content"]["degree"]['degree'] = d
            handler = Handle(data)
            res = handler.handle()
            self.assertEqual(res['education_degree_check'], value)


if __name__ == '__main__':
    unittest.main()
