# -*- coding:utf-8 -*-

from __future__ import unicode_literals

import requests
import json
import time

from vendor.utils.encrypt import Cryption

headers = {
    "Content-type": "application/json; charset=utf-8",
}
des_key = 'yyyyyyuuuuoooooo'


def async_post():
    url = 'http://127.0.0.1:9999/feature/extract/'
    data = {
        'client_code': 'test_client_code',
        'apply_id': 'test_apply_id',
        'res_keys': [
            'x',
            'y',
            'z',
        ],
        'arguments': {
            'a': '1',
            'b': '2',
            'c': '3',
            'd': '4',
            'e': '5',
            'f': '6',
            'g': '7',
        },
    }
    json_data = json.dumps(data, encoding="UTF-8", ensure_ascii=False)
    req_data = Cryption.aes_base64_encrypt(json_data, des_key)
    post_data = json.dumps({'content': req_data}, encoding="UTF-8", ensure_ascii=False)
    response = requests.post(url, headers=headers, data=post_data)
    print response.content

if __name__ == '__main__':
    async_post()
