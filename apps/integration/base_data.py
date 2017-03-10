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
}

data = {
    'unicom_finance_portrait_s': {
        'args': {

        },
        'data': {

        }
    },
    'multi_id_card_info_s': {
        'args': {

        },
        'data': {

        }
    },
    'industrial_commercial_s': {
        'args': {

        },
        'data': {

        }
    },
    'education_review_s': {
        'args': {

        },
        'data': {

        }
    },
    'loan_history': {
        'args': {

        },
        'data': {

        }
    },
    'mobile_locale': {
        'args': {

        },
        'data': {

        }
    },
}

unuse_data = {
    'high_way_over_speed': {
        'args': {

        },
        'data': {

        }
    },
    'high_way_over_load': {
        'args': {

        },
        'data': {

        }
    },
    'trustutn_loan_overdue': {
        'args': {

        },
        'data': {

        }
    },
    'trustutn_loan_blacklist': {
        'args': {

        },
        'data': {

        }
    },
    'multi_loan_91': {
        'args': {

        },
        'data': {

        }
    },
    'trustutn_loan_loanmsg': {
        'args': {

        },
        'data': {

        }
    },
    'trustutn_loan_phone': {
        'args': {

        },
        'data': {

        }
    },
    'cc_credit': {
        'args': {

        },
        'data': {

        }
    },
    'cc_car_credit': {
        'args': {

        },
        'data': {

        }
    },
    'trustutn_loan_otheragent': {
        'args': {

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
        num += 1

print num

