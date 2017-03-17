# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/3/10
    Change Activity:
"""

import pymongo

done_data = {
    'loan_agency': [
        {
            'args': {
                'data_identity': 'loan_agency',
                'mobile': '13311538888',
            },
            'data': {
                "result": "11",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'loan_agency',
                'mobile': '18910592066',
            },
            'data': {
                "result": "11",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'loan_agency',
                'mobile': '18911970588',
            },
            'data': {
                "result": "11",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'loan_agency',
                'mobile': '18511116256',
            },
            'data': {
                "result": "22",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'loan_agency',
                'mobile': '18511116277',
            },
            'data': {
                "result": "33",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'loan_agency',
                'mobile': '18511116212',
            },
            'data': {
                "result": "11",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'loan_agency',
                'mobile': '18511116218',
            },
            'data': {
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
            }
        },
        {
            'args': {
                'data_identity': 'loan_agency',
                'mobile': '13488898888 ',
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'loan_agency',
                'mobile': '13901395838',
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'loan_agency',
                'mobile': '13901328888',
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
    ],
    'agentg_black': [
        {
            'args': {
                'data_identity': 'agentg_black',
                'id_card_name': '璐璐1',
                'id_card_code': '132600198906251568',
                'mobile': '13311538888'
            },
            'data': {
                "result": "11",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'agentg_black',
                'id_card_name': '璐璐2',
                'id_card_code': '132600198906251569',
                'mobile': '18910592066'
            },
            'data': {
                "result": "11",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'agentg_black',
                'id_card_name': '璐璐3',
                'id_card_code': '132600198906251570',
                'mobile': '18911970588'
            },
            'data': {
                "result": "22",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'agentg_black',
                'id_card_name': '璐璐4',
                'id_card_code': '132600198906251571',
                'mobile': '18511116256'
            },
            'data': {
                "result": "22",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'agentg_black',
                'id_card_name': '璐璐5',
                'id_card_code': '132600198906251572',
                'mobile': '18511116277'
            },
            'data': {
                "result": "44",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'agentg_black',
                'id_card_name': '璐璐6',
                'id_card_code': '132600198906251573',
                'mobile': '18511116212'
            },
            'data': {
                "result": "44",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'agentg_black',
                'id_card_name': '璐璐7',
                'id_card_code': '132600198906251574',
                'mobile': '18511116218'
            },
            'data': {
                "result": "33",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'agentg_black',
                'id_card_name': '璐璐8',
                'id_card_code': '132600198906251575',
                'mobile': '13488898888'
            },
            'data': {
                "result": "33",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'agentg_black',
                'id_card_name': '璐璐9',
                'id_card_code': '132600198906251576',
                'mobile': '13901395838'
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'agentg_black',
                'id_card_name': '璐璐x',
                'id_card_code': '132600198906251577',
                'mobile': '13901328888'
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
    ],
    'tianwang_black': [
        {
            'args': {
                'data_identity': 'tianwang_black',
                'mobile': '13311538888',
            },
            'data': {
                "result": "11",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'tianwang_black',
                'mobile': '18910592066',
            },
            'data': {
                "result": "11",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'tianwang_black',
                'mobile': '18911970588',
            },
            'data': {
                "result": "11",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'tianwang_black',
                'mobile': '18511116256',
            },
            'data': {
                "result": "22",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'tianwang_black',
                'mobile': '18511116277',
            },
            'data': {
                "result": "33",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'tianwang_black',
                'mobile': '18511116212',
            },
            'data': {
                "result": "11",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'tianwang_black',
                'mobile': '18511116218',
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'tianwang_black',
                'mobile': '13488898888 ',
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'tianwang_black',
                'mobile': '13901395838',
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'tianwang_black',
                'mobile': '13901328888',
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
    ],
    'tianwang_multi_loan': [
        {
            'args': {
                'data_identity': 'tianwang_multi_loan',
                'mobile': '13311538888',
            },
            'data': {
                "result": "11",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'tianwang_multi_loan',
                'mobile': '18910592066',
            },
            'data': {
                "result": "11",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'tianwang_multi_loan',
                'mobile': '18911970588',
            },
            'data': {
                "result": "11",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'tianwang_multi_loan',
                'mobile': '18511116256',
            },
            'data': {
                "result": "22",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'tianwang_multi_loan',
                'mobile': '18511116277',
            },
            'data': {
                "result": "33",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'tianwang_multi_loan',
                'mobile': '18511116212',
            },
            'data': {
                "result": "11",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'tianwang_multi_loan',
                'mobile': '18511116218',
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'tianwang_multi_loan',
                'mobile': '13488898888 ',
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'tianwang_multi_loan',
                'mobile': '13901395838',
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'tianwang_multi_loan',
                'mobile': '13901328888',
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
    ],
    'tianyan_black': [
        {
            'args': {
                'data_identity': 'tianyan_black',
                'email': '123@163.com',
                'id_card_code': '132600198906251568',
                'mobile': '13311538888'
            },
            'data': {
                "result": "11",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'tianyan_black',
                'email': '123@164.com',
                'id_card_code': '132600198906251569',
                'mobile': '18910592066'
            },
            'data': {
                "result": "11",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'tianyan_black',
                'email': '123@165.com',
                'id_card_code': '132600198906251570',
                'mobile': '18911970588'
            },
            'data': {
                "result": "22",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'tianyan_black',
                'email': '123@166.com',
                'id_card_code': '132600198906251571',
                'mobile': '18511116256'
            },
            'data': {
                "result": "22",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'tianyan_black',
                'email': '123@167.com',
                'id_card_code': '132600198906251572',
                'mobile': '18511116277'
            },
            'data': {
                "result": "44",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'tianyan_black',
                'email': '123@168.com',
                'id_card_code': '132600198906251573',
                'mobile': '18511116212'
            },
            'data': {
                "result": "44",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'tianyan_black',
                'email': '123@169.com',
                'id_card_code': '132600198906251574',
                'mobile': '18511116218'
            },
            'data': {
                "result": "33",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'tianyan_black',
                'email': '123@170.com',
                'id_card_code': '132600198906251575',
                'mobile': '13488898888 '
            },
            'data': {
                "result": "33",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'tianyan_black',
                'email': '123@171.com',
                'id_card_code': '132600198906251576',
                'mobile': '13901395838'
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'tianyan_black',
                'email': '123@172.com',
                'id_card_code': '132600198906251577',
                'mobile': '13901328888'
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
    ],
    'court_shixin_a_s': [
        {
            'args': {
                'data_identity': 'court_shixin_a_s',
                'entity_name': '璐璐1',
                'entity_id': '132600198906251568',
            },
            'data': {
                "result": "11",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'court_shixin_a_s',
                'entity_name': '璐璐2',
                'entity_id': '132600198906251569',
            },
            'data': {
                "result": "11",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'court_shixin_a_s',
                'entity_name': '璐璐3',
                'entity_id': '132600198906251570',
            },
            'data': {
                "result": "22",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'court_shixin_a_s',
                'entity_name': '璐璐4',
                'entity_id': '132600198906251571',
            },
            'data': {
                "result": "22",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'court_shixin_a_s',
                'entity_name': '璐璐5',
                'entity_id': '132600198906251572',
            },
            'data': {
                "result": "44",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'court_shixin_a_s',
                'entity_name': '璐璐6',
                'entity_id': '132600198906251573',
            },
            'data': {
                "result": "44",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'court_shixin_a_s',
                'entity_name': '璐璐7',
                'entity_id': '132600198906251574',
            },
            'data': {
                "result": "33",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'court_shixin_a_s',
                'entity_name': '璐璐8',
                'entity_id': '132600198906251575',
            },
            'data': {
                "result": "33",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'court_shixin_a_s',
                'entity_name': '璐璐9',
                'entity_id': '132600198906251576',
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'court_shixin_a_s',
                'entity_name': '璐璐x',
                'entity_id': '132600198906251577',
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
    ],
    'net_black_a_s': [
        {
            'args': {
                'data_identity': 'net_black_a_s',
                'id_card_name': '璐璐1',
                'id_card_code': '132600198906251568',
            },
            'data': {
                "result": "11",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'net_black_a_s',
                'id_card_name': '璐璐2',
                'id_card_code': '132600198906251569',
            },
            'data': {
                "result": "11",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'net_black_a_s',
                'id_card_name': '璐璐3',
                'id_card_code': '132600198906251570',
            },
            'data': {
                "result": "22",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'net_black_a_s',
                'id_card_name': '璐璐4',
                'id_card_code': '132600198906251571',
            },
            'data': {
                "result": "22",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'net_black_a_s',
                'id_card_name': '璐璐5',
                'id_card_code': '132600198906251572',
            },
            'data': {
                "result": "44",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'net_black_a_s',
                'id_card_name': '璐璐6',
                'id_card_code': '132600198906251573',
            },
            'data': {
                "result": "44",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'net_black_a_s',
                'id_card_name': '璐璐7',
                'id_card_code': '132600198906251574',
            },
            'data': {
                "result": "33",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'net_black_a_s',
                'id_card_name': '璐璐8',
                'id_card_code': '132600198906251575',
            },
            'data': {
                "result": "33",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'net_black_a_s',
                'id_card_name': '璐璐9',
                'id_card_code': '132600198906251576',
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'net_black_a_s',
                'id_card_name': '璐璐x',
                'id_card_code': '132600198906251577',
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
    ],
    'negative_info_s': [
        {
            'args': {
                'data_identity': 'negative_info_s',
                'id_card_name': '璐璐1',
                'id_card_code': '132600198906251568',
            },
            'data': {
                "result": "11",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'negative_info_s',
                'id_card_name': '璐璐2',
                'id_card_code': '132600198906251569',
            },
            'data': {
                "result": "11",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'negative_info_s',
                'id_card_name': '璐璐3',
                'id_card_code': '132600198906251570',
            },
            'data': {
                "result": "22",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'negative_info_s',
                'id_card_name': '璐璐4',
                'id_card_code': '132600198906251571',
            },
            'data': {
                "result": "22",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'negative_info_s',
                'id_card_name': '璐璐5',
                'id_card_code': '132600198906251572',
            },
            'data': {
                "result": "44",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'negative_info_s',
                'id_card_name': '璐璐6',
                'id_card_code': '132600198906251573',
            },
            'data': {
                "result": "44",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'negative_info_s',
                'id_card_name': '璐璐7',
                'id_card_code': '132600198906251574',
            },
            'data': {
                "result": "33",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'negative_info_s',
                'id_card_name': '璐璐8',
                'id_card_code': '132600198906251575',
            },
            'data': {
                "result": "33",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'negative_info_s',
                'id_card_name': '璐璐9',
                'id_card_code': '132600198906251576',
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'negative_info_s',
                'id_card_name': '璐璐x',
                'id_card_code': '132600198906251577',
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
    ],
    'tianwang_gray': [
        {
            'args': {
                'data_identity': 'tianwang_gray',
                'mobile': '13311538888',
            },
            'data': {
                "result": "11",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'tianwang_gray',
                'mobile': '18910592066',
            },
            'data': {
                "result": "11",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'tianwang_gray',
                'mobile': '18911970588',
            },
            'data': {
                "result": "11",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'tianwang_gray',
                'mobile': '18511116256',
            },
            'data': {
                "result": "22",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'tianwang_gray',
                'mobile': '18511116277',
            },
            'data': {
                "result": "33",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'tianwang_gray',
                'mobile': '18511116212',
            },
            'data': {
                "result": "11",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'tianwang_gray',
                'mobile': '18511116218',
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'tianwang_gray',
                'mobile': '13488898888 ',
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'tianwang_gray',
                'mobile': '13901395838',
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'tianwang_gray',
                'mobile': '13901328888',
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
    ],
    'court_zhixing_a_s': [
        {
            'args': {
                'data_identity': 'court_zhixing_a_s',
                'entity_name': '璐璐1',
                'entity_id': '132600198906251568',
            },
            'data': {
                "result": "11",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'court_zhixing_a_s',
                'entity_name': '璐璐2',
                'entity_id': '132600198906251569',
            },
            'data': {
                "result": "11",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'court_zhixing_a_s',
                'entity_name': '璐璐3',
                'entity_id': '132600198906251570',
            },
            'data': {
                "result": "22",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'court_zhixing_a_s',
                'entity_name': '璐璐4',
                'entity_id': '132600198906251571',
            },
            'data': {
                "result": "22",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'court_zhixing_a_s',
                'entity_name': '璐璐5',
                'entity_id': '132600198906251572',
            },
            'data': {
                "result": "44",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'court_zhixing_a_s',
                'entity_name': '璐璐6',
                'entity_id': '132600198906251573',
            },
            'data': {
                "result": "44",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'court_zhixing_a_s',
                'entity_name': '璐璐7',
                'entity_id': '132600198906251574',
            },
            'data': {
                "result": "33",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'court_zhixing_a_s',
                'entity_name': '璐璐8',
                'entity_id': '132600198906251575',
            },
            'data': {
                "result": "33",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'court_zhixing_a_s',
                'entity_name': '璐璐9',
                'entity_id': '132600198906251576',
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
        {
            'args': {
                'data_identity': 'court_zhixing_a_s',
                'entity_name': '璐璐x',
                'entity_id': '132600198906251577',
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": []
            }
        },
    ],
    'telecom_mobile_online_time_s': [
        {
            'args': {
                'data_identity': 'telecom_mobile_online_time_s',
                'mobile': '13311538888',
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                    "online_time": "[0-6)"
                },
            }
        },
        {
            'args': {
                'data_identity': 'telecom_mobile_online_time_s',
                'mobile': '18910592066',
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                    "online_time": "[6-12)"
                },
            }
        },
        {
            'args': {
                'data_identity': 'telecom_mobile_online_time_s',
                'mobile': '18911970588',
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                    "online_time": "[12-24)"
                },
            }
        },
    ],
    'unicome_mobile_online_time_s': [
        {
            'args': {
                'data_identity': 'unicome_mobile_online_time_s',
                'mobile': '18511116256',
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                    "online_time": "[0-1]"
                },
            }
        },
        {
            'args': {
                'data_identity': 'unicome_mobile_online_time_s',
                'mobile': '18511116277',
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                    "online_time": "(1-2]"
                },
            }
        },
        {
            'args': {
                'data_identity': 'unicome_mobile_online_time_s',
                'mobile': '18511116212',
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                    "online_time": "[3-6]"
                },
            }
        },
        {
            'args': {
                'data_identity': 'unicome_mobile_online_time_s',
                'mobile': '18511116218',
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                    "online_time": "[7-12]"
                },
            }
        },
    ],
    'yd_mobile_online_time_s': [
        {
            'args': {
                'data_identity': 'yd_mobile_online_time_s',
                'mobile': '13488898888 ',
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                    "online_time": "[3,6)"
                },
            }
        },
        {
            'args': {
                'data_identity': 'yd_mobile_online_time_s',
                'mobile': '13901395838',
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                    "online_time": "(0,3)"
                },
            }
        },
        {
            'args': {
                'data_identity': 'yd_mobile_online_time_s',
                'mobile': '13901328888',
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                    "online_time": "[6,12)"
                },
            }
        },
    ],
    'telecom_mobile_identity_s': [
        {
            'args': {
                'data_identity': 'telecom_mobile_identity_s',
                'id_card_name': '璐璐1',
                'id_card_code': '132600198906251568',
                'mobile': '13311538888'
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                },
            }
        },
        {
            'args': {
                'data_identity': 'telecom_mobile_identity_s',
                'id_card_name': '璐璐2',
                'id_card_code': '132600198906251569',
                'mobile': '18910592066'
            },
            'data': {
                "result": "11",
                "result_message": "检测通过或查询有记录",
                "content": {
                },
            }
        },
        {
            'args': {
                'data_identity': 'telecom_mobile_identity_s',
                'id_card_name': '璐璐3',
                'id_card_code': '132600198906251570',
                'mobile': '18911970588'
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                },
            }
        },
    ],
    'unicom_mobile_identity_s': [
        {
            'args': {
                'data_identity': 'unicom_mobile_identity_s',
                'id_card_name': '璐璐4',
                'id_card_code': '132600198906251571',
                'mobile': '18511116256'
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {},
            }
        },
        {
            'args': {
                'data_identity': 'unicom_mobile_identity_s',
                'id_card_name': '璐璐5',
                'id_card_code': '132600198906251572',
                'mobile': '18511116277'
            },
            'data': {
                "result": "11",
                "result_message": "检测通过或查询有记录",
                "content": {},
            }
        },
        {
            'args': {
                'data_identity': 'unicom_mobile_identity_s',
                'id_card_name': '璐璐6',
                'id_card_code': '132600198906251573',
                'mobile': '18511116212'
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {},
            }
        },
        {
            'args': {
                'data_identity': 'unicom_mobile_identity_s',
                'id_card_name': '璐璐7',
                'id_card_code': '132600198906251574',
                'mobile': '18511116218'
            },
            'data': {
                "result": "11",
                "result_message": "检测通过或查询有记录",
                "content": {},
            }
        },
    ],
    'yd_mobile_identity_s': [
        {
            'args': {
                'data_identity': 'yd_mobile_identity_s',
                'id_card_name': '璐璐8',
                'id_card_code': '132600198906251575',
                'mobile': '13488898888'
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {},
            }
        },
        {
            'args': {
                'data_identity': 'yd_mobile_identity_s',
                'id_card_name': '璐璐9',
                'id_card_code': '132600198906251576',
                'mobile': '13901395838'
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {},
            }
        },
        {
            'args': {
                'data_identity': 'yd_mobile_identity_s',
                'id_card_name': '璐璐x',
                'id_card_code': '132600198906251577',
                'mobile': '13901328888'
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {},
            }
        },
    ],
    'airline_passenger_info': [
        {
            'args': {
                'data_identity': 'airline_passenger_info',
                'id_card_name': '璐璐1',
                'id_card_code': '132600198906251568',
            },
            'data': {
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
            'args': {
                'data_identity': 'airline_passenger_info',
                'id_card_name': '璐璐2',
                'id_card_code': '132600198906251569',
            },
            'data': {
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
                    "average_price": 256.5,
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
            'args': {
                'data_identity': 'airline_passenger_info',
                'id_card_name': '璐璐3',
                'id_card_code': '132600198906251570',
            },
            'data': {
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
            'args': {
                'data_identity': 'airline_passenger_info',
                'id_card_name': '璐璐4',
                'id_card_code': '132600198906251571',
            },
            'data': {
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
        {
            'args': {
                'data_identity': 'airline_passenger_info',
                'id_card_name': '璐璐5',
                'id_card_code': '132600198906251572',
            },
            'data': {
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
            }
        },
        {
            'args': {
                'data_identity': 'airline_passenger_info',
                'id_card_name': '璐璐6',
                'id_card_code': '132600198906251573',
            },
            'data': {
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
                    "tourist_class_count": 0,
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
            'args': {
                'data_identity': 'airline_passenger_info',
                'id_card_name': '璐璐7',
                'id_card_code': '132600198906251574',
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                    "id_card_name": "吴*",
                    "id_card_code": "513722198908***43X",
                    "flight_times": 2,
                    "flight_month": "201502",
                    "flight_max": 2,
                    "average_discount": 100,
                    "business_class_count": 3,
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
        {
            'args': {
                'data_identity': 'airline_passenger_info',
                'id_card_name': '璐璐8',
                'id_card_code': '132600198906251575',
            },
            'data': {
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
                    "executive_class_count": 5,
                    "tourist_class_count": 4,
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
            'args': {
                'data_identity': 'airline_passenger_info',
                'id_card_name': '璐璐9',
                'id_card_code': '132600198906251576',
            },
            'data': {
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
                    "executive_class_count": 3,
                    "tourist_class_count": 4,
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
            'args': {
                'data_identity': 'airline_passenger_info',
                'id_card_name': '璐璐x',
                'id_card_code': '132600198906251577',
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                    "id_card_name": "吴*",
                    "id_card_code": "513722198908***43X",
                    "flight_times": 2,
                    "flight_month": "201502",
                    "flight_max": 2,
                    "average_discount": 100,
                    "business_class_count": '',
                    "executive_class_count": 3,
                    "tourist_class_count": 4,
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
    ],
    'unicom_finance_portrait_s': [
        {
            'args': {
                'data_identity': 'unicom_finance_portrait_s',
                'mobile': '18511116256'
            },
            'data': {
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
        }
    ],
    'multi_id_card_info_s': [
        {
            'args': {
                'data_identity': 'multi_id_card_info_s',
            },
            'data': {
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
            }
        }
    ],
    'industrial_commercial_s': [
        {
            'args': {
                'data_identity': 'industrial_commercial_s',
                'enterprise_name': 'GE Wuhan Boiler CO,. Ltd.'
            },
            'data': {
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
        }
    ],
    'education_review_s': [
        {
            'args': {
                'data_identity': 'education_review_s',
                'id_card_name': '璐璐1',
                'id_card_code': '132600198906251568',
            },
            'data': {
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
        }
    ],
    'loan_history': [
        {
            'args': {
                'data_identity': 'loan_history',
                'card_id': '132600198906251568',
            },
            'data': {
                'status': 1,
                'message': '操作成功',
                'res_data': {
                    'is_unclear_loan': 2,
                },
            }
        }
    ],
    'mobile_locale': [
        {
            'args': {
                'data_identity': 'mobile_locale',
                'mobile': '13311538888',
            },
            'data': {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                    "mobile_area": "北京市",
                },
            }
        }
    ],
}

data = {
    'trustutn_loan_overdue': {
        'args': {
            'data_identity': 'trustutn_loan_overdue',
        },
        'data': {

        }
    },
    'trustutn_loan_blacklist': {
        'args': {
            'data_identity': 'trustutn_loan_blacklist',
        },
        'data': {

        }
    },
    'multi_loan_91': {
        'args': {
            'data_identity': 'multi_loan_91',
        },
        'data': {

        }
    },
    'trustutn_loan_loanmsg': {
        'args': {
            'data_identity': 'trustutn_loan_loanmsg',
        },
        'data': {

        }
    },
    'trustutn_loan_phone': {
        'args': {
            'data_identity': 'trustutn_loan_phone',
        },
        'data': {

        }
    },
    'cc_credit': {
        'args': {
            'data_identity': 'cc_credit',
        },
        'data': {

        }
    },
    'trustutn_loan_otheragent': {
        'args': {
            'data_identity': 'trustutn_loan_otheragent',
        },
        'data': {

        }
    },
}

unuse_data = {
    'high_way_over_speed': {
        'args': {
            'data_identity': 'high_way_over_speed',
        },
        'data': {

        }
    },
    'high_way_over_load': {
        'args': {
            'data_identity': 'high_way_over_load',
        },
        'data': {

        }
    },
    'cc_car_credit': {
        'args': {
            'data_identity': 'cc_car_credit',
        },
        'data': {

        }
    },
}

conn = pymongo.MongoClient('192.168.1.198', 27017)
coll = conn['feature_storage']['test_data']
keys = data.keys()
num = 0
for key in keys:
    temp_data = data[key]
    for i in temp_data:
        # coll.insert_one(i)
        num += 1

print num

