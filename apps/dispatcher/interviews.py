# -*- coding:utf-8 -*-

import requests
import json
import logging
import random

from apps.dispatcher.settings import *
from vendor.utils.cache import RedisX

logger = logging.getLogger('apps.dispatcher')


class RiskControl1(object):

    def __init__(self):
        self.red = RedisX()

    # def do_request_1_0(self, apply_id_2_0):
    #     json_data = self.red.get(apply_id_2_0)
    #     redis_data = json.loads(json_data)
    #     flow_chart = redis_data.get("flow_chart")
    #     if flow_chart == "formal":
    #         self.do_request_1_apply(redis_data)
    #     elif flow_chart in ["bankcard", "email", "operator"]:
    #         self.do_request_1_callback(redis_data)
    #     elif flow_chart == "final":
    #         self.do_request_1_result(redis_data)
    #     else:
    #         pass

    def do_request_1_apply(self, post_data):
        response = requests.post(URL_1_0_APPLY, headers=HEADERS, data=json.dumps(post_data))
        res_data = json.loads(response.content)
        apply_id = res_data['res_data']['apply_id']
        return [apply_id, response.content]

    def do_request_1_callback(self, post_data):
        response = requests.post(URL_1_0_CALLBACK, headers=HEADERS, data=json.dumps(post_data))
        res_data = json.loads(response.content)
        apply_id = res_data['res_data']['apply_id']
        return [apply_id, response.content]

    def do_request_1_result(self, data):
        get_params = {
            "product_code": data.get("product_code"),
            "apply_id": data.get("apply_id")
        }
        session = requests.session()
        resp = session.request('GET', URL_1_0_RESULT, params=get_params,
                               headers={'content-type': 'application/json;charset=utf-8'})
        return json.loads(resp.content)


class RiskControl2(object):

    def __init__(self):
        self.red = RedisX()

    def do_formal_request(self, data2, data1):
        card_id = data2.get("card_id")
        data2.update(
            {
                "call_back": URL_RECEIVE
            }
        )
        response = requests.post(URL_2_0_FORMAL, headers=HEADERS, data=json.dumps(data2))
        self.red.ping()
        if response.status_code == 200:
            res_date = json.loads(response.content)
            apply_id = res_date.get("res_data").get("apply_id")

            logger.info("Do 2.0 formal request success, apply_id is: %s" % apply_id)
            return apply_id
        else:
            logger.info("Do 2.0 formal request failed, status code is not 200, card_id is: %s" % card_id)

    def do_request_2(self, data, apply_id_2):
        data_identity = data.get('data_identity')
        if data_identity == "bank_card_upload":
            data2 = {}
            response = requests.post(URL_2_0_BANKCARD, headers=HEADERS, data=json.dumps(data2))
        elif data_identity == "email_dig_upload":
            data2 = {}
            response = requests.post(URL_2_0_EMAIL, headers=HEADERS, data=json.dumps(data2))
        elif data_identity == "operator_dig_upload":
            data2 = {}
            response = requests.post(URL_2_0_OPERATOR, headers=HEADERS, data=json.dumps(data2))
        elif data_identity == "final_upload":
            data2 = {}
            response = requests.post(URL_2_0_FINAL, headers=HEADERS, data=json.dumps(data2))
