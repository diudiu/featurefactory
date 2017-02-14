# -*- coding:utf-8 -*-
"""
    Copyright (c) 2013-2016 SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/22
    Change Activity:

"""

import logging
import time
from celery import shared_task

import django
from django.apps.registry import apps
if django.VERSION >= (1, 7) and not apps.ready:
    django.setup()

from apps.common.dispatcher import data_get_dispatch
from apps.common.dispatcher import process_dispatch

logger = logging.getLogger('apps.featureapi')


@shared_task
def audit_task(base_data):
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
    #        "\       "      \X/      "      /"
    ##################################################
    #  TODO 这里调用一个特征处理分发器  依然返回一个数据对象
    ret_data = process_dispatch(original_data_list, base_data['feature_list'], collect_type_list)

    # TODO 这里有按要求取特征逻辑, 计算结束的特征全部存在mongo里面  而且已经准备就绪  取出来返回
    # TODO 未来这里讲调用异步任务流
    if not ret_data:
        raise

    logger.info('\n**********\nin the tasks\n**********\n')

    callback_url = base_data.get('callback_url', None)
    # TODO 向callback_url回推结果