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
from vendor.utils.constant import cons
from vendor.errors.contact_error import *
import time
import logging
from celery import shared_task
import django
from django.apps.registry import apps

if django.VERSION >= (1, 7) and not apps.ready:
    django.setup()

logger = logging.getLogger('apps.featureapi')


@shared_task
def request_data_from_interface_async(data, url, apply_id, data_identity):
    content = ''
    try:

        if 'int(time.time())' in data.values():
            for k, v in data.items():
                if v == 'int(time.time())':
                    data.update({k: eval(v)})
        data = {
            "client_token": "test_lp_syph_code",
            "req_data": data,
            "apply_id": apply_id,
            "callback": cons.CALLBACK
        }
        logger.info("Async call remote interface request:\n %s" % data)
        response = requests.post(url, json.dumps(data))
        content = response.content
        content = json.loads(content)
        if content['status'] != cons.ASYNC_SUCCESS_CALL_STATUS:
            raise AsyncCallInterfaceError
        logger.info("Async call interface:%s success response:%s" % (data_identity, content))
    except AsyncCallInterfaceError:
        logger.error("Async call interface:%s error response:%s" % (data_identity, content))
    except Exception as e:
        logger.error("Async call interface:%s error message:%s" % e.message)

