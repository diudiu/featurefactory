# -*- coding:utf-8 -*-

from featrue_process import FeatureProcess

data = {
        'status': u'00',
        'message': '',
        'content': {
            'constellation': '水瓶座',
            'age': 10,
            'home_address': '江西 - 九江',
            'sex': '男',
        },
    }
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
        "application_on": "2015-02-01 12:20:10",
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

def test():
    fecture_obj = FeatureProcess('apply_register_duration', data)
    result = fecture_obj.run()
    print result


if __name__ == '__main__':
    test()
