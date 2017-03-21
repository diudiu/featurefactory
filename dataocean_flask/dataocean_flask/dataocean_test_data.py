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
"""

data = {
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
