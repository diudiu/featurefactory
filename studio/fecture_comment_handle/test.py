# -*- coding:utf-8 -*-

from featrue_process import FeatureProcess


data = {
    'cur_company': {
        'portrait_data': {
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
        }
    },

    'pingan_overdue_count': {
        'trustutn_loan_overdue': {
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
                                    "longestDays": "1"
                                },
                                "otherCredit": {
                                    "orgNums": 12,
                                    "recordNums": None,
                                    "maxAmount": "(1000, 2000]",
                                    "longestDays": "1"
                                },
                                "bankLoan": None
                            }
                        },
                        {
                            "M6": {
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
                        }]
                }],
                "phone": "15821732543",
                "imei": "",
                "imsi": ""
            }
        }
    },

    'pingan_overdue_corp_count': {
        'trustutn_loan_overdue': {
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
                                    "longestDays": "1"
                                },
                                "otherCredit": {
                                    "orgNums": 12,
                                    "recordNums": None,
                                    "maxAmount": "(1000, 2000]",
                                    "longestDays": "1"
                                },
                                "bankLoan": None
                            }
                        },
                        {
                            "M6": {
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
                        }]
                }],
                "phone": "15821732543",
                "imei": "",
                "imsi": ""
            }
        }
    },

    'pingan_max_overdue_days': {
        'trustutn_loan_overdue': {
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
                                    "longestDays": "1"
                                },
                                "otherCredit": {
                                    "orgNums": 12,
                                    "recordNums": None,
                                    "maxAmount": "(1000, 2000]",
                                    "longestDays": "1"
                                },
                                "bankLoan": None
                            }
                        },
                        {
                            "M6": {
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
                        }]
                }],
                "phone": "15821732543",
                "imei": "",
                "imsi": ""
            }
        }
    },

    'is_pingan_overdue_loan': {
        'trustutn_loan_overdue': {
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
                                    "longestDays": "1"
                                },
                                "otherCredit": {
                                    "orgNums": 12,
                                    "recordNums": None,
                                    "maxAmount": "(1000, 2000]",
                                    "longestDays": "1"
                                },
                                "bankLoan": None
                            }
                        },
                        {
                            "M6": {
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
                        }]
                }],
                "phone": "15821732543",
                "imei": "",
                "imsi": ""
            }
        }
    },

    'is_pingan_other_loan': {
        'trustutn_loan_otheragent': {
            "result": 0,
            "message": None,
            "data": {
                "201603": {
                    "orgNums": "23",
                    "queryNums": "123"
                },
                "201602": None,
                "201601": {
                    "orgNums": None,
                    "queryNums": "123"
                },
                "201512": {
                    "orgNums": "29",
                    "queryNums": "123"
                },
                "201511": {
                    "orgNums": "28",
                    "queryNums": "123"
                },
                "201510": {
                    "orgNums": "12",
                    "queryNums": "123"
                }
            }

        }
    },

    'pingan_other_loan_count': {
        'trustutn_loan_otheragent': {
            "result": 0,
            "message": None,
            "data": {
                "201603": {
                    "orgNums": "23",
                    "queryNums": "123"
                },
                "201602": None,
                "201601": {
                    "orgNums": None,
                    "queryNums": "123"
                },
                "201512": {
                    "orgNums": "29",
                    "queryNums": "123"
                },
                "201511": {
                    "orgNums": "28",
                    "queryNums": "123"
                },
                "201510": {
                    "orgNums": "12",
                    "queryNums": "123"
                }
            }
        }
    },

    'pingan_other_loan_infos': {
        'trustutn_loan_otheragent': {
            "result": 0,
            "message": None,
            "data": {
                "201603": {
                    "orgNums": "23",
                    "queryNums": "123"
                },
                "201602": None,
                "201601": {
                    "orgNums": None,
                    "queryNums": "123"
                },
                "201512": {
                    "orgNums": "29",
                    "queryNums": "123"
                },
                "201511": {
                    "orgNums": "28",
                    "queryNums": "123"
                },
                "201510": {
                    "orgNums": "12",
                    "queryNums": "123"
                }
            }
        }
    },

    'pingan_overdue_loan_infos': {
        'trustutn_loan_overdue': {
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
                                    "longestDays": "1"
                                },
                                "otherCredit": {
                                    "orgNums": 12,
                                    "recordNums": None,
                                    "maxAmount": "(1000, 2000]",
                                    "longestDays": "1"
                                },
                                "bankLoan": None
                            }
                        },
                        {
                            "M6": {
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
                        }]
                }],
                "phone": "15821732543",
                "imei": "",
                "imsi": ""
            }
        }
    },

    'cur_corp_years': {
        'industrial_commercial_s': {
            "result": "00",
            "result_message": "检测通过或查询有记录",
            "content": {
                "operation_start": "2009-09-08",
                "register_code": "371102200011819",
                "currency": "人民币",
                "postal_code": "",
                "national_economy_code": "5165",
                "enterprise_type": "有限责任公司(自然人投资或控股)",
                "operation_project": "矿产品(国家专控除外)、煤炭、钢材、木制品、建材、初级农产品、工程机械、机电设备、金属制品、摩托车、家用电器、文化用品、橡胶制品、化工产品（危险化学品及易制毒化学品除外）销售；普通货物进出口(法律禁止和国家专控除外限制的项目需取得许可证方可经营)。(依法须经批准的项目，经相关部门批准后方可开展经营活动)。",
                "industry_category_code": "F",
                "registered_assets": "1000.000000",
                "legal_person_name": "孙国庆",
                "authority_code": "",
                "start_business_date": "2009-09-08",
                "annual_inspection_year": "",
                "operation_scope_form": "矿产品(国家专控除外)、煤炭、钢材、木制品、建材、初级农产品、工程机械、机电设备、金属制品、摩托车、家用电器、文化用品、橡胶制品、化工产品（危险化学品及易制毒化学品除外）销售；普通货物进出口(法律禁止和国家专控除外限制的项目需取得许可证方可经营)。(依法须经批准的项目，经相关部门批准后方可开展经营活动)。",
                "staff_count": "",
                "revoke_date": "",
                "registration_authority": "日照市工商行政管理局东港分局",
                "tp_deal_identifying": "",
                "enterprise_phone": "",
                "annual_inspection_date": "",
                "authority_name": "",
                "organization_code": "",
                "address": "日照市黄海一路兴业国际商城001号楼01单元903号",
                "enterprise_name": "山东南港国际贸易有限公司",
                "operation_end": "2019-09-07",
                "organization_code_end": "",
                "organization_code_start": "",
                "licensing_project": "",
                "cancellation_date": "",
                "operation_status": "在营（开业）",
                "operation_scope": "矿产品(国家专控除外)、煤炭、钢材、木制品、建材、初级农产品、工程机械、机电设备、金属制品、摩托车、家用电器、文化用品、橡胶制品、化工产品（危险化学品及易制毒化学品除外）销售；普通货物进出口(法律禁止和国家专控除外限制的项目需取得许可证方可经营)。(依法须经批准的项目，经相关部门批准后方可开展经营活动)。"
            },
        }
    },

    'cur_employee_number': {
        'industrial_commercial_s': {
            "result": "00",
            "result_message": "检测通过或查询有记录",
            "content": {
                "operation_start": "2009-09-08",
                "register_code": "371102200011819",
                "currency": "人民币",
                "postal_code": "",
                "national_economy_code": "5165",
                "enterprise_type": "有限责任公司(自然人投资或控股)",
                "operation_project": "矿产品(国家专控除外)、煤炭、钢材、木制品、建材、初级农产品、工程机械、机电设备、金属制品、摩托车、家用电器、文化用品、橡胶制品、化工产品（危险化学品及易制毒化学品除外）销售；普通货物进出口(法律禁止和国家专控除外限制的项目需取得许可证方可经营)。(依法须经批准的项目，经相关部门批准后方可开展经营活动)。",
                "industry_category_code": "F",
                "registered_assets": "1000.000000",
                "legal_person_name": "孙国庆",
                "authority_code": "",
                "start_business_date": "2009-09-08",
                "annual_inspection_year": "",
                "operation_scope_form": "矿产品(国家专控除外)、煤炭、钢材、木制品、建材、初级农产品、工程机械、机电设备、金属制品、摩托车、家用电器、文化用品、橡胶制品、化工产品（危险化学品及易制毒化学品除外）销售；普通货物进出口(法律禁止和国家专控除外限制的项目需取得许可证方可经营)。(依法须经批准的项目，经相关部门批准后方可开展经营活动)。",
                "staff_count": "",
                "revoke_date": "",
                "registration_authority": "日照市工商行政管理局东港分局",
                "tp_deal_identifying": "",
                "enterprise_phone": "",
                "annual_inspection_date": "",
                "authority_name": "",
                "organization_code": "",
                "address": "日照市黄海一路兴业国际商城001号楼01单元903号",
                "enterprise_name": "山东南港国际贸易有限公司",
                "operation_end": "2019-09-07",
                "organization_code_end": "",
                "organization_code_start": "",
                "licensing_project": "",
                "cancellation_date": "",
                "operation_status": "在营（开业）",
                "operation_scope": "矿产品(国家专控除外)、煤炭、钢材、木制品、建材、初级农产品、工程机械、机电设备、金属制品、摩托车、家用电器、文化用品、橡胶制品、化工产品（危险化学品及易制毒化学品除外）销售；普通货物进出口(法律禁止和国家专控除外限制的项目需取得许可证方可经营)。(依法须经批准的项目，经相关部门批准后方可开展经营活动)。"
            },
        }
    },

    'is_cur_corp_shixin': {
        'court_shixin_a_s': {
        "result": "00",
        "result_message": "检测通过或查询有记录",
        "content": {
             "shixin_list":
		[
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
			}
		]
        }
        }
    },

    'name': {
        'apply_data': {
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
        }
    },

    'card_id': {
        'apply_data': {
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
        }
    },

    'mobile': {
        'apply_data': {
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
        }
    },

}


def test(data):
    for feature_name, datas in data.items():
        fecture_obj = FeatureProcess(feature_name, datas)
        result = fecture_obj.run()
        print result

if __name__ == '__main__':
    data = {'pingan_other_loan_infos': data['pingan_other_loan_infos']}
    test(data)

