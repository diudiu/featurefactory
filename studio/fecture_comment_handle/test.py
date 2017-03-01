# -*- coding:utf-8 -*-

from featrue_process import FeatureProcess

data = {
    'age': {'personal_info': {
        'status': u'00',
        'message': '',
        'content': {
            'constellation': '水瓶座',
            'age': 10,
            'home_address': '江西 - 九江',
            'sex': '男',
        },
    }},
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
                "mobile": "18920019795",
                "callback": "http://127.0.0.1/syph-re/api/credit/result/",
                "application_on": "2017-02-01 12:20:10",
                "contacts": 30,
                "card_id": "41140219890313739X",
                "longitudu": 23.45678
            }
        }},
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
        }},
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

}


def test():
    for feature_name, datas in data.items():
        fecture_obj = FeatureProcess(feature_name, datas)
        result = fecture_obj.run()
        print result


if __name__ == '__main__':
    # data = {'airfare_sum_12': data['airfare_sum_12']}
    test()
