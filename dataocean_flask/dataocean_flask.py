# -*- coding:utf-8 -*-

import json
import sys

import requests

reload(sys)
sys.setdefaultencoding('utf-8')
import sys
import os

path = os.path.dirname(__file__)
sys.path.append(path)

from flask import Flask, jsonify, request

from encrypt import Cryption
from setting import *

app = Flask(__name__)


def do_request(url, data, des_key):
    json_data = json.dumps(data, encoding="UTF-8", ensure_ascii=False)
    req_data = Cryption.aes_base64_encrypt(json_data, des_key)
    print url, req_data
    content = requests.post(url, json.dumps({"req_data": req_data,
                                             "client": client_id},
                                            encoding="UTF-8", ensure_ascii=False)).content
    content = json.loads(content)
    if content.get('res_data', None):
        content['res_data'] = Cryption.aes_base64_decrypt(content['res_data'], des_key)
    return content


def get_token(url, client_secret):
    grant_type = "client_credentials"
    datas = dict(grant_type=grant_type,
                 client_secret=client_secret,
                 )
    content = do_request(url, datas, des_key)
    token = json.loads(content['res_data'])
    return token


@app.route('/api/rule/gateway/<data_identity>/', methods=['POST'])
def post(data_identity):
    data = {
        "status": 1,
        "message": "success"
    }
    content = {}
    try:
        if data_identity == 'cc_car_credit':
            content = {
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
                    {"license_no": "豫SFD777"},
                    {"license_no": "豫SFD888"},
                    {"license_no": "ASFD456"},
                    {"license_no": "京SFD45"},

                ]
            }
        elif data_identity == 'cc_credit':
            content = {
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
            }
        elif data_identity == 'loan_agency':
            content = {
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
            content = {'res_data': json.dumps(content), 'status': 0, 'message': 'success'}
        elif data_identity == 'multi_loan_91':
            content = {
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
                                     "orgNums": 1, "loanAmount": None, "totalAmount": "(200, 500]",
                                     "repayAmount": None},
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
            }
            content = {
    'loanInfos': [
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
    ]
    }
        elif data_identity == 'trustutn_loan_blacklist':
            content = {
    'data':
        {
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
    }
        elif data_identity == 'trustutn_loan_phone':
            content = {
                "result": 0,
                "message": "",
                "data": {
                    "commonContacts":
                        {
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
                    "directCall":
                        {
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
                    "grayscale":
                        {
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
                    "interactCommons":
                        {
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
                            "13820019795_8a404758b8f8b87c70006b8e9f4614db_":
                                {
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
        elif data_identity == 'trustutn_loan_overdue':
            content = {
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
    }
        elif data_identity == 'trustutn_loan_loanmsg':
            content = {
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
                     }},
                 {
                     "M9": {
                         "other": {"orgNums": 1, "loanAmount": None, "totalAmount": "(0, 200]",
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
                         "other": {"orgNums": 2, "loanAmount": None, "totalAmount": "(1000, 2000]",
                                   "repayAmount": None},
                         "bank": None,
                     }}
             ]
             }
        ],
        "phone": "18627180708",
        "imei": "",
        "imsi": ""}}
        elif data_identity == 'trustutn_loan_otheragent':
            content = {
    "result": 0,
    "message": None,
    "data": {
        "201603": {
            "orgNums": "23",
            "queryNums": "123"
        },
        "201602": None,
        "201601": {
            "orgNums": 123,
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
        },
        "201509": {
            "orgNums": "22",
            "queryNums": "123"
        },
        "201508": {
            "orgNums": "",
            "queryNums": "123"
        },
        "201507": {
            "orgNums": "",
            "queryNums": ""
        },
        "201506": {
            "orgNums": "20",
            "queryNums": "123"
        },
        "201505": {
            "orgNums": None,
            "queryNums": "123"
        },
        "201504": {
            "orgNums": None,
            "queryNums": None
        }
    }
    }
        # if True:
        else:
            req_data = json.loads(request.data)['req_data']
            req_data.update({'data_identity': data_identity})
            token = get_token(dataocean_url_grant, client_secret)
            req_data.update({"access_token": token["access_token"]})
            content = do_request(dataocean_url_data, req_data, des_key)
        # print content
        data.update({"res_data": content})

    except Exception, e:
        # print e.message
        data.update({
            'status': 0,
            'message': e.message
        })
    return jsonify(data)


@app.route('/api/rule/gateway/async/<data_identity>/', methods=['POST'])
def async_post(data_identity):
    data = {
        "status": 0,
        "message": "success"
    }
    req_data = json.loads(request.data)
    print req_data
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8987)
    """
    http://192.168.1.196:8987/api/rule/gateway/court_zhixing_a_s/  post
    data = {"client_token": "test_lp_syph_code", "req_data": {"entity_id": "433031196210056032", "entity_name": "吴永荣"}}

    """

