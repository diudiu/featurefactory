# -*- coding:utf-8 -*-
import unittest
from studio.lp_dataocean_handle.lp_apply_register_duration import Handle
<<<<<<< HEAD

=======
>>>>>>> ed2dd7ad4669a84c046eb83ac35f79ee9fc1c10c
data = {
    "apply_data": {
        "product_code": "890wefjf320if0i302f0j3f0f",
        "apply_id": "APPLY20161011111111890934",
        "callback": "http://10.20.1.110/api/credit/result/",
        "name": "张三",
        "card_id": "411402198002039872",
        "mobile": "18989821092",
        "longitudu": 23.45678,
        "latitude": 145.23342,
        "contacts": 30,
        "application_on": "2017-02-01 12:20:10",
    },
    "portrait_data": {
        "product_code": "string",
        "registration_on": "2016-01-18",
        "name": "string",
        "card_id": "372922199312341111",
        "mobile": "string",
        "email": "string",
        "city_code": "string",
        "city_name": "string",
        "now_indust_code": "string",
        "now_indust_name": "string",
        "work_age": 0,
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
                "degree_name": "string",
                "tz": 0
            }
        ]
    }

}

applications_on = ['2017-02-01 12:20:10', 'None']
registrations_on = ['2017-02-01', 'None']


class TestPlugin(unittest.TestCase):
    def setUp(self):
        self.data = data

    def test_application(self):
        data = self.data.copy()
        for application_on in applications_on:
            data["apply_data"]["application_on"] = application_on
            handler = Handle(data)
            res = handler.handle()
            print res

    def test_registration(self):
        data = self.data.copy()
        for registration_on in registrations_on:
            data["portrait_data"]["registration_on"] = registration_on
            handler = Handle(data)
            res = handler.handle()
            print res


if __name__ == '__main__':
    unittest.main()
