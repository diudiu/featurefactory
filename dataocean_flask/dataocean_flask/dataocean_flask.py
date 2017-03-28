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
        if data_identity == 'cc_car_credit':
            content = {
                "status": "OK",
                "result": [
                    {
                        "license_no": "豫SFD***",
                        "run_miles": "20000.00",
                        "ton_count": "0.0000", "use_years": "5",
                        "assets_relation": "1",
                        "use_nature_code": "家庭⾃⽤",
                        "frame_no": "LBEXDA****87X530718",
                        "car_kind_code": "客⻋",
                        "seat_count": "5",
                        "license_color_code": "蓝",
                        "usable": "1",
                        "exhaust_scale": "1.5990",
                        "run_area_code": "中国境内（ 不含港、 澳、 台） ",
                        "purchase_price": "5-8万",
                        "engine_no": "7B50**12",
                        "mobile": "134****7600",
                        "enroll_date": "2007-11-03 00:00:00.0",
                        "brand_name": "北京现代BH7162MW轿⻋",
                        "ccity": "信阳"
                    },
                    {"license_no": "豫SFD123"},
                    {"license_no": "豫SFD456"},
                    {"license_no": "ASFD456"},
                    {"license_no": "京SFD45"},

                ]
            }
        elif data_identity == 'high_way_over_load':

            content = {
                    "status": "1",
                    "message": "操作成功",
                    "res_data": json.dumps({
                        "result": "00",
                        "result_message": "检测通过或查询有记录",
                        "content": {
                            "license_plate": "渝FC8***",
                            "start_time": "201401",
                            "end_time": "201412",
                            "over_speed_times": 2,
                            "over_speed_list": [{
                                "count_month": "201506",
                                "month_times": 2,
                                "section": "北京通州站-河北燕郊站，河北廊坊站-天津蓟县站",}
                            ]
                        }
                    })
                }

        else:
            req_data = json.loads(request.data)['req_data']
            # req_data = request.json["req_data"]
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
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8987)
    """
    http://192.168.1.196:8987/api/rule/gateway/court_zhixing_a_s/  post
    data = {"client_token": "test_lp_syph_code", "req_data": {"entity_id": "433031196210056032", "entity_name": "吴永荣"}}

    """

