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
    domain = 'http://139.129.220.118:10012'
    # domain = 'http://118.190.81.178:8888'
    # domain = 'http://127.0.0.1:9999'
    credit_audit_url = '/api/credit/apply/'
    obtain_result_url = '/api/credit/result/'
    receive_result_url = '/api/async/result/'

    def test_credit_audit(self):
        url = '%s%s' % (self.domain, self.credit_audit_url)
        json_ = {
            'product_code': 'cf5b6d062260f643d123ae61a37fe416',
            "name": "张娜",
            "mobile": "15652375668",
            'data_identity': '',
            'apply_id': '',
            'card_id': '120222198208052620',
            'scan_code_city': '西安',
            'san_code_time': time.time(),
            'gps_longitude': '108.85492143460725',
            'gps_latitude': '34.198012456599415',
            "product_version": "P045-v01.1125",
            "validation_status": True,
        }
        headers = {
            "Content-type": "application/json; charset=utf-8",
        }
        response = requests.post(url, headers=headers, data=json.dumps(json_))
        a = json.loads(response.content)

    def test_obtain_result(self):
        uri = '/api/credit/result/'
        url = '%s%s' % (self.domain, uri)
        json_ = {
            'product_code': 'cf5b6d062260f643d123ae61a37fe416',
            'apply_id': "APPLY20170721161004031679"
        }
        session = requests.session()
        resp = session.request('GET', url, params=json_,
                               headers={'content-type': 'application/json;charset=utf-8'})
        print resp.url
        print resp.content

    def test_list_result(self):
        uri = '/api/credit/result/'
        url = '%s%s' % (self.domain, uri)
        apply_list = [
            'APPLY20161110115751704001',
            'APPLY20161110115751704002',
            'APPLY20161110115751704003',
            'APPLY20161110115751704004',
            'APPLY20161110115751704005',
            'APPLY20161110115751704006',
            'APPLY20161110115751704007',
            'APPLY20161110115751704008',
            'APPLY20161110115751704009',
            'APPLY20161110115751704010',
            'APPLY20161110115751704011',
            'APPLY20161110115751704012',
            'APPLY20161110115751704013',
            'APPLY20161110115751704014',
            'APPLY20161110115751704015',
            'APPLY20161110115751704016',
        ]
        for apply_id in apply_list:
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
    url = 'http://127.0.0.1:9999/api/async/callback/'
    json_ = {
        'product_code': 'cf5b6d062260f643d123ae61a37fe416',
        'apply_id': 'APPLY20161228160919829153',
        'data_identity': 'bank_card_upload',
        'message': {
            'select_address': '陕西省咸阳市',
            'receive_address': u'陕西省 铜川市 宜君区',
        }
    }
    headers = {
        "Content-type": "application/json; charset=utf-8",
    }
    response = requests.post(url, headers=headers, data=json.dumps(json_))
    print response.content


