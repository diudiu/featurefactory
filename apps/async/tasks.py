# -*- coding:utf-8 -*-
"""
    Copyright (c) 2013-2016 SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/22
    Change Activity:

"""

import logging
from celery import shared_task
import django
from django.apps.registry import apps
if django.VERSION >= (1, 7) and not apps.ready:
    django.setup()

import requests
import json

from apps.common.dispatcher import data_get_dispatch
from apps.common.dispatcher import process_dispatch
from vendor.utils.constant import cons
from vendor.errors.common import ServerError
from vendor.messages.response_code import ResponseCode

logger = logging.getLogger('apps.featureapi')


@shared_task
def audit_task(base_data):
    # TODO 向callback_url回推结果
    data = {
        cons.RESPONSE_REQUEST_STATUS: ResponseCode.FEATURE_SUCCESS,
        cons.RESPONSE_REQUEST_MESSAGE: ResponseCode.message(ResponseCode.FEATURE_SUCCESS)
    }
    try:
        # TODO 这里调用一个原始数据收集分发器  再次返回一个数据对象
        original_data_list, collect_type_list = data_get_dispatch(base_data)
        ##################################################
        # TODO 未来用消息队列做链接
        #        _==/          i     i           \==_
        #      /XX/            |\___/|            \XX\
        #    /XXXX\            |XXXXX|            /XXXX\
        #   |XXXXXX\_         _XXXXXXX_         _/XXXXXX|
        #  XXXXXXXXXXXxxxxxxxXXXXXXXXXXXxxxxxxxXXXXXXXXXXX
        # |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        # |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
        #  XXXXXX/^^^^^\XXXXXXXXXXXXXXXXXXXXX/^^^^^\XXXXXX
        #   |XXX|       \XXX/^^\XXXXX/^^\XXX/       |XXX|
        #     \XX\       \X/    \XXX/    \X/       /XX/
        #        "\       "      \X/      "       /"
        ##################################################
        #  TODO 这里调用一个特征处理分发器  依然返回一个数据对象
        ret_data = process_dispatch(original_data_list, base_data['feature_list'], collect_type_list)
        # TODO 这里有按要求取特征逻辑, 计算结束的特征全部存在mongo里面  而且已经准备就绪  取出来返回
        # TODO 未来这里讲调用异步任务流
        logger.info('\n**********\nfeature compared completed\n**********\n')
        logger.info('All feature is %s', ret_data)
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
