# -*- coding:utf-8 -*-
"""
    Copyright (c) 2013-2016 SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/22
    Change Activity:

"""

import requests
import json

from apps.etl.dataclean import DataClean
from apps.etl.feature_collect import CollectFeature
from vendor.utils.constant import cons
from vendor.errors.common import ServerError
from vendor.messages.response_code import ResponseCode
from vendor.errors.contact_error import *

import logging
from celery import shared_task
import django
from django.apps.registry import apps

if django.VERSION >= (1, 7) and not apps.ready:
    django.setup()

logger = logging.getLogger('apps.featureapi')


@shared_task
def audit_task(base_data):
    data = {
        cons.RESPONSE_REQUEST_STATUS: ResponseCode.FEATURE_SUCCESS,
        cons.RESPONSE_REQUEST_MESSAGE: ResponseCode.message(ResponseCode.FEATURE_SUCCESS)
    }
    try:
        logger.info('\n============Streams in ASYNC mission control center,Collecting feature now===========')
        ret_data = mission_control(base_data)
        data.update({
            'client_code': base_data.get('client_code', None),
            'apply_id': base_data.get('apply_id', None),
            'ret_msg': ret_data
        })

    except ServerError as e:
        data = {
            cons.RESPONSE_REQUEST_STATUS: e.status,
            cons.RESPONSE_REQUEST_MESSAGE: e.message
        }
    except Exception as e:
        data = {
            cons.RESPONSE_REQUEST_STATUS: ResponseCode.FAILED,
            cons.RESPONSE_REQUEST_MESSAGE: e.message,
        }
    finally:
        callback_url = base_data['callback_url']
        headers = {"Content-type": "application/json; charset=utf-8"}
        response = requests.post(callback_url, headers=headers, data=json.dumps(data))
        logger.info('Results have already arrived, reply %s', response.content)


def mission_control(base_data):
    collecter = CollectFeature(base_data)
    collecter.get_feature_value()
    if collecter.error_list:
        pass
    ret_data = collecter.feature_ret
    logger.info('\n============feature compared completed=========================================\n')
    logger.info('All feature is %s', ret_data)
    return ret_data


@shared_task
def request_data_from_interface_async(data, url, data_identity):
    if 'int(time.time())' in data.values():
        for k, v in data.items():
            if v == 'int(time.time())':
                data.update({k: eval(v)})
    data = {
        "client_token": "test_lp_syph_code",
        "req_data": data
    }
    response = requests.post(url, json.dumps(data))
    content = response.content
    content = json.loads(content)
    if content['status'] != 1:
        logger.error("Async call interface:%s error response:%s" % (data_identity, content))
        raise AsyncCallInterfaceError
    logger.info("Async call interface:%s success response:%s" % (data_identity, content))

