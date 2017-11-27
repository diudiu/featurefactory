# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH(Shaohan Niu), All Rights Reserved.
    -----------------------------------------------------------
    Author: Shaohan Niu
    Date:  2016/2/14
    Change Activity:

"""
from __future__ import unicode_literals
import requests
import json
import time


class Cases(object):
    credit_audit_url = '/api/credit/apply/'
    obtain_result_url = '/api/credit/result/'
    receive_result_url = '/api/async/result/'

    def test_credit_audit(self):
        url = '%s%s' % (domain, self.credit_audit_url)
        headers = {
            "Content-type": "application/json; charset=utf-8",
        }
        print url
        response = requests.post(url, headers=headers, data=json.dumps(json_))
        print response.content
        a = json.loads(response.content)
        return a

    def test_obtain_result(self):
        uri = '/api/credit/result/'
        url = '%s%s' % (domain, uri)
        json_ = {
            'product_code': 'cf5b6d062260f643d123ae61a37fe416',
            'apply_id': apply_id
        }
        session = requests.session()
        resp = session.request('GET', url, params=json_,
                               headers={'content-type': 'application/json;charset=utf-8'})
        print resp.url
        print resp.content


def async_post():
    # url = 'http://139.129.220.118:8000/api/async/callback/'
    url = '%s/api/async/callback/' % domain
    json_ = appjson
    headers = {
        "Content-type": "application/json; charset=utf-8",
    }
    response = requests.post(url, headers=headers, data=json.dumps(json_))
    print response.content


if __name__ == '__main__':
    # json_ = {
    #     'product_code': 'cf5b6d062260f643d123ae61a37fe416',
    #     "name": "张娜",
    #     "mobile": "15652375668",
    #     'data_identity': '',
    #     'apply_id': '',
    #     'card_id': '120222198208052620',
    #     'scan_code_city': '西安',
    #     'san_code_time': time.time(),
    #     'gps_longitude': '108.85492143460725',
    #     'gps_latitude': '34.198012456599415',
    #     "product_version": "P045-v01.1125",
    #     "validation_status": True,
    # }
    # json_ = {u'scan_code_city': u'\u5409\u6797', u'name': u'\u738b\u4e16\u4e3d', u'validation_status': True,
    #          u'mobile': u'13679211845', 'product_version': u'P045-v01.1125', u'san_code_time': u'1503972559',
    #          u'card_id': u'610626199112290921', u'apply_id': u'', u'gps_latitude': u'',
    #          u'product_code': u'cf5b6d062260f643d123ae61a37fe416', u'gps_longitude': u''}
    # json_ = {u'scan_code_city': u'\u5409\u6797', u'name': u'\u5218\u5e73\u5b87', u'validation_status': True,
    #          u'mobile': u'13910135048', 'product_version': u'P045-v01.1125', u'san_code_time': u'1503547926',
    #          u'card_id': u'511026197510304714', u'apply_id': u'', u'gps_latitude': 34.200490027310536,
    #          u'product_code': u'cf5b6d062260f643d123ae61a37fe416', u'gps_longitude': 108.85090802942125}
    # json_ = {
    #     "product_code": "cf5b6d062260f643d123ae61a37fe416",
    #     "name": "宋晓颖",
    #     "mobile": "13716315381",
    #     "data_identity": "",
    #     "apply_id": "",
    #     "card_id": "411626199202213528",
    #     "scan_code_city": "吉林",
    #     "san_code_time": 1504771099,
    #     "gps_longitude": "",
    #     "gps_latitude": "",
    #     "product_version": "P045-v01.1125",
    #     "validation_status": "True"
    # }
    call_back = "http://de.digcredit.com:8071/api/async/result/"
    # call_back = "http://127.0.0.1:10012/api/async/result/"
    json_ = {
        "product_code": "cf5b6d062260f643d123ae61a37fe416",
        "name": "董立强",
        "mobile": "15201293718",
        "data_identity": "",
        "apply_id": "",
        "card_id": "610103199305292032",
        "scan_code_city": "吉林",
        "san_code_time": 1504771099,
        "gps_longitude": u'116.382324',
        "gps_latitude": u'39.957206',
        "product_version": "P045-v01.1125",
        "validation_status": "True",
        "call_back": call_back

    }

    # domain = 'http://127.0.0.1:10012'
    domain = 'http://de.digcredit.com:8071'
    # domain = 'http://192.168.1.100:8071'

    test_case = Cases()
    content = test_case.test_credit_audit()
    print content
    apply_id = content["res_data"]["apply_id"]

    json_bank_card_upload = {"apply_id": apply_id,
                             "call_back": call_back,
                             "message": {u'bank_card_number': u'6226890085988409',
                                         u'hit': u'no',
                                         u'risk_list': [],
                                         u'antifraud_score': 100,
                                         u'union_pay_data': {u'CDTT092': u'9', u'CDTB122': u'1', u'CDTT097': u'0',
                                                             u'CDTT094': u'0', u'CDTB061': u'600.9',
                                                             u'CDTB004': u'7210.8', u'CDCA003': u'01',
                                                             u'CDTB064': u'1.0', u'CDTB065': u'600.9',
                                                             u'CDTB066': u'1.0', u'CDMC136': u'0', u'CDTC048': u'2',
                                                             u'CDMC133': u'0', u'CDMC260': u'937.9',
                                                             u'CDMC113': u'1647.9', u'CDTT079': u'2827.9',
                                                             u'CDTB230': u'4200', u'CDTB296': u'1', u'CDTB292': u'4200',
                                                             u'CDTB019': u'12', u'CDTT027': u'0', u'CDTC050': u'12',
                                                             u'CDTB268': u'\u5317\u4eac\u5e02', u'CDTT040': u'0',
                                                             u'CDTT106': u'964.5', u'CDTC035': u'7210.8',
                                                             u'CDTB260': u'1', u'CSWC002': u'6', u'CDTB045': u'0',
                                                             u'CSRL003': u'579', u'CSRL001': u'343'}},
                             "product_code": "cf5b6d062260f643d123ae61a37fe416",
                             "data_identity": "bank_card_upload"}

    # 最后
    json_final_upload = {
        'product_code': 'cf5b6d062260f643d123ae61a37fe416',
        'apply_id': apply_id,
        "call_back": call_back,
        'data_identity': 'final_upload',
        "message": {
            "receive_address": "北京市朝阳区大屯路洛克时代"
        }
    }
    s = 5
    time.sleep(s)
    appjson = json_bank_card_upload
    async_post()
    time.sleep(s)
    # test_case.test_obtain_result()
    # time.sleep(s)
    appjson = json_final_upload
    async_post()
    # time.sleep(s)
    # test_case.test_obtain_result()