def all_step_test():
    # audit_api = 'http://127.0.0.1:9999/api/credit/apply/'
    # result_api = 'http://127.0.0.1:9999/api/credit/result/'
    # callback_api = 'http://127.0.0.1:9999/api/async/callback/'
    audit_api = 'http://139.129.220.118:10012/api/credit/apply/'
    result_api = 'http://139.129.220.118:10012/api/credit/result/'
    callback_api = 'http://139.129.220.118:10012/api/async/callback/'
    # 第一次授信
    json_ = {
        'product_code': 'cf5b6d062260f643d123ae61a37fe416',
        'data_identity': '',
        'apply_id': '',
        'name': '尚刚',
        'card_id': '371422199311137713',
        'mobile': '18811436445',
        'gps_longitude': '116.401361',
        'gps_latitude': '40.000479',
        'select_address': '陕西省咸阳市',
        'san_code_time': '',
        'san_code_loc': '',
    }
    response = requests.post(audit_api, data=json_)
    print response.content
    res_data = eval(response.content)
    if res_data['status'] == 1:
        apply_id = res_data['res_data']['apply_id']
    else:
        return
    # 获取结果
    print 'I sleep'
    json_ = {
        'product_code': 'cf5b6d062260f643d123ae61a37fe416',
        'apply_id': apply_id,
    }
    session = requests.session()
    resp = session.request('GET', result_api, params=json_,
                           headers={'content-type': 'application/json;charset=utf-8'})
    print resp.url
    print resp.content
    # 银联报告
    data = {
        'product_code': 'cf5b6d062260f643d123ae61a37fe416',
        'apply_id': apply_id,
        'data_identity': 'bank_card_upload',
        'message': {
            'bank_card_number': u'6222370193771314',
        }
    }
    headers = {
        "Content-type": "application/json; charset=utf-8",
    }
    response = requests.post(callback_api, headers=headers, data=json.dumps(data))
    # 获取结果
    json_ = {
        'product_code': 'cf5b6d062260f643d123ae61a37fe416',
        'apply_id': apply_id,
    }
    session = requests.session()
    resp = session.request('GET', result_api, params=json_,
                           headers={'content-type': 'application/json;charset=utf-8'})
    print resp.url
    print resp.content
    # 邮箱抓取
    data = {
        'product_code': 'cf5b6d062260f643d123ae61a37fe416',
        'apply_id': apply_id,
        'data_identity': 'email_dig_upload',
        'message': {
            'credit_card_number': u'6222370193771314',
            'credit_limit': 30000,
            'available_balance': 26000,
        }
    }
    headers = {
        "Content-type": "application/json; charset=utf-8",
    }
    response = requests.post(callback_api, headers=headers, data=json.dumps(data))
    # 获取结果
    json_ = {
        'product_code': 'cf5b6d062260f643d123ae61a37fe416',
        'apply_id': apply_id,
    }
    session = requests.session()
    resp = session.request('GET', result_api, params=json_,
                           headers={'content-type': 'application/json;charset=utf-8'})
    print resp.url
    print resp.content
    # 邮箱抓取
    data = {
        'product_code': 'cf5b6d062260f643d123ae61a37fe416',
        'apply_id': apply_id,
        'data_identity': 'operator_dig_upload',
        'message': {
            'phone_remain': 50.1,
            'phone_list': ['734863463', '734863463', '734863463', '734863463', '554324364'],
            'call_pay_list': [95.4, 58, 64, 85, 69]
        }
    }
    headers = {
        "Content-type": "application/json; charset=utf-8",
    }
    response = requests.post(callback_api, headers=headers, data=json.dumps(data))
    # 获取结果
    json_ = {
        'product_code': 'cf5b6d062260f643d123ae61a37fe416',
        'apply_id': apply_id,
    }
    session = requests.session()
    resp = session.request('GET', result_api, params=json_,
                           headers={'content-type': 'application/json;charset=utf-8'})
    print resp.url
    print resp.content
    # 最后
    data = {
        'product_code': 'cf5b6d062260f643d123ae61a37fe416',
        'apply_id': apply_id,
        'data_identity': 'final_upload',
        'message': {
            'receive_address': u'陕西省西安市陕国贸6阿奴也风光',
        },
    }
    headers = {
        "Content-type": "application/json; charset=utf-8",
    }
    response = requests.post(callback_api, headers=headers, data=json.dumps(data))
    # 获取结果
    json_ = {
        'product_code': 'cf5b6d062260f643d123ae61a37fe416',
        'apply_id': apply_id,
    }
    session = requests.session()
    resp = session.request('GET', result_api, params=json_,
                           headers={'content-type': 'application/json;charset=utf-8'})
    print resp.url
    print resp.content


if __name__ == '__main__':
    # all_step_test()
    test_case = Cases()
    # test_case.test_credit_audit()
    # for i in range(45):
    #     test_case.test_credit_audit()
    #     time.sleep(1)
    test_case.test_obtain_result()
    # test_case.test_list_result()
    # async_post()
