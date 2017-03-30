# -*- coding:utf-8 -*-

import requests
import json
import time

# from vendor.utils.encrypt import Cryption

headers = {
    "Content-type": "application/json; charset=utf-8",
}
des_key = 'yyyyyyuuuuoooooo'
no_disease_list = [

]


def feature_post():
    url = 'http://127.0.0.1:9999/rule/gateway/personal_info/'
    # url = 'http://192.168.1.199:9900/syph-ff/feature/extract/'
    data = {
        'id_card_name': '孙俊鹏',
        'id_card_code': '130202199108101414',
    }
    a = time.time()
    response = requests.post(url, headers=headers, data=json.dumps(data))
    content = json.loads(response.content)
    print content
    print time.time() - a

if __name__ == '__main__':
    feature_post()
