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
    original_data_list = data_get_dispatch(base_data)
    # TODO 这里调用一个特征处理分发器  依然返回一个数据对象
    target_field_list = [data['target_field_name'] for data in base_data['useful_args']]
    ret_data = process_dispatch(original_data_list, target_field_list)

    # TODO 这里有按要求取特征逻辑, 计算结束的特征全部存在mongo里面  而且已经准备就绪  取出来返回
    # TODO 未来这里讲调用异步任务流
    if not ret_data:
        raise

    logger.info('\n**********\nin the tasks\n**********\n')
