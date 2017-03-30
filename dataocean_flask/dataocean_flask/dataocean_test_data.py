# -*- coding:utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
"""
fecture:{
    'data_identify':'****',
    [
        {
           'req_data':{},
            'res_data':{}，
            'fecture_value': True
        },
        {
           'req_data':{},
            'res_data':{},
            'fecture_value': True
        },

    ]}
db.portrait_base.insert({  "_class" : "com.digcredit.brms.model.orm.mongo.Portrait", "proposer_id" : "123456789dinger", "product_code" : "12345", "data" : { "edu_exp_form" : [ { "school" : "北京理工", "start" : "201009", "end" : "201406", "degree" : "30", "degree_name" : "硕士", "tz" : 1 } ], "now_indust_code" : "330", "upload_contact" : 0, "sns_sd_friend_cnt" : 1194, "mobile" : "13311538888", "city_code" : "200", "work_age" : 11, "sns_friends_cnt" : 1, "registration_on" : "2016-10-01 12:20:10", "city_name" : "北京", "sns_skill_tag_list" : [ { "skill_tag" : "预测", "certified_num" : 0 } ], "name" : "丁二", "cur_work_status" : "在职", "complete_degree" : 95, "sns_h_fans_cn" : 31, "work_exp_form" : [ { "title" : "Lead Project control", "has_certified" : 0, "certified_num" : 0, "comp_name" : "微软中国", "months" : 13, "salary" : 16000, "work_start" : "201407", "work_end" : "999999", "industry" : "330", "industry_name" : "能源(电力/水利)", "dq" : "北京", "dq_name" : "北京朝阳" } ], "email" : "123@163.com", "now_indust_name" : "能源(电力/水利)" }, "is_delete" : false } )
db.portrait_base.insert({ "_class" : "com.digcredit.brms.model.orm.mongo.Portrait", "proposer_id" : "123456789lisi", "product_code" : "12345", "data" : { "edu_exp_form" : [ { "school" : "北京理工", "start" : "201009", "end" : "201406", "degree" : "10", "degree_name" : "博士", "tz" : 1 } ], "now_indust_code" : "150", "upload_contact" : 0, "sns_sd_friend_cnt" : 1902, "mobile" : "13661117777", "city_code" : "200", "work_age" : 9, "sns_friends_cnt" : 21, "registration_on" : "2016-10-01 12:20:10", "city_name" : "北京", "sns_skill_tag_list" : [ { "skill_tag" : "0", "certified_num" : 0 } ], "name" : "李四", "cur_work_status" : "在职", "complete_degree" : 80, "sns_h_fans_cn" : 10, "work_exp_form" : [ { "title" : "矿业投资部总经理", "has_certified" : 1, "certified_num" : 3, "comp_name" : "昆吾九鼎投资管理有限公司", "months" : 12, "salary" : 62500, "work_start" : "201407", "work_end" : "999999", "industry" : "150", "industry_name" : "基金/证券/期货/投资", "dq" : "北京", "dq_name" : "北京朝阳" } ], "email" : "456@163.com", "now_indust_name" : "基金/证券/期货/投资" }, "is_delete" : false }
db.portrait_base.insert({ "_class" : "com.digcredit.brms.model.orm.mongo.Portrait", "proposer_id" : "123456789zhangsan", "product_code" : "12345", "data" : { "edu_exp_form" : [ { "school" : "北京理工", "start" : "201009", "end" : "201406", "degree" : "20", "degree_name" : "MBA/EMBA", "tz" : 1 } ], "now_indust_code" : "170", "upload_contact" : 1, "sns_sd_friend_cnt" : 1294, "mobile" : "18511116277", "city_code" : "200", "work_age" : 14, "sns_friends_cnt" : 12, "registration_on" : "2016-10-01 12:20:10", "city_name" : "北京", "sns_skill_tag_list" : [ { "skill_tag" : "0", "certified_num" : 0 } ], "name" : "张三", "cur_work_status" : "在职", "complete_degree" : 80, "sns_h_fans_cn" : 281, "work_exp_form" : [ { "title" : "矿业投资部总经理", "has_certified" : 0, "certified_num" : 0, "comp_name" : "百度", "months" : 12, "salary" : 7000, "work_start" : "201608", "work_end" : "999999", "industry" : "170", "industry_name" : "影视/媒体/艺术/文化/出版", "dq" : "北京", "dq_name" : "北京朝阳" } ], "email" : "789@163.com", "now_indust_name" : "影视/媒体/艺术/文化/出版" }, "is_delete" : false }

db.apply_base.insert({ "product_code" : "890wefjf320if0i302f0j3f0f", "apply_id" : "APPLY201703081545051dxdinger", "data" : { "name" : "丁二", "card_id" : "132600199306251568", "mobile" : "13311538888", "longitudu" : 23.45678, "latitude" : 145.23342, "contacts" : 30, "application_on" : "2017-02-01 12:20:10" }, "proposer_id" : "123456789dinger", "is_delete" : false }
db.apply_base.insert({ "product_code" : "890wefjf320if0i302f0j3f0f", "apply_id" : "APPLY20170308154505179ydlisi", "data" : { "name" : "李四", "card_id" : "132600198506251568", "mobile" : "13661117777", "longitudu" : 23.45678, "latitude" : 145.23342, "contacts" : 30, "application_on" : "2017-02-01 12:20:10" }, "proposer_id" : "123456789lisi", "is_delete" : false }
db.apply_base.insert({ "product_code" : "890wefjf320if0i302f0j3f0f", "apply_id" : "APPLY2017030815450ltzhangsan", "data" : { "name" : "张三", "card_id" : "132600197206251568", "mobile" : "18511116277", "longitudu" : 23.45678, "latitude" : 145.23342, "contacts" : 30, "application_on" : "2017-02-01 12:20:10" }, "proposer_id" : "123456789zhangsan", "is_delete" : false })
"""

