# -*- coding:utf-8 -*-

from __future__ import unicode_literals

import requests
import json

from vendor.utils.encrypt import Cryption

headers = {
    "Content-type": "application/json; charset=utf-8",
}
des_key = 'yyyyyyuuuuoooooo'


def feature_post():
    url = 'http://127.0.0.1:9999/feature/extract/'
    # url = 'http://192.168.1.196:9998/feature/extract/'
    data = {
        'client_code': 'lp_test',
        'content': {
            'apply_id': 'test_apply_id',
            'res_keys': [
                'is_tianwang_gray',
                'is_tianwang_black',
                'is_tianwang_multi_loan',
                'is_tianyan_black',
            ],
            'arguments': {
                'id_card_code': '0',
                'mobile': '1',
                'email': '2',
            },
        },
    }
    json_data = json.dumps(data['content'], encoding="UTF-8", ensure_ascii=False)
    req_data = Cryption.aes_base64_encrypt(json_data, des_key)
    data.update({'content': req_data})
    post_data = json.dumps(data, encoding="UTF-8", ensure_ascii=False)
    response = requests.post(url, headers=headers, data=post_data)
    print response.content

if __name__ == '__main__':
    feature_post()
