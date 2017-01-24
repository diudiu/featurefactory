# -*- coding:utf-8 -*-
import os
import json
import requests


def data_test():

    headers = {
        "Content-type": "application/json; charset=utf-8",
    }

    url = 'http://127.0.0.1:9999/feature/data_test/'
    # url = 'http://192.168.1.196:8070/feature/data_test/'
    original_data_list = [{
        u'tianwang_gray': {u'time': u'Sun Jan 22 14:53:13 2017'},
        u'tianyan_black': {u'time': u'Sun Jan 22 14:53:13 2017'},
        u'tianwang_multi_loan': {u'time': u'Sun Jan 22 14:53:13 2017'},
        u'tianwang_black': {u'time': u'Sun Jan 22 14:53:13 2017'}
    }]

    res = requests.post(url, headers=headers, data=json.dumps(original_data_list))
    print json.loads(res.content)

if __name__ == '__main__':
    data_test()
