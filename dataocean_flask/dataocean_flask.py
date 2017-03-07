# -*- coding:utf-8 -*-

import json
import sys

import requests

reload(sys)
sys.setdefaultencoding('utf-8')
import sys
import os

path = os.path.dirname(__file__)
sys.path.append(path)

from flask import Flask, jsonify, request

from encrypt import Cryption
from setting import *

app = Flask(__name__)


def do_request(url, data, des_key):
    json_data = json.dumps(data, encoding="UTF-8", ensure_ascii=False)
    req_data = Cryption.aes_base64_encrypt(json_data, des_key)
    print url, req_data
    content = requests.post(url, json.dumps({"req_data": req_data,
                                             "client": client_id},
                                            encoding="UTF-8", ensure_ascii=False)).content
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


@app.route('/api/rule/gateway/<data_identity>/', methods=['POST'])
def post(data_identity):
    data = {
        "status": 1,
        "message": "操作成功"
    }
    try:
        req_data = request.json["req_data"]
        req_data.update({'data_identity': data_identity})
        token = get_token(dataocean_url_grant, client_secret)
        req_data.update({"access_token": token["access_token"]})
        print req_data
        content = do_request(dataocean_url_data, req_data, des_key)
        # print content
        data.update({"res_data": content})

    except Exception, e:
        print e.message

        data.update({
            'status': 0,
            'message': 'error'
        })
    # print data
    return jsonify(data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8987)
    """
    http://192.168.1.196:8987/api/rule/gateway/court_zhixing_a_s/  post
    data = {"client_token": "test_lp_syph_code", "req_data": {"entity_id": "433031196210056032", "entity_name": "吴永荣"}}

    """

