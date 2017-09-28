# -*- coding:utf-8 -*-

import requests
import json
import logging
import time

from apps.dispatcher.settings import *
from vendor.utils.cache import RedisX

logger = logging.getLogger('apps.dispatcher')
loggertime = logging.getLogger('apps.timelog')


class RiskControl1(object):
    def __init__(self):
        self.red = RedisX()

    def do_request_1_apply(self, post_data):
        starttime = time.time()
        response = requests.post(URL_1_0_APPLY, headers=HEADERS, data=json.dumps(post_data))
        endtime = time.time()
        loggertime.info("do_request_1_apply time: %s" % (endtime - starttime))
        res_data = json.loads(response.content)
        logger.info("do_request_1_apply: %s" % res_data)
        apply_id = res_data['res_data']['apply_id']
        return [apply_id, response.content]

    def do_request_1_callback(self, post_data):
        starttime = time.time()
        response = requests.post(URL_1_0_CALLBACK, headers=HEADERS, data=post_data)
        endtime = time.time()
        loggertime.info("do_request_1_callback time: %s" % (endtime - starttime))
        return json.loads(response.content)

    def do_request_1_result(self, data):
        get_params = {
            "product_code": data.get("product_code"),
            "apply_id": data.get("apply_id")
        }
        starttime = time.time()
        session = requests.session()
        resp = session.request('GET', URL_1_0_RESULT, params=get_params,
                               headers={'content-type': 'application/json;charset=utf-8'})

        endtime = time.time()
        loggertime.info("do_request_1_result time: %s" % (endtime - starttime))
        return json.loads(resp.content)


class RiskControl2(object):
    def __init__(self):
        self.red = RedisX()

    def do_formal_request(self, data2):
        card_id = data2.get("card_id")
        res_date = {"status": 0, "message": "操作失败"}
        try:
            starttime = time.time()
            response = requests.post(URL_2_0_FORMAL, headers=HEADERS, data=json.dumps(data2))
            endtime = time.time()
            loggertime.info("do_request_2_apply time: %s" % (endtime - starttime))
            self.red.ping()
            if response.status_code == 200:
                res_date = json.loads(response.content)
                logger.info("do_request_2_apply response: %s" % res_date)
                apply_id = res_date.get("res_data").get("apply_id")
                logger.info("Do 2.0 formal request success, apply_id is: %s" % apply_id)
            else:
                logger.error("Do 2.0 formal request failed, status code is not 200, card_id is: %s" % card_id)

        except Exception as e:
            logger.error(e.message)

        return res_date

    def do_request_2(self, data):
        data_identity = data.get('data_identity')
        res_date = {"status": 0, "message": "操作失败"}
        try:
            response = ''
            if data_identity == "bank_card_upload":
                logger.info("Do request to 2.0, flowchart is: %s, data is: %s" % (data_identity, data))
                starttime = time.time()
                response = requests.post(URL_2_0_BANKCARD, headers=HEADERS, data=json.dumps(data))
                endtime = time.time()
                loggertime.info("do_request_2_bank_card_upload time: %s" % (endtime - starttime))
                logger.info("bank_card_upload response is: %s, flowchart is: %s" % (response.content, data))
            elif data_identity == "email_dig_upload":
                logger.info("Do request to 2.0, flowchart is: %s, data is: %s", data_identity, data)
                starttime = time.time()
                response = requests.post(URL_2_0_EMAIL, headers=HEADERS, data=json.dumps(data))
                endtime = time.time()
                loggertime.info("do_request_2_email_dig_upload time: %s" % (endtime - starttime))
                logger.info("email_dig_upload response is: %s, flowchart is: %s" % (response.content, data))
            elif data_identity == "operator_dig_upload":
                phone_remain = data.get("phone_remain", None)
                if phone_remain:
                    data["phone_remain"] = float(phone_remain)
                logger.info("Do request to 2.0, flowchart is: %s, data is: %s", data_identity, data)
                starttime = time.time()
                response = requests.post(URL_2_0_OPERATOR, headers=HEADERS, data=json.dumps(data))
                endtime = time.time()
                loggertime.info("do_request_2_operator_dig_upload time: %s" % (endtime - starttime))
                logger.info("operator_dig_upload response is: %s, flowchart is: %s" % (response.content, data))
            elif data_identity == "final_upload":
                logger.info("Do request to 2.0, flowchart is: %s, data is: %s", data_identity, data)
                starttime = time.time()
                response = requests.post(URL_2_0_FINAL, headers=HEADERS, data=json.dumps(data))
                endtime = time.time()
                loggertime.info("do_request_2_final_upload time: %s" % (endtime - starttime))
                logger.info("final_upload response is: %s, flowchart is: %s" % (response.content, data))
            res_date = json.loads(response.content)
        except Exception as e:
            logger.error(e.message)

        return res_date
