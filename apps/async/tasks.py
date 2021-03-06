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
def audit_task(apply_id, base_data, process_apply_id):
    data = {
        cons.RESPONSE_REQUEST_STATUS: ResponseCode.FEATURE_SUCCESS,
        cons.RESPONSE_REQUEST_MESSAGE: ResponseCode.message(ResponseCode.FEATURE_SUCCESS)
    }
    try:
        logger.info('\n===========Streams in ASYNC mission control center,Collecting feature now==========')
        logger.info("base_data: %s" % base_data)
        ret_data = mission_control(base_data)
        data.update({
            'client_code': base_data.get('client_code', None),
            'apply_id': apply_id.get('apply_id', None),
            'ret_msg': ret_data,
            'process_apply_id': process_apply_id
        })
    except ServerError as e:
        data = {
            'apply_id': apply_id.get('apply_id', None),
            cons.RESPONSE_REQUEST_STATUS: e.status,
            cons.RESPONSE_REQUEST_MESSAGE: e.message,
            'process_apply_id': process_apply_id
        }
    except Exception as e:
        import traceback
        traceback.print_exc()
        data = {
            'apply_id': apply_id.get('apply_id', None),
            cons.RESPONSE_REQUEST_STATUS: ResponseCode.FAILED,
            cons.RESPONSE_REQUEST_MESSAGE: e.message,
            'process_apply_id': process_apply_id
        }
    finally:
        callback_url = base_data['callback_url']
        headers = {"Content-type": "application/json; charset=utf-8"}
        logger.info("%s, %s" % (callback_url, data))
        post_data = json.dumps(data)
        response = requests.post(callback_url, headers=headers, data=post_data)
        logger.info('Results have already arrived, reply %s', response.content)


def mission_control(base_data):
    collecter = CollectFeature(base_data)  # 收集特征
    collecter.get_feature_value()
    if collecter.error_list:
        pass
    ret_data = collecter.feature_ret
    logger.info('\n==========feature compared completed==========\n')
    logger.info('All feature is %s', ret_data)
    return ret_data
