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
    from apply_base import apply_data

    call_back = "http://de.digcredit.com:8071/api/async/result/"
    for i in apply_data[:-1]:
        data = i["data"]
        bank_card_upload = data.get("bank_card_upload", {})
        if not bank_card_upload:
            continue
        json_ = {
            "product_code": "cf5b6d062260f643d123ae61a37fe416",
            "name": data.get("name",''),
            "mobile": data.get("mobile",''),
            "data_identity": "",
            "apply_id": "",
            "card_id": data.get("card_id",''),
            "scan_code_city": data.get("scanCodeCity",''),
            "san_code_time": data.get("san_code_time",''),
            "gps_longitude": data.get("gpsLongitude",''),
            "gps_latitude": data.get("gpsLatitude",''),
            "product_version": "P045-v01.1125",
            "validation_status": "True",
            "call_back": call_back,
        }

        # domain = 'http://127.0.0.1:10012'
        domain = 'http://de.digcredit.com:8071'
        # domain = 'http://192.168.1.100:8071'

        test_case = Cases()
        content = test_case.test_credit_audit()
        print content
        apply_id = content["res_data"]["apply_id"]
        json_bank_card_upload = {"apply_id": apply_id,
                                 "message": bank_card_upload,
                                 "call_back": call_back,
                                 "product_code": "cf5b6d062260f643d123ae61a37fe416", "data_identity": "bank_card_upload"}

        # 最后
        json_final_upload = {
            'product_code': 'cf5b6d062260f643d123ae61a37fe416',
            'apply_id': apply_id,
            'data_identity': 'final_upload',
            "message": {
                "receive_address": data.get("final_upload", {}).get("receive_address"),
            "call_back": call_back
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

