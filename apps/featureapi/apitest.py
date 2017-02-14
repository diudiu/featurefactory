# -*- coding:utf-8 -*-

import requests
import json


def feature_post():
    url = 'http://127.0.0.1:9999/feature/extract/'
    # url = 'http://192.168.1.199:9900/feature/extract/'
    # url = 'http://192.168.1.196:8070/feature/extract/'
    data = {
        'client_code': 'lp_test',
        'content': {
            'apply_id': 'APPLY20170213143121831017716',
            'callback_url': 'http://0.0.0.0:10086',
            'res_keys': [
                'online_time'
            ],
        },
    }
    headers = {"Content-type": "application/json; charset=utf-8"}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    content = json.loads(response.content)
    print content

if __name__ == '__main__':
    feature_post()
