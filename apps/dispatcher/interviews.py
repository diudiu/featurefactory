# -*- coding:utf-8 -*-

import requests
import json
import logging

from apps.dispatcher.settings import *
from vendor.utils.cache import RedisX

logger = logging.getLogger('apps.dispatcher')


class RiskControl1(object):

    def __init__(self):
        self.red = RedisX()

    def do_request_1_apply(self, post_data):
        response = requests.post(URL_1_0_APPLY, headers=HEADERS, data=json.dumps(post_data))
        res_data = json.loads(response.content)
        apply_id = res_data['res_data']['apply_id']
        return [apply_id, response.content]

    def do_request_1_callback(self, post_data):
        response = requests.post(URL_1_0_CALLBACK, headers=HEADERS, data=post_data)
        return json.loads(response.content)

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

    def do_formal_request(self, data2):
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
        data.update({"apply_id": apply_id_2, "call_back": URL_RECEIVE})
        if data_identity == "bank_card_upload":
            logger.info("Do request to 2.0, flowchart is: %s, data is: %s" % (data_identity, data))
            response = requests.post(URL_2_0_BANKCARD, headers=HEADERS, data=json.dumps(data))
            logger.info("bank_card_upload response is: %s, flowchart is: %s" % (response.content, data))
            pass
        elif data_identity == "email_dig_upload":
            logger.info("Do request to 2.0, flowchart is: %s, data is: %s", data_identity, data)
            response = requests.post(URL_2_0_EMAIL, headers=HEADERS, data=json.dumps(data))
            logger.info("email_dig_upload response is: %s, flowchart is: %s" % (response.content, data))
            pass
        elif data_identity == "operator_dig_upload":
            phone_remain = data.get("phone_remain", None)
            if phone_remain:
                data["phone_remain"] = float(phone_remain)
            logger.info("Do request to 2.0, flowchart is: %s, data is: %s", data_identity, data)
            response = requests.post(URL_2_0_OPERATOR, headers=HEADERS, data=json.dumps(data))
            logger.info("operator_dig_upload response is: %s, flowchart is: %s" % (response.content, data))
            pass
        elif data_identity == "final_upload":
            logger.info("Do request to 2.0, flowchart is: %s, data is: %s", data_identity, data)
            response = requests.post(URL_2_0_FINAL, headers=HEADERS, data=json.dumps(data))
            logger.info("final_upload response is: %s, flowchart is: %s" % (response.content, data))
            pass
