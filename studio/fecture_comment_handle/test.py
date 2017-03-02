# -*- coding:utf-8 -*-

from featrue_process import FeatureProcess

data = {
    'age': {
        'personal_info': {
            'status': u'00',
            'message': '',
            'content': {
                'constellation': '水瓶座',
                'age': 10,
                'home_address': '江西 - 九江',
                'sex': '男',
            },
        }
    },

    'apply_register_duration': {
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
    },

    'car_count': {
        'cc_car_credit': {
            "status": "OK",
            "result": [
                {
                    "license_no": "豫SFD**",
                    "run_miles": "20000.00",
                    "ton_count": "0.0000", "use_years": "5",
                    "assets_relation": "1",
                    "use_nature_code": "家庭⾃⽤",
                },
            ]
        }
    },

    'car_number': {
        "status": "OK",
        "result": [
            {
                "license_no": "豫SFD**",
                "run_miles": "20000.00",
                "ton_count": "0.0000", "use_years": "5",
                "assets_relation": "1",
                "use_nature_code": "家庭⾃⽤",
                "frame_no": "LBEXDA****87X530718",
                "car_kind_code": "客⻋",
                "seat_count": "5",
                "license_color_code": "蓝",
                "usable": "1",
                "exhaust_scale": "1.5990",
                "run_area_code": "中国境内（ 不含港、 澳、 台） ",
                "purchase_price": "5-8万",
                "engine_no": "7B50**12",
                "mobile": "134****7600",
                "enroll_date": "2007-11-03 00:00:00.0",
                "brand_name": "北京现代BH7162MW轿⻋",
                "ccity": "信阳"
            },
            {"license_no": "豫SFD123"},
            {"license_no": "豫SFD456"},

        ]
    },

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
    },

    'mobile_stability': {
        "trustutn_loan_phone": {
            "result": 0,
            "message": None,
            "res_data": {
                "tags": {
                    "18920019795__": {
                        "M0": {
                            "distributionOfContacts": {
                                "1": "16",
                                "2": "13",
                                "3": "1",
                                "4": "3",
                                "6": "2",
                                "7": "1",
                                "8": "1",
                                "10": "1",
                                "13": "2",
                                "22": "1",
                                "36": "1"
                            },
                            "dailyCallTimes": 8.901,
                            "hourStat": {
                                "night": 6,
                                "day": 158,
                                "morning": 14
                            },
                            "callTimes": '',
                            "calledTimes": '',
                            "smsNotifications": None,
                            "activeShortest": 1,
                            "activeLongest": 79236,
                            "activeAverage": 9615.126,
                            "contactAmount": 42,
                            "month": "201701"
                        },
                        "M1": {
                            "distributionOfContacts": {
                                "3": "1",
                                "4": "1",
                                "5": "1"
                            },
                            "dailyCallTimes": 0.388,
                            "hourStat": {
                                "night": 0,
                                "day": 12,
                                "morning": 0
                            },
                            "callTimes": 6,
                            "calledTimes": '',
                            "smsNotifications": None,
                            "activeShortest": 2,
                            "activeLongest": 10888,
                            "activeAverage": 3377,
                            "contactAmount": 3,
                            "month": "201612"
                        },
                        "M6": {
                            "month": "201611"
                        },
                        "M3": {
                            "month": "201610"
                        },
                        "M4": {
                            "distributionOfContacts": {
                                "1": "4",
                                "2": "3"
                            },
                            "dailyCallTimes": 0.334,
                            "hourStat": {
                                "night": 0,
                                "day": 10,
                                "morning": 0
                            },
                            "callTimes": 8,
                            "calledTimes": 2,
                            "smsNotifications": None,
                            "activeShortest": 6,
                            "activeLongest": 59391,
                            "activeAverage": 9786.223,
                            "contactAmount": 7,
                            "month": "201609"
                        },
                        "M5": {
                            "distributionOfContacts": {
                                "1": "18",
                                "2": "11",
                                "3": "2",
                                "5": "1",
                                "6": "1",
                                "10": "1"
                            },
                            "dailyCallTimes": 2.162,
                            "hourStat": {
                                "night": 6,
                                "day": 55,
                                "morning": 6
                            },
                            "callTimes": 38,
                            "calledTimes": 9,
                            "smsNotifications": None,
                            "activeShortest": 2,
                            "activeLongest": 156909,
                            "activeAverage": 10155.107,
                            "contactAmount": 34,
                            "month": "201608"
                        },
                        "T6": {
                            "distributionOfContacts": {
                                "1": "17",
                                "2": "14",
                                "3": "3",
                                "5": "1",
                                "7": "1",
                                "11": "1"
                            },
                            "dailyCallTimes": 0.446,
                            "hourStat": {
                                "night": 6,
                                "day": 65,
                                "morning": 6
                            },
                            "callTimes": 46,
                            "calledTimes": 31,
                            "smsNotifications": None,
                            "activeShortest": 2,
                            "activeLongest": 156909,
                            "activeAverage": 10876.54,
                            "contactAmount": 37,
                            "month": "halfyear"
                        }
                    },
                    "18920019796__": {
                        "M0": {
                            "distributionOfContacts": {
                                "1": "16",
                                "2": "13",
                                "3": "1",
                                "4": "3",
                                "6": "2",
                                "7": "1",
                                "8": "1",
                                "10": "1",
                                "13": "2",
                                "22": "1",
                                "36": "1"
                            },
                            "dailyCallTimes": 8.901,
                            "hourStat": {
                                "night": 6,
                                "day": 158,
                                "morning": 14
                            },
                            "callTimes": '',
                            "calledTimes": '',
                            "smsNotifications": None,
                            "activeShortest": 1,
                            "activeLongest": 79236,
                            "activeAverage": 9615.126,
                            "contactAmount": 42,
                            "month": "201701"
                        },
                        "M1": {
                            "distributionOfContacts": {
                                "3": "1",
                                "4": "1",
                                "5": "1"
                            },
                            "dailyCallTimes": 0.388,
                            "hourStat": {
                                "night": 0,
                                "day": 12,
                                "morning": 0
                            },
                            "callTimes": '',
                            "calledTimes": 6,
                            "smsNotifications": None,
                            "activeShortest": 2,
                            "activeLongest": 10888,
                            "activeAverage": 3377,
                            "contactAmount": 3,
                            "month": "201612"
                        },
                        "M2": {
                            "month": "201611"
                        },
                        "M3": {
                            "month": "201610"
                        },
                        "M4": {
                            "distributionOfContacts": {
                                "1": "4",
                                "2": "3"
                            },
                            "dailyCallTimes": 0.334,
                            "hourStat": {
                                "night": 0,
                                "day": 10,
                                "morning": 0
                            },
                            "callTimes": 8,
                            "calledTimes": '',
                            "smsNotifications": None,
                            "activeShortest": 6,
                            "activeLongest": 59391,
                            "activeAverage": 9786.223,
                            "contactAmount": 7,
                            "month": "201609"
                        },
                        "M5": {
                            "distributionOfContacts": {
                                "1": "18",
                                "2": "11",
                                "3": "2",
                                "5": "1",
                                "6": "1",
                                "10": "1"
                            },
                            "dailyCallTimes": 2.162,
                            "hourStat": {
                                "night": 6,
                                "day": 55,
                                "morning": 6
                            },
                            "callTimes": 38,
                            "calledTimes": 9,
                            "smsNotifications": None,
                            "activeShortest": 2,
                            "activeLongest": 156909,
                            "activeAverage": 10155.107,
                            "contactAmount": 34,
                            "month": "201608"
                        },
                        "T6": {
                            "distributionOfContacts": {
                                "1": "17",
                                "2": "14",
                                "3": "3",
                                "5": "1",
                                "7": "1",
                                "11": "1"
                            },
                            "dailyCallTimes": 0.446,
                            "hourStat": {
                                "night": 6,
                                "day": 65,
                                "morning": 6
                            },
                            "callTimes": 46,
                            "calledTimes": 31,
                            "smsNotifications": None,
                            "activeShortest": 2,
                            "activeLongest": 156909,
                            "activeAverage": 10876.54,
                            "contactAmount": 37,
                            "month": "halfyear"
                        }
                    },
                    "18920019798_8a404758b8f8b87c70006b8e9f4614db_": {
                        "M0": {
                            "distributionOfContacts": {
                                "1": "16",
                                "2": "13",
                                "3": "1",
                                "4": "3",
                                "6": "2",
                                "7": "1",
                                "8": "1",
                                "10": "1",
                                "13": "2",
                                "22": "1",
                                "36": "1"
                            },
                            "dailyCallTimes": 8.901,
                            "hourStat": {
                                "night": 6,
                                "day": 158,
                                "morning": 14
                            },
                            "callTimes": 75,
                            "calledTimes": 13,
                            "smsNotifications": None,
                            "activeShortest": 1,
                            "activeLongest": 79236,
                            "activeAverage": 9615.126,
                            "contactAmount": 42,
                            "month": "201701"
                        },
                        "M1": {
                            "distributionOfContacts": {
                                "3": "1",
                                "4": "1",
                                "5": "1"
                            },
                            "dailyCallTimes": 0.388,
                            "hourStat": {
                                "night": 0,
                                "day": 12,
                                "morning": 0
                            },
                            "callTimes": '',
                            "calledTimes": None,
                            "smsNotifications": None,
                            "activeShortest": 2,
                            "activeLongest": 10888,
                            "activeAverage": 3377,
                            "contactAmount": 3,
                            "month": "201612"
                        },
                        "M2": {
                            "month": "201611"
                        },
                        "M3": {
                            "month": "201610"
                        },
                        "M4": {
                            "distributionOfContacts": {
                                "1": "4",
                                "2": "3"
                            },
                            "dailyCallTimes": 0.334,
                            "hourStat": {
                                "night": 0,
                                "day": 10,
                                "morning": 0
                            },
                            "callTimes": 8,
                            "calledTimes": 20,
                            "smsNotifications": None,
                            "activeShortest": 6,
                            "activeLongest": 59391,
                            "activeAverage": 9786.223,
                            "contactAmount": 7,
                            "month": "201609"
                        },
                        "M5": {
                            "distributionOfContacts": {
                                "1": "18",
                                "2": "11",
                                "3": "2",
                                "5": "1",
                                "6": "1",
                                "10": "1"
                            },
                            "dailyCallTimes": 2.162,
                            "hourStat": {
                                "night": 6,
                                "day": 55,
                                "morning": 6
                            },
                            "callTimes": 3,
                            "calledTimes": 2,
                            "smsNotifications": None,
                            "activeShortest": 2,
                            "activeLongest": 156909,
                            "activeAverage": 10155.107,
                            "contactAmount": 34,
                            "month": "201608"
                        },
                        "T6": {
                            "distributionOfContacts": {
                                "1": "17",
                                "2": "14",
                                "3": "3",
                                "5": "1",
                                "7": "1",
                                "11": "1"
                            },
                            "dailyCallTimes": 0.446,
                            "hourStat": {
                                "night": 6,
                                "day": 65,
                                "morning": 6
                            },
                            "callTimes": 46,
                            "calledTimes": 31,
                            "smsNotifications": None,
                            "activeShortest": 2,
                            "activeLongest": 156909,
                            "activeAverage": 10876.54,
                            "contactAmount": 37,
                            "month": "halfyear"
                        }
                    }
                }
            },
            "apply_base": {
                "latitude": 145.23342,
                "name": "章撒",
                "mobile": "18920019799",
                "callback": "http://127.0.0.1/syph-re/api/credit/result/",
                "application_on": "2017-02-01 12:20:10",
                "contacts": 30,
                "card_id": "41140219890313739X",
                "longitudu": 23.45678
            }
        }},

    'mobile_activeness': {
        "trustutn_loan_phone": {
            "result": 0,
            "message": None,
            "res_data": {
                "tags": {
                    "18920019795__": {
                        "M0": {
                            "distributionOfContacts": {
                                "1": "16",
                                "2": "13",
                                "3": "1",
                                "4": "3",
                                "6": "2",
                                "7": "1",
                                "8": "1",
                                "10": "1",
                                "13": "2",
                                "22": "1",
                                "36": "1"
                            },
                            "dailyCallTimes": 8.901,
                            "hourStat": {
                                "night": 6,
                                "day": 158,
                                "morning": 14
                            },
                            "callTimes": '',
                            "calledTimes": '',
                            "smsNotifications": None,
                            "activeShortest": 1,
                            "activeLongest": 79236,
                            "activeAverage": 9615.126,
                            "contactAmount": 42,
                            "month": "201701"
                        },
                        "M1": {
                            "distributionOfContacts": {
                                "3": "1",
                                "4": "1",
                                "5": "1"
                            },
                            "dailyCallTimes": 0.388,
                            "hourStat": {
                                "night": 0,
                                "day": 12,
                                "morning": 0
                            },
                            "callTimes": 6,
                            "calledTimes": '',
                            "smsNotifications": None,
                            "activeShortest": 2,
                            "activeLongest": 10888,
                            "activeAverage": 3377,
                            "contactAmount": '',
                            "month": "201612"
                        },
                        "M6": {
                            "month": "201611"
                        },
                        "M3": {
                            "month": "201610"
                        },
                        "M4": {
                            "distributionOfContacts": {
                                "1": "4",
                                "2": "3"
                            },
                            "dailyCallTimes": 0.334,
                            "hourStat": {
                                "night": 0,
                                "day": 10,
                                "morning": 0
                            },
                            "callTimes": 8,
                            "calledTimes": 2,
                            "smsNotifications": None,
                            "activeShortest": 6,
                            "activeLongest": 59391,
                            "activeAverage": 9786.223,
                            "contactAmount": 7,
                            "month": "201609"
                        },
                        "M5": {
                            "distributionOfContacts": {
                                "1": "18",
                                "2": "11",
                                "3": "2",
                                "5": "1",
                                "6": "1",
                                "10": "1"
                            },
                            "dailyCallTimes": 2.162,
                            "hourStat": {
                                "night": 6,
                                "day": 55,
                                "morning": 6
                            },
                            "callTimes": 38,
                            "calledTimes": 9,
                            "smsNotifications": None,
                            "activeShortest": 2,
                            "activeLongest": 156909,
                            "activeAverage": 10155.107,
                            "contactAmount": 34,
                            "month": "201608"
                        },
                        "T6": {
                            "distributionOfContacts": {
                                "1": "17",
                                "2": "14",
                                "3": "3",
                                "5": "1",
                                "7": "1",
                                "11": "1"
                            },
                            "dailyCallTimes": 0.446,
                            "hourStat": {
                                "night": 6,
                                "day": 65,
                                "morning": 6
                            },
                            "callTimes": 46,
                            "calledTimes": 31,
                            "smsNotifications": None,
                            "activeShortest": 2,
                            "activeLongest": 156909,
                            "activeAverage": 10876.54,
                            "contactAmount": 37,
                            "month": "halfyear"
                        }
                    },
                    "18920019796__": {
                        "M0": {
                            "distributionOfContacts": {
                                "1": "16",
                                "2": "13",
                                "3": "1",
                                "4": "3",
                                "6": "2",
                                "7": "1",
                                "8": "1",
                                "10": "1",
                                "13": "2",
                                "22": "1",
                                "36": "1"
                            },
                            "dailyCallTimes": 8.901,
                            "hourStat": {
                                "night": 6,
                                "day": 158,
                                "morning": 14
                            },
                            "callTimes": '',
                            "calledTimes": '',
                            "smsNotifications": None,
                            "activeShortest": 1,
                            "activeLongest": 79236,
                            "activeAverage": 9615.126,
                            "contactAmount": 42,
                            "month": "201701"
                        },
                        "M1": {
                            "distributionOfContacts": {
                                "3": "1",
                                "4": "1",
                                "5": "1"
                            },
                            "dailyCallTimes": 0.388,
                            "hourStat": {
                                "night": 0,
                                "day": 12,
                                "morning": 0
                            },
                            "callTimes": '',
                            "calledTimes": 6,
                            "smsNotifications": None,
                            "activeShortest": 2,
                            "activeLongest": 10888,
                            "activeAverage": 3377,
                            "contactAmount": 8,
                            "month": "201612"
                        },
                        "M2": {
                            "month": "201611"
                        },
                        "M3": {
                            "month": "201610"
                        },
                        "M4": {
                            "distributionOfContacts": {
                                "1": "4",
                                "2": "3"
                            },
                            "dailyCallTimes": 0.334,
                            "hourStat": {
                                "night": 0,
                                "day": 10,
                                "morning": 0
                            },
                            "callTimes": 8,
                            "calledTimes": '',
                            "smsNotifications": None,
                            "activeShortest": 6,
                            "activeLongest": 59391,
                            "activeAverage": 9786.223,
                            "contactAmount": 7,
                            "month": "201609"
                        },
                        "M5": {
                            "distributionOfContacts": {
                                "1": "18",
                                "2": "11",
                                "3": "2",
                                "5": "1",
                                "6": "1",
                                "10": "1"
                            },
                            "dailyCallTimes": 2.162,
                            "hourStat": {
                                "night": 6,
                                "day": 55,
                                "morning": 6
                            },
                            "callTimes": 38,
                            "calledTimes": 9,
                            "smsNotifications": None,
                            "activeShortest": 2,
                            "activeLongest": 156909,
                            "activeAverage": 10155.107,
                            "contactAmount": 34,
                            "month": "201608"
                        },
                        "T6": {
                            "distributionOfContacts": {
                                "1": "17",
                                "2": "14",
                                "3": "3",
                                "5": "1",
                                "7": "1",
                                "11": "1"
                            },
                            "dailyCallTimes": 0.446,
                            "hourStat": {
                                "night": 6,
                                "day": 65,
                                "morning": 6
                            },
                            "callTimes": 46,
                            "calledTimes": 31,
                            "smsNotifications": None,
                            "activeShortest": 2,
                            "activeLongest": 156909,
                            "activeAverage": 10876.54,
                            "contactAmount": 37,
                            "month": "halfyear"
                        }
                    },
                    "18920019798_8a404758b8f8b87c70006b8e9f4614db_": {
                        "M0": {
                            "distributionOfContacts": {
                                "1": "16",
                                "2": "13",
                                "3": "1",
                                "4": "3",
                                "6": "2",
                                "7": "1",
                                "8": "1",
                                "10": "1",
                                "13": "2",
                                "22": "1",
                                "36": "1"
                            },
                            "dailyCallTimes": 8.901,
                            "hourStat": {
                                "night": 6,
                                "day": 158,
                                "morning": 14
                            },
                            "callTimes": 75,
                            "calledTimes": 13,
                            "smsNotifications": None,
                            "activeShortest": 1,
                            "activeLongest": 79236,
                            "activeAverage": 9615.126,
                            "contactAmount": 42,
                            "month": "201701"
                        },
                        "M1": {
                            "distributionOfContacts": {
                                "3": "1",
                                "4": "1",
                                "5": "1"
                            },
                            "dailyCallTimes": 0.388,
                            "hourStat": {
                                "night": 0,
                                "day": 12,
                                "morning": 0
                            },
                            "callTimes": '',
                            "calledTimes": None,
                            "smsNotifications": None,
                            "activeShortest": 2,
                            "activeLongest": 10888,
                            "activeAverage": 3377,
                            "contactAmount": 12,
                            "month": "201612"
                        },
                        "M2": {
                            "month": "201611"
                        },
                        "M3": {
                            "month": "201610"
                        },
                        "M4": {
                            "distributionOfContacts": {
                                "1": "4",
                                "2": "3"
                            },
                            "dailyCallTimes": 0.334,
                            "hourStat": {
                                "night": 0,
                                "day": 10,
                                "morning": 0
                            },
                            "callTimes": 8,
                            "calledTimes": 20,
                            "smsNotifications": None,
                            "activeShortest": 6,
                            "activeLongest": 59391,
                            "activeAverage": 9786.223,
                            "contactAmount": 7,
                            "month": "201609"
                        },
                        "M5": {
                            "distributionOfContacts": {
                                "1": "18",
                                "2": "11",
                                "3": "2",
                                "5": "1",
                                "6": "1",
                                "10": "1"
                            },
                            "dailyCallTimes": 2.162,
                            "hourStat": {
                                "night": 6,
                                "day": 55,
                                "morning": 6
                            },
                            "callTimes": 3,
                            "calledTimes": 2,
                            "smsNotifications": None,
                            "activeShortest": 2,
                            "activeLongest": 156909,
                            "activeAverage": 10155.107,
                            "contactAmount": 34,
                            "month": "201608"
                        },
                        "T6": {
                            "distributionOfContacts": {
                                "1": "17",
                                "2": "14",
                                "3": "3",
                                "5": "1",
                                "7": "1",
                                "11": "1"
                            },
                            "dailyCallTimes": 0.446,
                            "hourStat": {
                                "night": 6,
                                "day": 65,
                                "morning": 6
                            },
                            "callTimes": 46,
                            "calledTimes": 31,
                            "smsNotifications": None,
                            "activeShortest": 2,
                            "activeLongest": 156909,
                            "activeAverage": 10876.54,
                            "contactAmount": 37,
                            "month": "halfyear"
                        }
                    }
                }
            },
            "apply_base": {
                "latitude": 145.23342,
                "name": "章撒",
                "mobile": "18920019799",
                "callback": "http://127.0.0.1/syph-re/api/credit/result/",
                "application_on": "2017-02-01 12:20:10",
                "contacts": 30,
                "card_id": "41140219890313739X",
                "longitudu": 23.45678
            }
        }
    },

    'is_pingan_financial_shixin': {
        'data': {
            'name': '姓名 ',
            'idCard': '身份证 ',
            'phone': '手机号',
            'imsi': 'imsi',
            'imei': 'imei',
            'areaCode': '地区编号',
            'others': [
                {
                    'orgLostContact': '2015-09-11 09:49:52',  # 机构失联
                    'bankLostContact': '2015-08-23 11:23:50',  # 银行失联
                    'orgOverduePeriod': '',  # 机构逾期期数
                    'bankOverduePeriod': '',  # 银行逾期期数
                    'seriousOverdueTime': '2016-04-24 11:44:20',  # 最后一次严重逾期时间
                    'dunTelCallTime': '20160524',  # 最后一次催收电话的呼叫时间
                    'orgLitigation': '',  # 机构诉讼
                    'bankLitigation': '',  # 银行诉讼
                    'orgBlackList': [
                        {
                            'value': 'abc',  # 机构名称
                            'org_code': '123',  # 机构编号
                            'imsi': '135',  # 匹配的加密imsi
                        }
                    ],  # 列为黑名单的机构
                    'orgOneMonthOvedue': '',  # 开户30天有逾期
                    'matchType': '',  # 匹配查询的类型(phone/imei/imsi)
                    'matchValue': '',  # 匹配查询类型的值
                    'matchId': ''  # 匹配查询到的imsi的md5值
                }
            ]
        }
    },

    'company_addr_city_level': {
        "result": "00",
        "result_message": "检测通过或查询有记录",
        "content": {
            "status": "在营（开业）企业",
            "changerecords": [
                {
                    "change_date": "2015年03月06日",
                    "change_item": "经营范围变更",
                    "before_content": "矿产品(国家专控除外)、煤炭、钢材、木制品、建材、初级农产品（不含食品）、工程机械、机电设备、金属制品、摩托车、家用电器、文化用品、橡胶制品、化工产品（危险化学品及易制毒化学品除外）销售；普通货物进出口(法律禁止和国家专控除外限制的项目需取得许可证方可经营)。(依法须经批准的项目，经相关部门批准后方可开展经营活动)。",
                    "after_content": "矿产品(国家专控除外)、煤炭、钢材、木制品、建材、初级农产品、工程机械、机电设备、金属制品、摩托车、家用电器、文化用品、橡胶制品、化工产品（危险化学品及易制毒化学品除外）销售；普通货物进出口(法律禁止和国家专控除外限制的项目需取得许可证方可经营)。(依法须经批准的项目，经相关部门批准后方可开展经营活动)。"
                }
            ],
            "end_date": "-",
            "tp_deal_identifying": "",
            "scope": "矿产品(国家专控除外)、煤炭、钢材、木制品、建材、初级农产品、工程机械、机电设备、金属制品、摩托车、家用电器、文化用品、橡胶制品、化工产品（危险化学品及易制毒化学品除外）销售；普通货物进出口(法律禁止和国家专控除外限制的项目需取得许可证方可经营)。(依法须经批准的项目，经相关部门批准后方可开展经营活动)。",
            "term_start": "2009年09月08日",
            "address": '广州',
            "regist_capi": "1000 万人民币",
            "partners": [
                {
                    "real_capi_items": [
                        {
                            "invest_type": "货币",
                            "real_capi": "660 万人民币",
                            "real_capi_date": "2013-12-19"
                        }
                    ],
                    "name": "孙国庆",
                    "identify_no": "-",
                    "identify_type": "-",
                    "stock_type": "其他投资者",
                    "should_capi_items": [
                        {
                            "invest_type": "货币",
                            "should_capi_date": "2013-12-19",
                            "shoud_capi": "660 万人民币"
                        }
                    ]
                },
                {
                    "real_capi_items": [
                        {
                            "invest_type": "货币",
                            "real_capi": "340 万人民币",
                            "real_capi_date": "2013-12-19"
                        }
                    ],
                    "name": "孙磊",
                    "identify_no": "-",
                    "identify_type": "-",
                    "stock_type": "其他投资者",
                    "should_capi_items": [
                        {
                            "invest_type": "货币",
                            "should_capi_date": "2013-12-19",
                            "shoud_capi": "340 万人民币"
                        }
                    ]
                }
            ],
            "branches": [],
            "name": "山东南港国际贸易有限公司",
            "reg_no": "371102200011819",
            "oper_name": "孙国庆",
            "econ_kind": "有限责任公司(自然人投资或控股)",
            "term_end": "2019年09月07日",
            "start_date": "2009-09-08",
            "belong_org": "日照市东港区工商行政管理局",
            "check_date": "2015年03月06日",
            "employees": [
                {
                    "name": "孙国庆",
                    "job_title": "执行董事兼总经理"
                },
                {
                    "name": "孙磊",
                    "job_title": "监事"
                }
            ],
            "abnormal_items": []
        },
    },

    'folk': {
        "result": "00",
        "result_message": "检测通过或查询有记录",
        "content": {
            "id_card_name": "李..",
            "marital_status": "10",
            "id_card_code": "1306251....",
            "verify": "一致",
            "company": "暂无",
            "nation": "汉族",
            "former_name": "",
            "native_place": "河北省保定市徐水县",
            "birthday": "1988-09-10",
            "birth_place": "河北省保定市徐水县",
            "sex_id": "2",
            "photo": "",
            "education": "大学本科（简称'大学'）",
            "address": "河北省保定市徐水区高林村镇"
        }
    },

    'marital_status': {
        "result": "00",
        "result_message": "检测通过或查询有记录",
        'content': {
            'id_card_name': '李..',
            'marital_status': '23',
            'id_card_code': '1306251....',
            'verify': '一致',
            'company': '暂无',
            'nation': '汉族',
            'former_name': '',
            'native_place': '河北省保定市徐水县',
            'birthday': '1988-09-10',
            'birth_place': '河北省保定市徐水县',
            'sex_id': '2',
            'photo': '',
            'education': '大学本科（简称"大学"）',
            'address': '河北省保定市徐水区高林村镇'
        }
    },

    'gender': {
        "result": "00",
        "result_message": "检测通过或查询有记录",
        "content": {
            "constellation": "水瓶座",
            "age": 24,
            "home_address": "江西-九江",
            "sex": "女"
        },
    },

    'mobile_area_city_level': {
        "result": "00",
        "result_message": "检测通过或查询有记录",
        "content": {
            "mobile_area": "北京市",
        },
    },

    'register_city_level': {
        "result": "00",
        "result_message": "检测通过或查询有记录",
        "content": {
            "constellation": "水瓶座",
            "age": 24,
            "home_address": "江西-九江",
            "sex": "男"
        },
    },

    'max_flight_area': {
        "result": "00",
        "result_message": "检测通过或查询有记录",
        "content": {
            "id_card_name": "吴*",
            "id_card_code": "513722198908***43X",
            "flight_times": 2,
            "flight_month": "201502",
            "flight_max": 2,
            "average_discount": 100,
            "business_class_count": 0,
            "executive_class_count": 0,
            "tourist_class_count": 2,
            "from_city": "广元1次,北京1次,",
            "destination_city ": "北京1次,广元1次,",
            "inland_count": 2,
            "international_count": 3,
            "free_count": 0,
            "average_price": 1340.00,
            "delay_time": 40,
            "average_delay_time": 20,
            "average_ticket_day": 68,
            "last_date": "20150228",
            "last_from_city": "广元",
            "last_destination_city": "北京",
            "total_distance": 2810,
        }
    },

    'max_flight_class': {
        "result": "00",
        "result_message": "检测通过或查询有记录",
        "content": {
            "id_card_name": "吴*",
            "id_card_code": "513722198908***43X",
            "flight_times": 2,
            "flight_month": "201502",
            "flight_max": 2,
            "average_discount": 100,
            "business_class_count": 0,
            "executive_class_count": 0,
            "tourist_class_count": 2,
            "from_city": "广元1次,北京1次,",
            "destination_city ": "北京1次,广元1次,",
            "inland_count": 2,
            "international_count": 0,
            "free_count": 0,
            "average_price": 1340.00,
            "delay_time": 40,
            "average_delay_time": 20,
            "average_ticket_day": 68,
            "last_date": "20150228",
            "last_from_city": "广元",
            "last_destination_city": "北京",
            "total_distance": 2810,
        },
    },

    'airfare_sum_12': {
        "result": "00",
        "result_message": "检测通过或查询有记录",
        "content": {
            "id_card_name": "吴*",
            "id_card_code": "513722198908***43X",
            "flight_times": 2,
            "flight_month": "201502",
            "flight_max": 2,
            "average_discount": 100,
            "business_class_count": 0,
            "executive_class_count": 0,
            "tourist_class_count": 2,
            "from_city": "广元1次,北京1次,",
            "destination_city ": "北京1次,广元1次,",
            "inland_count": 2,
            "international_count": 0,
            "free_count": 0,
            "average_price": 1340.00,
            "delay_time": 40,
            "average_delay_time": 20,
            "average_ticket_day": 68,
            "last_date": "20150228",
            "last_from_city": "广元",
            "last_destination_city": "北京",
            "total_distance": 2810,
        },
    },

    'jiuyao_multi_loan_denied_count': {
        'multi_loan_91': {
            'loanInfos': [
                {
                    'borrowType': 1,
                    'borrowState': 2,
                    'borrowAmount': 3,
                    'contractDate': 1488079200000,
                    'loanPeriod': 24,
                    'repayState': 7,
                    'arrearsAmount': 0,
                    'companyCode': 'P2P4HJK0000100010'
                },
                {
                    'borrowType': 1,
                    'borrowState': 1,
                    'borrowAmount': 3,
                    'contractDate': 1487779200000,
                    'loanPeriod': 24,
                    'repayState': 7,
                    'arrearsAmount': 0,
                    'companyCode': 'P2P4HJK0000100011'
                },
                {
                    'borrowType': 1,
                    'borrowState': 1,
                    'borrowAmount': 3,
                    'contractDate': 1343779200000,
                    'loanPeriod': 24,
                    'repayState': 7,
                    'arrearsAmount': 0,
                    'companyCode': 'P2P4HJK0000100011'
                }
            ]
        }
    },

    'contacts': {
        "apply_data": {
        'product_code': '890wefjf320if0i302f0j3f0f',
        'apply_id': 'APPLY20161011111111890934',
        'callback': 'http://10.20.1.110/api/credit/result/',
        'name': '张三',
        'card_id': '411402198002039872',
        'mobile': '18989821092',
        'longitudu': 23.45678,
        'latitude': 145.23342,
        'contacts': 30,
        'application_on': '2017-02-01 12:20:10'
    }
    },

    'jiuyao_multi_loan_m2_count': {
        'multi_loan_91': {
            'loanInfos': [
                {
                    'borrowType': 1,
                    'borrowState': 2,
                    'borrowAmount': 3,
                    'contractDate': 1343779200000,
                    'loanPeriod': 24,
                    'repayState': 8,
                    'arrearsAmount': 0,
                    'companyCode': 'P2P4HJK0000100010'
                },
                {
                    'borrowType': 1,
                    'borrowState': 1,
                    'borrowAmount': 3,
                    'contractDate': 1343779200000,
                    'loanPeriod': 24,
                    'repayState': 6,
                    'arrearsAmount': 0,
                    'companyCode': 'P2P4HJK0000100011'
                },
                {
                    'borrowType': 1,
                    'borrowState': 1,
                    'borrowAmount': 3,
                    'contractDate': 1343779200000,
                    'loanPeriod': 24,
                    'repayState': 5,
                    'arrearsAmount': 0,
                    'companyCode': 'P2P4HJK0000100011'
                }
            ]
        }
    },

    'is_unclear_loan': {
        'loan_history': {
            "status": 1,
            "message": "操作成功",
            "res_data": {
                "is_unclear_loan": 2,
            },
        }
    },

    'mobile_area_city_code': {
        'mobile_local': {
            'result': '00',
            'result_message': '检测通过或查询有记录',
            'content': {
                'mobile_area': '唐山市',
            },
        }
    },

    'gps_city_code': {
        'geo_location': {
            "content": {
                "status": 0,
                "result": {
                    "location": {
                        "lng": 114.23075168099999,
                        "lat": 29.57908754899005
                    },
                    "formatted_address": "湖北省咸宁市崇阳县G56(杭瑞高速)",
                    "business": "",
                    "addressComponent": {
                        "country": "中国",
                        "country_code": 0,
                        "province": "湖北省",
                        "city": "咸宁市",
                        "district": "崇阳县",
                        "adcode": "421223",
                        "street": "G56(杭瑞高速)",
                        "street_number": "",
                        "direction": "",
                        "distance": ""
                    },
                    "pois": [],
                    "poiRegions": [],
                    "sematic_description": "大屋沈家南210米",
                    "cityCode": 362
                }
            },
            "result_message": "检测通过或查询有记录",
            "result": "00"
        }
    },

    'cur_work_status': {
        'portrait_data': {
            "product_code": "string",
            "name": "string",
            "card_id": "string",
            "mobile": "string",
            "email": "string",
            "registration_on": "2016-10-01 12:20:10",
            "city_code": "string",
            "city_name": "string",
            "now_indust_code": "string",
            "now_indust_name": "string",
            "work_age": 0,
            "complete_degree": 0,
            "cur_work_status": u"在职,急寻新工作",
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
                },
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
    },

    'now_workplace_code': {
        'portrait_data': {
            "product_code": "string",
            "name": "string",
            "card_id": "string",
            "mobile": "string",
            "email": "string",
            "registration_on": "2016-10-01 12:20:10",
            "city_code": "string",
            "city_name": "string",
            "now_indust_code": "string",
            "now_indust_name": "string",
            "work_age": 0,
            "complete_degree": 0,
            "cur_work_status": u"在职,急寻新工作",
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
                    "work_end": "999999",
                    "industry": '30',
                    "industry_name": "string",
                    "dq": "string",
                    "dq_name": "string"
                },
                {
                    "title": "string",
                    "has_certified": "string",
                    "certified_num": 0,
                    "comp_name": "string",
                    "months": 0,
                    "salary": 0,
                    "work_start": "string",
                    "work_end": "201508",
                    "industry": '120',
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
    },

    'work_time': {
        'portrait_data': {
            "product_code": "string",
            "name": "string",
            "card_id": "string",
            "mobile": "string",
            "email": "string",
            "registration_on": "2016-10-01 12:20:10",
            "city_code": "string",
            "city_name": "string",
            "now_indust_code": "string",
            "now_indust_name": "string",
            "work_age": 0,
            "complete_degree": 0,
            "cur_work_status": u"在职,急寻新工作",
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
                    "work_start": "201605",
                    "work_end": "999999",
                    "industry": '30',
                    "industry_name": "string",
                    "dq": "string",
                    "dq_name": "string"
                },
                {
                    "title": "string",
                    "has_certified": "string",
                    "certified_num": 0,
                    "comp_name": "string",
                    "months": 0,
                    "salary": 0,
                    "work_start": "",
                    "work_end": "201604",
                    "industry": '120',
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
    },

    'is_jiuyao_multi_loan': {'loanInfos': [
        {
            'borrowType': 1,
            'borrowState': 2,
            'borrowAmount': 3,
            'contractDate': 1487224222000,
            'loanPeriod': 24,
            'repayState': 7,
            'arrearsAmount': 0,
            'companyCode': 'P2P4HJK0000100010'
        },
        {
            'borrowType': 1,
            'borrowState': 1,
            'borrowAmount': 3,
            'contractDate': 1487224222000,
            'loanPeriod': 24,
            'repayState': 7,
            'arrearsAmount': 0,
            'companyCode': 'P2P4HJK0000100011'
        },
        {
            'borrowType': 1,
            'borrowState': 1,
            'borrowAmount': 3,
            'contractDate': '',
            'loanPeriod': 24,
            'repayState': 7,
            'arrearsAmount': 0,
            'companyCode': 'P2P4HJK0000100011'
        }
    ]},

    'loan_infos': {'loanInfos': [
        {
            'borrowType': 1,
            'borrowState': 2,
            'borrowAmount': 3,
            'contractDate': 1487224222000,
            'loanPeriod': 24,
            'repayState': 7,
            'arrearsAmount': 0,
            'companyCode': 'P2P4HJK0000100010'
        },
        {
            'borrowType': 1,
            'borrowState': 1,
            'borrowAmount': 3,
            'contractDate': 1487224222000,
            'loanPeriod': 24,
            'repayState': 7,
            'arrearsAmount': 0,
            'companyCode': 'P2P4HJK0000100011'
        },
        {
            'borrowType': 1,
            'borrowState': 1,
            'borrowAmount': 3,
            'contractDate': '',
            'loanPeriod': 24,
            'repayState': 7,
            'arrearsAmount': 0,
            'companyCode': 'P2P4HJK0000100011'
        }
    ]},

    'is_mobile_black': {
        "apply_data": {
            'product_code': '890wefjf320if0i302f0j3f0f',
            'apply_id': 'APPLY20161011111111890934',
            'callback': 'http://10.20.1.110/api/credit/result/',
            'name': '张三',
            'card_id': '411402198002039872',
            'mobile': '18989821092',
            'longitudu': 23.45678,
            'latitude': 145.23342,
            'contacts': 30,
            'application_on': '2017-02-01 12:20:10'
        },
        "trustutn_loan_phone": {
            "result": 0,
            "message": "",
            "data": {
                "commonContacts": {
                    "18920019795 | 17720038301": {
                        "M0": {
                            "count": "1",
                            "month": "201701"
                        },
                        "M1": {
                            "count": "1",
                            "month": "201612"},
                        "M2": {
                            "count": "0",
                            "month": "201611"
                        },
                        "M3": {
                            "count": "0",
                            "month": "201610"
                        },
                        "M4": {
                            "count": "1",
                            "month": "201609"
                        },
                        "M5": {
                            "count": "0",
                            "month": "201608"},
                        "T6": {
                            "97bf35e9449cbea50088c17f97af6049": {
                                "18920019795": {
                                    "hourStat": {
                                        "night": 0,
                                        "day": 4,
                                        "morning": 0
                                    },
                                    "dailyCallTimes": 0.024,
                                    "rateOfCallPerAve": 0.0,
                                    "callTimes": 0,
                                    "calledTimes": 4,
                                    "earliestTime": 1483142287000,
                                    "latestTime": 1483142354000,
                                    "periodicity": False
                                },
                                "17720038301": {
                                    "hourStat": {"night": 0,
                                                 "day": 28,
                                                 "morning": 9
                                                 },
                                    "dailyCallTimes": 0.214,
                                    "rateOfCallPerAve": 0.0,
                                    "callTimes": 18,
                                    "calledTimes": 19,
                                    "earliestTime": 1472722765000,
                                    "latestTime": 1484717040000,
                                    "periodicity": False
                                }
                            }
                        }
                    }
                },
                "directCall": {
                    "17720038301__": {
                        "M0": {
                            "hourStat": {
                                "night": 0,
                                "day": 25,
                                "morning": 8
                            },
                            "dailyCallTimes": 1.65,
                            "rateOfCallPerAve": 0.0,
                            "callTimes": 17,
                            "calledTimes": 16,
                            "earliestTime": 1483295919000,
                            "latestTime": 1484717040000,
                            "month": "201701",
                            "periodicity": False
                        },
                        "M1": {
                            "hourStat": {
                                "night": 0,
                                "day": 0,
                                "morning": 0
                            },
                            "dailyCallTimes": 0.0,
                            "rateOfCallPerAve": 0.0,
                            "callTimes": 0,
                            "calledTimes": 0,
                            "earliestTime": 1484895878756,
                            "latestTime": 1484895878756,
                            "month": "201612",
                            "periodicity": False
                        },
                        "M2": {
                            "hourStat": {
                                "night": 0,
                                "day": 0,
                                "morning": 0
                            },
                            "dailyCallTimes": 0.0,
                            "rateOfCallPerAve": 0.0,
                            "callTimes": 0,
                            "calledTimes": 0,
                            "earliestTime": 1484895878756,
                            "latestTime": 1484895878756,
                            "month": "201611",
                            "periodicity": False},
                        "M3": {
                            "hourStat": {
                                "night": 0,
                                "day": 0,
                                "morning": 0
                            },
                            "dailyCallTimes": 0.0,
                            "rateOfCallPerAve": 0.0,
                            "callTimes": 0,
                            "calledTimes": 0,
                            "earliestTime": 1484895878756,
                            "latestTime": 1484895878756,
                            "month": "201610",
                            "periodicity": False},
                        "M4": {
                            "hourStat": {
                                "night": 0,
                                "day": 1,
                                "morning": 0
                            },
                            "dailyCallTimes": 0.034,
                            "rateOfCallPerAve": 0.0,
                            "callTimes": 1,
                            "calledTimes": 0,
                            "earliestTime": 1472722765000,
                            "latestTime": 1472722765000,
                            "month": "201609",
                            "periodicity": False},
                        "M5": {
                            "hourStat": {
                                "night": 0,
                                "day": 0,
                                "morning": 0
                            },
                            "dailyCallTimes": 0.0,
                            "rateOfCallPerAve": 0.0,
                            "callTimes": 0,
                            "calledTimes": 0,
                            "earliestTime": 1484895878756,
                            "latestTime": 1484895878756,
                            "month": "201608",
                            "periodicity": False},
                        "T6": {
                            "hourStat": {
                                "night": 0,
                                "day": 26,
                                "morning": 8
                            },
                            "dailyCallTimes": 0.197,
                            "rateOfCallPerAve": 0.0,
                            "callTimes": 18,
                            "calledTimes": 16,
                            "earliestTime": 1472722765000,
                            "latestTime": 1484717040000,
                            "periodicity": False
                        }
                    }
                },
                "grayscale": {
                    "18920019795__819020148A8F03B7CE75B530FCBD08E3": {
                        "M0": {
                            "NBFI": {
                                "contactTimes": 1,
                                "orgNumbs": 1,
                                "earliestTime": "20170108",
                                "latestTime": "20170108"
                            },
                            "bank": '',
                            "collectionAgency": '',
                            "month": "201701"
                        },
                        "M1": {
                            "month": "201612"
                        },
                        "M2": {
                            "month": "201611"
                        },
                        "M3": {
                            "month": "201610"
                        },
                        "M4": {
                            "month": "201609"
                        },
                        "M5": {
                            "NBFI": {
                                "contactTimes": 1,
                                "orgNumbs": 1,
                                "earliestTime": "20160824",
                                "latestTime": "20160824"
                            },
                            "bank": '',
                            "collectionAgency": '',
                            "month": "201608"
                        }
                    }
                },
                "interactCommons": {

                },
                "tags":
                    {"18989821092__5975452a1caf27d58030b62de41a92a0":
                        {
                            "M0":
                                {"distributionOfContacts": {
                                    "3": "1",
                                    "2": "13",
                                    "1": "16",
                                    "10": "1",
                                    "7": "1",
                                    "6": "2",
                                    "4": "3",
                                    "22": "1",
                                    "36": "1",
                                    "8": "1",
                                    "13": "2"
                                },
                                    "dailyCallTimes": 8.901,
                                    "hourStat": {
                                        "night": 6,
                                        "day": 158,
                                        "morning": 14
                                    },
                                    "callTimes": 75.0,
                                    "calledTimes": 103.0,
                                    "smsNotifications": '',
                                    "activeShortest": 1.0,
                                    "activeLongest": 79236.0,
                                    "activeAverage": 9615.126,

                                    "month": "201701"
                                },
                            "M1": {
                                "distributionOfContacts": {
                                    "3": "1",
                                    "5": "1",
                                    "4": "1"
                                },
                                "dailyCallTimes": 0.388,
                                "hourStat": {
                                    "night": 0,
                                    "day": 12,
                                    "morning": 0
                                },
                                "callTimes": 6.0,
                                "calledTimes": 6.0,
                                "smsNotifications": '',
                                "activeShortest": 2.0,
                                "activeLongest": 10888.0,
                                "activeAverage": 3377.0,

                                "month": "201612"
                            },
                            "M2": {
                                "month": "201611"
                            },
                            "M3": {
                                "month": "201610"
                            },
                            "M4": {
                                "distributionOfContacts":
                                    {
                                        "2": "3",
                                        "1": "4"
                                    },
                                "dailyCallTimes": 0.334,
                                "hourStat": {
                                    "night": 0,
                                    "day": 10,
                                    "morning": 0
                                },
                                "callTimes": 8.0,
                                "calledTimes": 2.0,
                                "smsNotifications": '',
                                "activeShortest": 6.0,
                                "activeLongest": 59391.0,
                                "activeAverage": 9786.223,
                                "contactAmount": 20.0,
                                "month": "201609"
                            },
                            "M5": {
                                "distributionOfContacts": {
                                    "3": "2",
                                    "2": "11",
                                    "1": "18",
                                    "10": "1",
                                    "6": "1",
                                    "5": "1"
                                },
                                "dailyCallTimes": 2.162,
                                "hourStat": {
                                    "night": 6,
                                    "day": 55,
                                    "morning": 6
                                },
                                "callTimes": 38.0,
                                "calledTimes": 29.0,
                                "smsNotifications": '',
                                "activeShortest": 2.0,
                                "activeLongest": 156909.0,
                                "activeAverage": 10155.107,
                                "contactAmount": 30.0,
                                "month": "201608"
                            },
                            "T6": {
                                "distributionOfContacts": {
                                    "3": "3",
                                    "2": "14",
                                    "1": "17",
                                    "7": "1",
                                    "5": "1",
                                    "11": "1"
                                },
                                "dailyCallTimes": 0.446,
                                "hourStat": {
                                    "night": 6,
                                    "day": 65,
                                    "morning": 6
                                },
                                "callTimes": 46.0,
                                "calledTimes": 31.0,
                                "smsNotifications": '',
                                "activeShortest": 2.0,
                                "activeLongest": 156909.0,
                                "activeAverage": 10876.54,
                                "contactAmount": 37.0,
                                "month": "halfyear"
                            }
                        },
                        "18989821092__a":
                            {
                                "M0":
                                    {"distributionOfContacts": {
                                        "3": "1",
                                        "2": "13",
                                        "1": "16",
                                        "10": "1",
                                        "7": "1",
                                        "6": "2",
                                        "4": "3",
                                        "22": "1",
                                        "36": "1",
                                        "8": "1",
                                        "13": "2"
                                    },
                                        "dailyCallTimes": 8.901,
                                        "hourStat": {
                                            "night": 6,
                                            "day": 158,
                                            "morning": 14
                                        },
                                        "callTimes": 75.0,
                                        "calledTimes": 103.0,
                                        "smsNotifications": '',
                                        "activeShortest": 1.0,
                                        "activeLongest": 79236.0,
                                        "activeAverage": 9615.126,
                                        "contactAmount": 42.0,
                                        "month": "201701"
                                    },
                                "M1": {
                                    "distributionOfContacts": {
                                        "3": "1",
                                        "5": "1",
                                        "4": "1"
                                    },
                                    "dailyCallTimes": 0.388,
                                    "hourStat": {
                                        "night": 0,
                                        "day": 12,
                                        "morning": 0
                                    },
                                    "callTimes": 6.0,
                                    "calledTimes": 6.0,
                                    "smsNotifications": '',
                                    "activeShortest": 2.0,
                                    "activeLongest": 10888.0,
                                    "activeAverage": 3377.0,
                                    "contactAmount": 4.0,
                                    "month": "201612"
                                },
                                "M2": {
                                    "month": "201611"
                                },
                                "M3": {
                                    "month": "201610"
                                },
                                "M4": {
                                    "distributionOfContacts":
                                        {
                                            "2": "3",
                                            "1": "4"
                                        },
                                    "dailyCallTimes": 0.334,
                                    "hourStat": {
                                        "night": 0,
                                        "day": 10,
                                        "morning": 0
                                    },
                                    "callTimes": 8.0,
                                    "calledTimes": 2.0,
                                    "smsNotifications": '',
                                    "activeShortest": 6.0,
                                    "activeLongest": 59391.0,
                                    "activeAverage": 9786.223,
                                    "contactAmount": 7.0,
                                    "month": "201609"
                                },
                                "M5": {
                                    "distributionOfContacts": {
                                        "3": "2",
                                        "2": "11",
                                        "1": "18",
                                        "10": "1",
                                        "6": "1",
                                        "5": "1"
                                    },
                                    "dailyCallTimes": 2.162,
                                    "hourStat": {
                                        "night": 6,
                                        "day": 55,
                                        "morning": 6
                                    },
                                    "callTimes": 38.0,
                                    "calledTimes": 29.0,
                                    "smsNotifications": '',
                                    "activeShortest": 2.0,
                                    "activeLongest": 156909.0,
                                    "activeAverage": 10155.107,
                                    "contactAmount": 34.0,
                                    "month": "201608"
                                },
                                "T6": {
                                    "distributionOfContacts": {
                                        "3": "3",
                                        "2": "14",
                                        "1": "17",
                                        "7": "1",
                                        "5": "1",
                                        "11": "1"
                                    },
                                    "dailyCallTimes": 0.446,
                                    "hourStat": {
                                        "night": 6,
                                        "day": 65,
                                        "morning": 6
                                    },
                                    "callTimes": 46.0,
                                    "calledTimes": 31.0,
                                    "smsNotifications": '',
                                    "activeShortest": 2.0,
                                    "activeLongest": 156909.0,
                                    "activeAverage": 10876.54,
                                    "contactAmount": 30.0,
                                    "month": "halfyear"
                                }
                            },
                        "13820019795_8a404758b8f8b87c70006b8e9f4614db_": {
                            "M0": {
                                "distributionOfContacts": {
                                    "3": "1",
                                    "2": "13",
                                    "1": "16",
                                    "10": "1",
                                    "7": "1",
                                    "6": "2",
                                    "4": "3",
                                    "22": "1",
                                    "36": "1",
                                    "8": "1",
                                    "13": "2"
                                },
                                "dailyCallTimes": 8.901,
                                "hourStat": {
                                    "night": 6,
                                    "day": 158,
                                    "morning": 14
                                },
                                "callTimes": 75.0,
                                "calledTimes": 103.0,
                                "smsNotifications": '',
                                "activeShortest": 1.0,
                                "activeLongest": 79236.0,
                                "activeAverage": 9615.126,
                                "contactAmount": 19.0,
                                "month": "201701"
                            },
                            "M1": {
                                "distributionOfContacts": {
                                    "3": "1",
                                    "5": "1",
                                    "4": "1"
                                },
                                "dailyCallTimes": 0.388,
                                "hourStat":
                                    {"night": 0,
                                     "day": 12,
                                     "morning": 0
                                     },
                                "callTimes": 6.0,
                                "calledTimes": 6.0,
                                "smsNotifications": '',
                                "activeShortest": 2.0,
                                "activeLongest": 10888.0,
                                "activeAverage": 3377.0,
                                "contactAmount": 3.0,
                                "month": "201612"
                            },
                            "M2": {
                                "month": "201611"
                            },
                            "M3": {
                                "month": "201610"
                            },
                            "M4": {
                                "distributionOfContacts": {
                                    "2": "3", "1": "4"
                                },
                                "dailyCallTimes": 0.334,
                                "hourStat": {
                                    "night": 0,
                                    "day": 10,
                                    "morning": 0
                                },
                                "callTimes": 8.0,
                                "calledTimes": 2.0,
                                "smsNotifications": '',
                                "activeShortest": 6.0,
                                "activeLongest": 59391.0,
                                "activeAverage": 9786.223,
                                "contactAmount": 7.0,
                                "month": "201609"
                            },
                            "M5": {
                                "distributionOfContacts": {
                                    "3": "2",
                                    "2": "11",
                                    "1": "18",
                                    "10": "1",
                                    "6": "1",
                                    "5": "1"
                                },
                                "dailyCallTimes": 2.162,
                                "hourStat": {
                                    "night": 6,
                                    "day": 55,
                                    "morning": 6
                                },
                                "callTimes": 38.0,
                                "calledTimes": 29.0,
                                "smsNotifications": '',
                                "activeShortest": 2.0,
                                "activeLongest": 156909.0,
                                "activeAverage": 10155.107,

                                "month": "201608"
                            },
                            "T6": {
                                "distributionOfContacts": {
                                    "3": "3",
                                    "2": "14",
                                    "1": "17",
                                    "7": "1",
                                    "5": "1",
                                    "11": "1"
                                },
                                "dailyCallTimes": 0.446,
                                "hourStat": {"night": 6,
                                             "day": 65,
                                             "morning": 6
                                             },
                                "callTimes": 46.0,
                                "calledTimes": 31.0,
                                "smsNotifications": '',
                                "activeShortest": 2.0,
                                "activeLongest": 156909.0,
                                "activeAverage": 10876.54,
                                "contactAmount": 37.0,
                                "month": "halfyear"
                            }
                        }
                    }

            }
        }
    },

    'pingan_multi_loan_infos': {
        "result": 0,
        "message": None,
        "data": {
            "record": [{
                "matchType": "idCard",
                "matchValue": "340825198609101051",
                "matchId": "92a297643fdcd96644cf30942b8a2e5f",
                "classification": [
                    {
                        "M3": {
                            "bankCredit": None,
                            "otherLoan": {
                                "orgNums": 12,
                                "recordNums": 1,
                                "maxAmount": "(1000, 2000]",
                                "longestDays": "6"
                            },
                            "otherCredit": None,
                            "bankLoan": None
                        }
                    },
                    {
                        "M6": {
                            "bankCredit": None,
                            "otherLoan": {
                                "orgNums": 1,
                                "recordNums": 1,
                                "maxAmount": "(1000, 2000]",
                                "longestDays": "1"
                            },
                            "otherCredit": None,
                            "bankLoan": None
                        }
                    },
                    {
                        "M9": {
                            "bankCredit": None,
                            "otherLoan": {
                                "orgNums": 1,
                                "recordNums": 2,
                                "maxAmount": "(1000, 2000]",
                                "longestDays": "1"
                            },
                            "otherCredit": None,
                            "bankLoan": None
                        }
                    },
                    {
                        "M24": {
                            "bankCredit": None,
                            "otherLoan": {
                                "orgNums": 1,
                                "recordNums": 1,
                                "maxAmount": "(1000, 2000]",
                                "longestDays": "1"
                            },
                            "otherCredit": None,
                            "bankLoan": None
                        }
                    }
                ]
            }
            ],
            "phone": "15821732543",
            "imei": "",
            "imsi": ""}
    },

    "industry_change_count": {
        "product_code": "string",
        "name": "string",
        "card_id": "string",
        "mobile": "string",
        "email": "string",
        "registration_on": "2016-10-01 12:20:10",
        "city_code": "string",
        "city_name": "string",
        "now_indust_code": "string",
        "now_indust_name": "string",
        "work_age": 0,
        "complete_degree": 0,
        "cur_work_status": "string",
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
                "work_start": "201605",
                "work_end": "201607",
                "industry": "数云普惠",
                "industry_name": "string",
                "dq": "string",
                "dq_name": "string"
            },
            {
                "title": "string",
                "has_certified": "string",
                "certified_num": 0,
                "comp_name": "string",
                "months": 0,
                "salary": 0,
                "work_start": "201503",
                "work_end": "201601",
                "industry": "猎聘",
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
                "degree": "5",
                "degree_name": "string",
                "tz": 0
            },
            {
                "school": "string",
                "start": "string",
                "end": "string",
                "degree": "30",
                "degree_name": "string",
                "tz": 1
            }
        ]
    },

    "mobile_identity": {
        'telecom_mobile_identity_s': {
            "result": "11",
            "result_message": "检测通过或查询有记录",
            "content": {}
        }
    }
}


def test(data):
    for feature_name, datas in data.items():
        fecture_obj = FeatureProcess(feature_name, datas)
        result = fecture_obj.run()
        print result


if __name__ == '__main__':
    data = {'mobile_identity': data['mobile_identity']}
    test(data)