data_old = {
    'is_court_zhixing': {
        'data_identify': 'court_zhixing_a_s',
        'req_res': [
            {
                'req_data': {'access_token': 'aaaaaaaaa',
                             'entity_id': '433031196210056032',
                             'entity_name': '吴永荣',
                             'data_identity': 'court_zhixing_a_s'},
                'res_data': {
                    "result": "00",
                    "result_message": "检测通过或查询有记录",
                    "content":
                        {
                            "zhixing_list":
                                [
                                    {
                                        "case_create_time": "2016-03-01",
                                        "entity_id": "433031196210056032",
                                        "court": "通道侗族自治县人民法院",
                                        "entity_name": "吴永荣",
                                        "case_code": "(2016)湘1230执00016号",
                                        "case_state": "执行中",
                                        "exec_money": "237000"
                                    },

                                ]
                        }
                },
                'fecture_value': True
            },
            {
                'req_data': {'access_token': 'aaaaaaaaa',
                             'entity_id': '410381199012296021',
                             'entity_name': '郭靖',
                             'data_identity': 'court_zhixing_a_s'},
                'res_data': {
                    "result": "11",
                    "result_message": "检测不通过",
                    "content":
                        {
                            "zhixing_list":
                                [
                                    {
                                        "case_create_time": "2016-03-01",
                                        "entity_id": "410381199012296321",
                                        "court": "通道侗族自治县人民法院",
                                        "entity_name": "郭",
                                        "case_code": "(2016)湘1230执00016号",
                                        "case_state": "执行中",
                                        "exec_money": "237000"
                                    },

                                ]
                        }
                },
                'fecture_value': False
            },

        ]},
    'mobile_online_time': {
        'data_identify': 'unicome_mobile_online_time_s',
        'req_res': [
            {
                'req_data': {
                    "access_token": " sCUm9NJAcpGgZWBVp0yWp89lILnOUw",
                    "mobile": "15538810634",
                    "data_identity": "unicom_mobile_online_time_s"
                },
                'res_data': {
                    "result": "11",
                    "result_message": "检测通过或查询有记录",
                    "content": {
                        "online_time": "[0-1]"
                    }
                },
                'fecture_value': "(0,6)"
            },
        ]},
    'is_net_black': {
        'data_identify': 'net_black_a_s',
        'req_res': [
            {
                'req_data': {
                    "access_token": "mUI98g7W2Blnkj7umQlDck1uA7jg1X",
                    "id_card_code": "612501198407110021",
                    "data_identity": "net_black_a_s",
                    "id_card_name": "徐娟"
                },
                'res_data': {
                    "result": "00",
                    "result_message": "检测通过或查询有记录",
                    "content": {
                        "data_list": [
                            {
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
                            }
                        ]
                    }
                },
                'fecture_value': True
            },
        ]},
}

