# -*- coding:utf-8 -*-

import requests
import json

# from vendor.utils.encrypt import Cryption

headers = {
    "Content-type": "application/json; charset=utf-8",
}
des_key = 'yyyyyyuuuuoooooo'


def feature_post():
    url = 'http://127.0.0.1:9999/syph-ff/feature/extract/'
    # url = 'http://192.168.1.196:8070/feature/extract/'
    data = {
        'client_code': 'lp_test',
        'content': {
            'apply_id': 'APPLY20170213143121831017716',
            'callback_url': 'http://0.0.0.0:0000',
            'res_keys': [
                'income_level',
                'income_expense_comparison',
                'register_city_level',
                'company_addr_city_level',

                'application_on_plus',  # 张璐在写
                'education_degree_check',
            ],
        },
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    content = json.loads(response.content)
    print content

if __name__ == '__main__':
    feature_post()
