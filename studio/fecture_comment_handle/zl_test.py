# -*- coding:utf-8 -*-

from featrue_process import FeatureProcess

data = {
    'application_on': {
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
    'application_on_plus': {
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

    'cc_bill_age': {
        "status": "OK",
        "result": {
            "rrx_once_all": {
                "banks_num": "开卡银行个数",
                "debit_cards_num": "3",
                "credit_cards_num": "1",
                "debit_card_account_age": "2",
                "credit_card_account_age": "3"
            }
        }
    },

    'complete_degree': {
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
    },

    'dc_bill_age': {
        "status": "OK",
        "result": {
            "rrx_once_all": {
                "banks_num": "开卡银行个数",
                "debit_cards_num": "3",
                "credit_cards_num": "1",
                "debit_card_account_age": "2",
                "credit_card_account_age": "3"
            }
        }
    },

    'creditcard_count': {
        "status": "OK",
        "result": {
            "rrx_once_all": {
                "banks_num": "开卡银行个数",
                "debit_cards_num": "3",
                "credit_cards_num": "1",
                "debit_card_account_age": "2",
                "credit_card_account_age": "3"
            }
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

    'overload_count': {
        "XXXX1234":
        {
            "result": "00",
            "result_message": "检测通过或查询有记录",
            "content": {
                "license_plate": "渝FC8***",
                "start_time": "201401",
                "end_time": "201412",
                "over_load_times": 2,
                "over_load_list": [{
                    "count_month": "201506",
                    "month_times": 5, }
                ]
            }
        },
        "XXXX5678":
            {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                    "license_plate": "渝FC8***",
                    "start_time": "201401",
                    "end_time": "201412",
                    "over_load_times": 5,
                    "over_load_list": [{
                        "count_month": "201506",
                        "month_times": '', }
                    ]
                }
            },
        "XXXX5679":
            {
                "result": "11",
                "result_message": "检测通过或查询有记录",
                "content": {
                    "license_plate": "渝FC8***",
                    "start_time": "201401",
                    "end_time": "201412",
                    "over_load_times": 5,
                    "over_load_list": [{
                        "count_month": "201506",
                        "month_times": 1, }
                    ]
                }
            },
    },

    'overspeed_count': {
        "XXXX1234":
            {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                    "license_plate": "渝FC8***",
                    "start_time": "201401",
                    "end_time": "201412",
                    "over_speed_times": 2,
                    "over_speed_list": [{
                        "count_month": "201506",
                        "month_times": '',
                        "section": "北京通州站-河北燕郊站，河北廊坊站-天津蓟县站",}
                    ]
                }
            },
        "XXXX5678":
            {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                    "license_plate": "渝FC8***",
                    "start_time": "201401",
                    "end_time": "201412",
                    "over_speed_times": 1,
                    "over_speed_list": [{
                        "count_month": "201506",
                        "month_times": 2,
                        "section": "北京通州站-河北燕郊站，河北廊坊站-天津蓟县站",}
                    ]
                }
            },
        "XXXX5679":
            {
                "result": "11",
                "result_message": "检测通过或查询有记录",
                "content": {
                    "license_plate": "渝FC8***",
                    "start_time": "201401",
                    "end_time": "201412",
                    "over_speed_times": 2,
                    "over_speed_list": [{
                        "count_month": "201506",
                        "month_times": 2,
                        "section": "北京通州站-河北燕郊站，河北廊坊站-天津蓟县站",}
                    ]
                }
            },
    },

    'is_loan_agency': {
        "result": "00",
        "result_message": "检测通过或查询有记录",
        "content": [{
            "source_name": " 赶集网",
            "name": "张三",
            "mobile": " 13581***204",
            "business_released_date": " 2015-06-01",
            "company_register_date": " 2015-03-01",
            "publish_city": "北京市",
            "company_name": "北京某投资公司",
            "company_address": "北京市海淀区上地",
            "company_url": "http://www.exp.com",
        }, ]
    },

    'is_netsky_black': {
        "result": "00",
        "result_message": "检测通过或查询有记录",
        "content": [
            {
                "type": "商品交易",
                "date": "",
                "desc": "WOOG韩版男装2014秋季新款蓝色小脚休闲裤男士纯色潮流修身型",
                "originalRet": {
                    "no": 8,
                    "url": "http://bagideal.com/goods_44652152990.html",
                    "abstract": "1398**0 品牌: 价格: 369.00 韩版男装2014秋季新款蓝色小脚休闲裤男士纯色潮流修身型长裤评价",
                    "title": "WOOG韩版男装2014秋季新款蓝色小脚休闲裤男士纯色潮流修身型",
                    "search_type": "phone",
                    "search_word": "13**000",
                    "class": "商品交易"
                }
            }, ]
    },
    'is_organization_g_black': {
        "result": "00",
        "result_message": "检测通过或查询有记录",
        "content": [{
            "type": "欺诈",
            "date": "",
            "desc": "",
            "originalRet": {
                "name": "100",
                "pid": "100",
                "mobile": "0",
                "confirm_type": "欺诈",
                "confirm_details": "",
                "confirmed_at": "2014年02月01日",
                "loan_type": "",
                "applied_at": ""
            }
        }]
    },

    'is_pingan_multi_loan': {
        "result": 0,
        "message": None,
        "data": {
            "record": [
                {"matchType": "phone",
                 "matchValue": "18627180708",
                 "matchId": "AA28960E040AE2BB960CD4736012A791",
                 "classification": [

                     {
                         "M6": {
                             "other": {
                                 "orgNums": 1, "loanAmount": None, "totalAmount": "(200, 500]", "repayAmount": None
                             },
                             "bank": None,
                         }}
                 ]
                 }
            ],
            "phone": "18627180708",
            "imei": "",
            "imsi": "",
        }
    },
    'pingan_multi_loan_count': {
        "result": 0,
        "message": None,
        "data": {
            "record": [
                {"matchType": "phone",
                 "matchValue": "18627180708",
                 "matchId": "AA28960E040AE2BB960CD4736012A791",
                 "classification": [
                     {
                         "M6": {
                             "other": {
                                 "orgNums": None, "loanAmount": None, "totalAmount": "(200, 500]", "repayAmount": None
                             },
                             "bank": None,
                         }},
                     {
                         "M9": {
                             "other": {"orgNums": "1", "loanAmount": None, "totalAmount": "(0, 200]",
                                       "repayAmount": None},
                             "bank": {"orgNums": 1},
                         }},
                     {
                         "M12": {
                             "other": {"orgNums": 2, "loanAmount": None, "totalAmount": "(500, 1000]",
                                       "repayAmount": None},
                             "bank": {},
                         }},
                     {
                         "M24": {
                             "other": {"orgNums": 0, "loanAmount": None, "totalAmount": "(1000, 2000]",
                                       "repayAmount": None},
                             "bank": None,
                         }}
                 ]
                 }
            ],
            "phone": "18627180708",
            "imei": "",
            "imsi": ""}},

    'mobile_mark': {
        "tags": {
            "contactMain_IMSI1_IMEI1":
                {
                    "city": "上海市上海市",
                    "label": "未被标记",
                    "operator": "上海移动",
                },
        },
    },

    'education_degree_code': {
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
        "edu_exp_form": [
            {
                "school": "string",
                "start": "string",
                "end": "string",
                "degree": "40",
                "degree_name": "中专",
                "tz": 0
            },
            {
                "school": "string",
                "start": "string",
                "end": "string",
                "degree": "80",
                "degree_name": "",
                "tz": 0
            },
            {
                "school": "string",
                "start": "string",
                "end": "string",
                "degree": "",
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
    data = {'overload_count': data['overload_count']}
    # application_on
    # application_on_plus
    # cc_bill_age
    # complete_degree
    # creditcard_count
    # dc_bill_age
    # # education_degree_code
    # # income_level
    # is_loan_agency
    # is_netsky_black
    # is_organization_g_black
    # is_pingan_multi_loan
    # mobile_mark
    # # online_time
    # pingan_multi_loan_count
    # overspeed_count
    # overload_count
    test()

