# -*- coding:utf-8 -*-

from featrue_process import FeatureProcess

data = {
    # 'age': {
    #     'status': u'00',
    #     'message': '',
    #     'content': {
    #         'constellation': '水瓶座',
    #         'age': 10,
    #         'home_address': '江西 - 九江',
    #         'sex': '男',
    #     },
    # },
    # 'apply_register_duration': {
    #     "apply_data": {
    #         "product_code": "890wefjf320if0i302f0j3f0f",
    #         "apply_id": "APPLY20161011111111890934",
    #         "callback": "http://10.20.1.110/api/credit/result/",
    #         "name": "张三",
    #         "card_id": "411402198002039872",
    #         "mobile": "18989821092",
    #         "longitudu": 23.45678,
    #         "latitude": 145.23342,
    #         "contacts": 30,
    #         "application_on": "2017-02-01 12:20:10",
    #     },
    #     "portrait_data": {
    #         "product_code": "string",
    #         "registration_on": "2016-01-18",
    #         "name": "string",
    #         "card_id": "372922199312341111",
    #         "mobile": "string",
    #         "email": "string",
    #         "city_code": "string",
    #         "city_name": "string",
    #         "now_indust_code": "string",
    #         "now_indust_name": "string",
    #         "work_age": 0,
    #         "complete_degree": 65,
    #         "cur_status": "string",
    #         "upload_contact": 0,
    #         "sns_friends_cnt": 0,
    #         "sns_sd_friend_cnt": 0,
    #         "sns_h_fans_cn": 0,
    #         "sns_skill_tag_list": [
    #             {
    #                 "skill_tag": "string",
    #                 "certified_num": 0
    #             }
    #         ],
    #         "work_exp_form": [
    #             {
    #                 "title": "string",
    #                 "has_certified": "string",
    #                 "certified_num": 0,
    #                 "comp_name": "string",
    #                 "months": 0,
    #                 "salary": 0,
    #                 "work_start": "string",
    #                 "work_end": "string",
    #                 "industry": "string",
    #                 "industry_name": "string",
    #                 "dq": "string",
    #                 "dq_name": "string"
    #             }
    #         ],
    #         "edu_exp_form": [
    #             {
    #                 "school": "string",
    #                 "start": "string",
    #                 "end": "string",
    #                 "degree": "string",
    #                 "degree_name": "string",
    #                 "tz": 0
    #             }
    #         ]
    #     }
    #
    # },
    # 'car_count': {
    #     "status": "OK",
    #     "result": [
    #         {
    #             "license_no": "豫SFD**",
    #             "run_miles": "20000.00",
    #             "ton_count": "0.0000", "use_years": "5",
    #             "assets_relation": "1",
    #             "use_nature_code": "家庭⾃⽤",
    #         },
    #     ]
    # },
    # 'car_number': {
    #     "status": "OK",
    #     "result": [
    #         {
    #             "license_no": "豫SFD**",
    #             "run_miles": "20000.00",
    #             "ton_count": "0.0000", "use_years": "5",
    #             "assets_relation": "1",
    #             "use_nature_code": "家庭⾃⽤",
    #             "frame_no": "LBEXDA****87X530718",
    #             "car_kind_code": "客⻋",
    #             "seat_count": "5",
    #             "license_color_code": "蓝",
    #             "usable": "1",
    #             "exhaust_scale": "1.5990",
    #             "run_area_code": "中国境内（ 不含港、 澳、 台） ",
    #             "purchase_price": "5-8万",
    #             "engine_no": "7B50**12",
    #             "mobile": "134****7600",
    #             "enroll_date": "2007-11-03 00:00:00.0",
    #             "brand_name": "北京现代BH7162MW轿⻋",
    #             "ccity": "信阳"
    #         },
    #         {"license_no": "豫SFD123"},
    #         {"license_no": "豫SFD456"},
    #
    #     ]
    # },
    'cur_company': {
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
                "comp_name": "",
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
    },
}


def test():
    for feature_name, datas in data.items():
        fecture_obj = FeatureProcess(feature_name, datas)
        result = fecture_obj.run()
        print result


if __name__ == '__main__':
    test()


