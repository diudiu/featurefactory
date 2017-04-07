import unittest
from studio.lp_dataocean_handle.lp_income_level import Handle
data = {
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
                "months": 12,
                "salary": 1000,
                "work_start": "string",
                "work_end": "11",
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


class TestPlugin(unittest.TestCase):

    def setUp(self):
        self.data = data

    def test_lp_income_level(self):
        data = self.data.copy()
        handler = Handle(data)
        res = handler.handle()
        print res


if __name__ == '__main__':
    unittest.main()