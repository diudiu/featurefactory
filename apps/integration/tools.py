# -*- coding:utf-8 -*-
"""
    Copyright (c) 2013-2016 SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/22
    Change Activity:
"""

import json
import requests
from vendor.utils.encrypt import Cryption

client_id = "jpWstKTB3bqPLWNoocVncCVVHniytPn6ROHy82Ze"
client_secret = "kXXNuP6IOMYr5WxhZihef4Ub6QbOFRPglX0WPPZ5D2sAydh3vDZTCvuMGRFAwlJcu3LoqlQuzs60XE72mxlisrZfhW2DGGCjUHJojkPhiouYrjKrkBj357ThuC61qupk"
des_key = 'sjdguhcphysghcih'


def do_request(url, data, des_key):
    json_data = json.dumps(data, encoding="UTF-8", ensure_ascii=False)
    # print "gyf---------", json_data
    req_data = Cryption.aes_base64_encrypt(json_data, des_key)
    content = requests.post(url, json.dumps(
        {"req_data": req_data, "client": client_id}, encoding="UTF-8", ensure_ascii=False
    )).content
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
    # print content
    token = json.loads(content['res_data'])
    return token
