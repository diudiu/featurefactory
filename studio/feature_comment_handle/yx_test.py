# -*- coding:utf-8 -*-

from featrue_process import FeatureProcess

data = {
    "is_netsky_multi_loan": {
        "result": "00",
        "result_message": "检测通过或查询有记录",
        "content": [
            {
                "type": "黑名单",
                "date": "",
                "desc": "黑名单_网贷黑名单_网贷帮手",
                "originalRet": {
                    "no": 0,
                    "url": "",
                    "abstract": "",
                    "title": "",
                    "class": "",
                    "search_type": "",
                    "search_word": ""
                }
            }
        ]
    },

    "is_skyeye_black": {
        "result": "00",
        "result_message": "检测通过或查询有记录",
        "content": [
            {
                "date": "0000-00-00",
                "orginalRet": {
                    "illegal_type": "",
                    "id_card_name": "楚亮",
                    "home_address": "湖南省湘潭市雨湖区人民路２４号",
                    "user_type": "",
                    "sex": 0,
                    "source_email": None,
                    "black_level": "1",
                    "execute_status": "",
                    "id": 15851,
                    "borrow_amount": "4000.00",
                    "court": "",
                    "source_mobile": "13873275214",
                    "case_detail": "",
                    "company_name": "",
                    "performed_part": "",
                    "publish_source": "拍拍贷",
                    "source_card": None,
                    "qq": None,
                    "publish_time": "0000-00-00",
                    "id_card_code": "430321198402069014",
                    "over_due_days": 0,
                    "mobile_equipment_number": "",
                    "crawl_time": "2015-06-09",
                    "case_code": "",
                    "arrears_limit": "0.00",
                    "fixed_telephone": "0731-57894381",
                    "over_due_nums": 0,
                    "mobile": "13873275214",
                    "email": "419650792@qq.com",
                    "publish_date": "",
                    "unperform_part": "",
                    "company_address": "",
                    "source_equipment_number": None
                },
                "type": "拍拍贷",
                "desc": "楚亮"
            }
        ],
    },

    "is_court_shixin": {
        "result_message": "检测通过或查询有记录",
        "result": "00",
        "content": {
            "shixin_list": [
                {
                    "province": "浙江",
                    "entity_id": "676150594",
                    "publish_time": "2014-09-16",
                    "entity_name": "上虞市巨**设备有限公司",
                    "shixin_type": "其他有履行能力而拒不履行生效法律文书确定义务",
                    "sex": "",
                    "case_create_time": "2013-12-31",
                    "file_id": "(2013)绍虞商初字第00766号",
                    "execute_status": "全部未履行",
                    "case_code": "(2014)绍虞执民字第00243号",
                    "obligation": "支付款项427408元",
                    "court": "上虞市人民法院",
                    "legal_person_name": "徐玉蓉",
                    "age": "",
                    "case_type": "法人或其他组织",
                    "executor_unit": "绍兴上虞法院"
                },
            ]
        }
    },

    "is_net_black": {
        "result": "00",
        "result_message": "检测通过或查询有记录",
        "content": {
            "data_list": [{
                "loan_date": "",
                "over_date": "",
                "id_card_code": "612501198407110021",
                "enterprise_name": "",
                "id_card_name": "徐娟",
                "state": "",
                "mobile": "",
                "gender": "女",
                "age": "",
                "over_amount": "3300",
                "publish_source": "拍拍贷",
                "loan_amount": "",
                "publish_date": "2013-06-07",
                "address": "",
                "enterprise_address": "",
                "email": "",
                "loan_term": ""
            },
                {
                    "loan_date": "2010-09-09",
                    "over_date": "",
                    "id_card_code": "612501198407110021",
                    "enterprise_name": "",
                    "id_card_name": "徐娟",
                    "state": "逾期未还",
                    "mobile": "18991502655",
                    "gender": "女",
                    "age": "",
                    "over_amount": "2235.10",
                    "publish_source": "拍拍贷",
                    "loan_amount": "3300.00",
                    "publish_date": "2011-01-04",
                    "address": "陕西省商洛市商州区迎宾路4号",
                    "enterprise_address": "",
                    "email": "11777761@qq.com",
                    "loan_term": "6"
                }]
        }

    },

    "has_negative_info": {
        "result": "00",
        "result_message": "检测通过或查询有记录",
        "content": {
            "check_message": "在逃、前科、吸毒",
            "case_time_list": ["20160101"]
        }
    },

    "is_netsky_grey": {
        "result": "00",
        "result_message": "检测通过或查询有记录",
        "content": [
            {
                "type": "博彩",
                "date": "",
                "desc": "1**的个人空间_彩客网",
                "originalRet": {
                    "no": 0,
                    "url": "",
                    "abstract": "",
                    "title": "",
                    "class": "",
                    "search_type": "",
                    "search_word": ""
                }
            }]
    },

    "is_court_zhixing": {
        "result": "00",
        "result_message": "检测通过或查询有记录",
        "content": {
            "zhixing_list": [{
                "case_create_time": "2016-03-01",
                "entity_id": "433031196210056032",
                "court": "通道侗族自治县人民法院",
                "entity_name": "吴永荣",
                "case_code": "(2016)湘1230执00016号",
                "case_state": "执行中",
                "exec_money": "237000"
            },
                {
                    "case_create_time": "2015-09-25",
                    "entity_id": "433031196210056032",
                    "court": "中山市第一人民法院",
                    "entity_name": "吴永荣",
                    "case_code": "(2015)中-法执字第08491号",
                    "case_state": "执行中",
                    "exec_money": "21651.16"
                },
                {
                    "case_create_time": "2015-09-21",
                    "entity_id": "433031196210056032",
                    "court": "中山市第一人民法院",
                    "entity_name": "吴永荣",
                    "case_code": "(2015)中-法执字第08293号",
                    "case_state": "执行中",
                    "exec_money": "50392.22"
                },
                {
                    "case_create_time": "2015-09-21",
                    "entity_id": "433031196210056032",
                    "court": "中山市第一人民法院",
                    "entity_name": "吴永荣",
                    "case_code": "(2015)中一法执字第08293号",
                    "case_state": "执行中",
                    "exec_money": "50392.22"
                },
                {
                    "case_create_time": "2015-01-09",
                    "entity_id": "433031196210056032",
                    "court": "中山市第二人民法院",
                    "entity_name": "吴永荣",
                    "case_code": "(2015)中二法执字第00706号",
                    "case_state": "执行中",
                    "exec_money": "305800"
                }
            ]
        }
    },

    "is_recruitment": {
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
                "school_nature": "",
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
    },

    "graduate_college": {
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
        "sns_skill_tag_list": [{
            "skill_tag": "string",
            "certified_num": 0
        }],
        "work_exp_form": [{
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
        }],
        "edu_exp_form": [{
            "school": "石家庄学院",
            "start": "string",
            "end": "string",
            "degree": "string",
            "degree_name": "string",
            "tz": 0
        }]
    },

    'car_number': {
        "status": "OK",
        "result": [
            {
                "license_no": "豫SFD***",
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
            {"license_no": "ASFD456"},
            {"license_no": "京SFD45"},

        ]
    },

    "college_type": {
        "content": {
            "person_base": {
                "original_address": "",
                "id_card_code": "130**24821",
                "name": "甄**",
                "degree": "本科",
                "gender": "女",
                "age": "25",
                "birthday": "19910512",
                "graduate_years": "4"},
            "college": {
                "create_data": "",
                "master_pilot": "",
                "manage_dept": "",
                "science_batch": "",
                "school_nature": "普通本科",
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
                "college_name": "石家庄学院"},
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
                "is_key_subject": "N"},
            "result_message": "检测通过或查询有记录",
            "result": "00"
        },
    },

    "graduate_college_check": {
        "content": {
            "person_base": {
                "original_address": "",
                "id_card_code": "130**24821",
                "name": "甄**",
                "degree": "本科",
                "gender": "女",
                "age": "25",
                "birthday": "19910512",
                "graduate_years": "4"},
            "college": {
                "create_data": "",
                "master_pilot": "",
                "manage_dept": "",
                "science_batch": "",
                "school_nature": "",
                "school_category": " 本科",
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
                "college_name": "石家庄学院"},
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
                "is_key_subject": "N"},
            "result_message": "检测通过或查询有记录",
            "result": "00"
        },
    },

    "education_degree_check": {
        "content": {
            "person_base": {
                "original_address": "",
                "id_card_code": "130**24821",
                "name": "甄**",
                "degree": "本科",
                "gender": "女",
                "age": "25",
                "birthday": "19910512",
                "graduate_years": "4"},
            "college": {
                "create_data": "",
                "master_pilot": "",
                "manage_dept": "",
                "science_batch": "",
                "school_nature": "985,211工程院校",
                "school_category": " 本科",
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
                "college_name": "石家庄学院"},
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
                "is_key_subject": "N"},
            "result_message": "检测通过或查询有记录",
            "result": "00"
        },
    },

    "pingan_multi_loan_infos": {
        "result": 0,
        "message": None,
        "data": {
            "record": [
                {},
                {"matchType": "phone",
                 "matchValue": "18627180708",
                 "matchId": "AA28960E040AE2BB960CD4736012A791",
                 "classification": [{
                     "M6": {
                         "other": {
                             "orgNums": 1, "loanAmount": None, "totalAmount": "(200, 500]", "repayAmount": None},
                         "bank": None,
                     }},
                     {
                         "M9": {
                             "other": {"orgNums": 1, "loanAmount": None, "totalAmount": "(0, 200]",
                                       "repayAmount": None},
                             "bank": None,
                         }},
                     {
                         "M12": {
                             "other": {"orgNums": 2, "loanAmount": None, "totalAmount": "(500, 1000]",
                                       "repayAmount": None},
                             "bank": {},
                         }},
                     {
                         "M24": {
                             "other": {"orgNums": 2, "loanAmount": None, "totalAmount": "(1000, 2000]",
                                       "repayAmount": None},
                             "bank": None,
                         }},
                 ]
                 }
            ],
            "phone": "18627180708",
            "imei": "",
            "imsi": "",
        }
    },


}


def test():
    for feature_name, datas in data.items():
        fecture_obj = FeatureProcess(feature_name, datas)
        result = fecture_obj.run()
        print result


if __name__ == '__main__':
    # data = {'pingan_multi_loan_infos': data['pingan_multi_loan_infos']}
    test()