data = {
    "loan_agency": [
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'loan_agency',
                'mobile': '13311538888',
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'loan_agency',
                'mobile': '13661117777',
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'loan_agency',
                'mobile': '18511116277',
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
    ],
    "agentg_black": [
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'agentg_black',
                'id_card_name': '丁二',
                'id_card_code': '132600199306251568',
                'mobile': '13311538888'
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'agentg_black',
                'id_card_name': '李四',
                'id_card_code': '132600198506251568',
                'mobile': '13661117777'
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'agentg_black',
                'id_card_name': '张三',
                'id_card_code': '132600197206251568',
                'mobile': '18511116277'
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
    ],
    "tianwang_black": [
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'tianwang_black',
                'mobile': '13311538888',
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'tianwang_black',
                'mobile': '13661117777',
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'tianwang_black',
                'mobile': '18511116277',
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
    ],
    "tianwang_multi_loan": [
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'tianwang_multi_loan',
                'mobile': '13311538888',
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'tianwang_multi_loan',
                'mobile': '13661117777',
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'tianwang_multi_loan',
                'mobile': '18511116277',
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
    ],
    "tianyan_black": [
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'tianyan_black',
                'email': '123@163.com',
                'id_card_code': '132600199306251568',
                'mobile': '13311538888'
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'tianyan_black',
                'email': '456@163.com',
                'id_card_code': '132600198506251568',
                'mobile': '13661117777'
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'tianyan_black',
                'email': '789@163.com',
                'id_card_code': '132600197206251568',
                'mobile': '18511116277'
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
    ],
    "court_shixin_a_s": [
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'court_shixin_a_s',
                'entity_name': '丁二',
                'entity_id': '132600199306251568',
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'court_shixin_a_s',
                'entity_name': '李四',
                'entity_id': '132600198506251568',
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'court_shixin_a_s',
                'entity_name': '张三',
                'entity_id': '132600197206251568',
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
    ],
    "net_black_a_s": [
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'net_black_a_s',
                'id_card_name': '丁二',
                'id_card_code': '132600199306251568',
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'net_black_a_s',
                'id_card_name': '李四',
                'id_card_code': '132600198506251568',
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'net_black_a_s',
                'id_card_name': '张三',
                'id_card_code': '132600197206251568',
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
    ],
    "negative_info_s": [
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'negative_info_s',
                'id_card_name': '丁二',
                'id_card_code': '132600199306251568',
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'negative_info_s',
                'id_card_name': '李四',
                'id_card_code': '132600198506251568',
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'negative_info_s',
                'id_card_name': '张三',
                'id_card_code': '132600197206251568',
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
    ],
    "tianwang_gray": [
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'tianwang_gray',
                'mobile': '13311538888',
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'tianwang_gray',
                'mobile': '13661117777',
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'tianwang_gray',
                'mobile': '18511116277',
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
    ],
    "court_zhixing_a_s": [
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'court_zhixing_a_s',
                'entity_name': '丁二',
                'entity_id': '132600199306251568',
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'court_zhixing_a_s',
                'entity_name': '李四',
                'entity_id': '132600198506251568',
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'court_zhixing_a_s',
                'entity_name': '张三',
                'entity_id': '132600197206251568',
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
    ],
    "telecom_mobile_online_time_s": [
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'telecom_mobile_online_time_s',
                'mobile': '13311538888',
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                    "online_time": "[0-6)"
                },
            }
        },
    ],
    "unicome_mobile_online_time_s": [
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'unicome_mobile_online_time_s',
                'mobile': '18511116277',
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                    "online_time": "[0-1]"
                },
            }
        },
    ],
    "yd_mobile_online_time_s": [
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'yd_mobile_online_time_s',
                'mobile': '13661117777',
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                    "online_time": "[3,6)"
                },
            }
        },
    ],
    "mobile_locale": [
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'mobile_locale',
                'mobile': '13311538888',
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                    "mobile_area": "北京市",
                },
            }
        },
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'mobile_locale',
                'mobile': '13661117777',
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                    "mobile_area": "北京市",
                },
            }
        },
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'mobile_locale',
                'mobile': '18511116277',
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                    "mobile_area": "北京市",
                },
            }
        },
    ],
    "telecom_mobile_identity_s": [
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'telecom_mobile_identity_s',
                'id_card_name': '丁二',
                'id_card_code': '132600199306251568',
                'mobile': '13311538888'
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                },
            }
        },
    ],
    "unicom_mobile_identity_s": [
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'unicom_mobile_identity_s',
                'id_card_name': '张三',
                'id_card_code': '132600197206251568',
                'mobile': '18511116277'
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                },
            }
        },
    ],
    "yd_mobile_identity_s": [
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'yd_mobile_identity_s',
                'id_card_name': '李四',
                'id_card_code': '132600198506251568',
                'mobile': '13661117777'
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                },
            }
        },
    ],
    "airline_passenger_info": [
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'airline_passenger_info',
                'id_card_name': '丁二',
                'id_card_code': '132600199306251568',
            },
            "res_data": {
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
                    "average_price": 1340.5,
                    "delay_time": 40,
                    "average_delay_time": 20,
                    "average_ticket_day": 68,
                    "last_date": "20150228",
                    "last_from_city": "广元",
                    "last_destination_city": "北京",
                    "total_distance": 2810,
                },
            }
        },
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'airline_passenger_info',
                'id_card_name': '李四',
                'id_card_code': '132600198506251568',
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                    "id_card_name": "吴*",
                    "id_card_code": "513722198908***43X",
                    "flight_times": 0,
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
            }
        },
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'airline_passenger_info',
                'id_card_name': '张三',
                'id_card_code': '132600197206251568',
            },
            "res_data": {
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
                    "inland_count": 4,
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
            }
        },
    ],
    "unicom_finance_portrait_s": [
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'unicom_finance_portrait_s',
                'mobile': '18511116277'
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                    "last12": {
                        "credit": {
                            "charge_off_range": "b",
                            "charge_off_times": 25,
                            "income_times": 35,
                            "income_range": "c"
                        },
                        "debit": {
                            "charge_off_range": "13",
                            "charge_off_times": 138,
                            "income_times": 16,
                            "income_range": "13",
                        }
                    }
                }
            }
        },
    ],
    "education_review_s": [
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'education_review_s',
                'id_card_name': '丁二',
                'id_card_code': '132600199306251568',
            },
            "res_data": {
                "result_message": "检测通过或查询有记录",
                "result": "00",
                "content": {
                    "person_base": {
                        "original_address": "",
                        "id_card_code": "130**24821",
                        "name": "甄**",
                        "degree": "本科",
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
                    },
                },
            }
        },
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'education_review_s',
                'id_card_name': '李四',
                'id_card_code': '132600198506251568',
            },
            "res_data": {
                "result_message": "检测通过或查询有记录",
                "result": "00",
                "content": {
                    "person_base": {
                        "original_address": "",
                        "id_card_code": "130**24821",
                        "name": "甄**",
                        "degree": "本科",
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
                    },
                },
            }
        },
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'education_review_s',
                'id_card_name': '张三',
                'id_card_code': '132600197206251568',
            },
            "res_data": {
                "result_message": "检测通过或查询有记录",
                "result": "00",
                "content": {
                    "person_base": {
                        "original_address": "",
                        "id_card_code": "130**24821",
                        "name": "甄**",
                        "degree": "本科",
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
                    },
                },
            }
        },
    ],
    "multi_id_card_info_s": [
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'multi_id_card_info_s',
                'id_card_name': '丁二',
                'id_card_code': '132600199306251568',
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                    "id_card_name": "李..",
                    "id_card_code": "1306251....",
                    "verify": "一致",
                    "company": "暂无",
                    "nation": "汉族",
                    "marital_status": "10",
                    "former_name": "",
                    "native_place": "河北省保定市徐水县",
                    "birthday": "1988-09-10",
                    "birth_place": "河北省保定市徐水县",
                    "sex_id": "2",
                    "photo": "",
                    "education": "大学本科",
                    "address": "河北省保定市徐水区高林村镇"
                }
            }
        },
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'multi_id_card_info_s',
                'id_card_name': '李四',
                'id_card_code': '132600198506251568',
            },
            "res_data": {
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
                    "education": "大学本科",
                    "address": "河北省保定市徐水区高林村镇"
                }
            }
        },
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'multi_id_card_info_s',
                'id_card_name': '张三',
                'id_card_code': '132600197206251568',
            },
            "res_data": {
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
                    "education": "大学本科",
                    "address": "河北省保定市徐水区高林村镇"
                }
            }
        },
    ],
    "industrial_commercial_s": [
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'industrial_commercial_s',
                'enterprise_name': '微软中国',
                'register_code': ''
            },
            "res_data": {
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
                    "staff_count": "30",
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
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'industrial_commercial_s',
                'enterprise_name': '昆吾九鼎投资管理有限公司',
                'register_code': ''
            },
            "res_data": {
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
                    "staff_count": "30",
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
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'industrial_commercial_s',
                'enterprise_name': '百度',
                'register_code': ''
            },
            "res_data": {
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
                    "staff_count": "30",
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
    ],
    "high_way_over_speed": [
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'high_way_over_speed',
                'license_plate': '京P3L43H',
                "high_way_period": "4",
                "start_time": "",
                "end_time": ""
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                    "license_plate": "京P3L43H",
                    "start_time": "201401",
                    "end_time": "201412",
                    "over_speed_times": 2,
                    "over_speed_list": [
                        {
                            "count_month": "201506",
                            "month_times": 2,
                            "section": "北京通州站-河北燕郊站，河北廊坊站-天津蓟县站",
                        }
                    ]
                }
            }
        },
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'high_way_over_speed',
                'license_plate': '京P3L82G',
                "high_way_period": "4",
                "start_time": "",
                "end_time": ""
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                    "license_plate": "京P3L82G",
                    "start_time": "201401",
                    "end_time": "201412",
                    "over_speed_times": 2,
                    "over_speed_list": [
                        {
                            "count_month": "201506",
                            "month_times": 2,
                            "section": "北京通州站-河北燕郊站，河北廊坊站-天津蓟县站",
                        }
                    ]
                }
            }
        },
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'high_way_over_speed',
                'license_plate': '京F86B3H',
                "high_way_period": "4",
                "start_time": "",
                "end_time": ""
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                    "license_plate": "京F86B3H",
                    "start_time": "201401",
                    "end_time": "201412",
                    "over_speed_times": 2,
                    "over_speed_list": [
                        {
                            "count_month": "201506",
                            "month_times": 2,
                            "section": "北京通州站-河北燕郊站，河北廊坊站-天津蓟县站",
                        }
                    ]
                }
            }
        },
    ],
    "high_way_over_load": [
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'high_way_over_load',
                'license_plate': '京P3L43H',
                "high_way_period": "4",
                "start_time": "",
                "end_time": ""
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                    "license_plate": "京P3L43H",
                    "start_time": "201401",
                    "end_time": "201412",
                    "over_load_times": 2,
                    "over_load_list": [
                        {
                            "count_month": "201506",
                            "month_times": 2,
                        }
                    ]
                }
            }
        },
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'high_way_over_load',
                'license_plate': '京P3L82G',
                "high_way_period": "4",
                "start_time": "",
                "end_time": ""
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                    "license_plate": "京P3L82G",
                    "start_time": "201401",
                    "end_time": "201412",
                    "over_load_times": 2,
                    "over_load_list": [
                        {
                            "count_month": "201506",
                            "month_times": 2,
                        }
                    ]
                }
            }
        },
        {
            "req_data": {
                'access_token': 'aaaaaaaaa',
                'data_identity': 'high_way_over_load',
                'license_plate': '京F86B3H',
                "high_way_period": "4",
                "start_time": "",
                "end_time": ""
            },
            "res_data": {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                    "license_plate": "京F86B3H",
                    "start_time": "201401",
                    "end_time": "201412",
                    "over_load_times": 2,
                    "over_load_list": [
                        {
                            "count_month": "201506",
                            "month_times": 2,
                        }
                    ]
                }
            }
        },
    ],
}
