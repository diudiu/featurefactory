# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/26
    Change Activity:
"""
import logging
from django.utils.module_loading import import_string

from apps.featureapi.models import ClientOverview
from vendor.errors.contact_error import *

logger = logging.getLogger('apps.etl')


def client_dispatch(client_code, content):
    """
    客户端分发器
    根据客户端标识client_code  确定客户端类型
    导入相应的传入参数处理逻辑中
    根据配置动态引入想用的judger对象
    对传入参数进行 验证, 填充, 处理
    :return:
    """
    handle_base = ClientOverview.objects.filter(client_code=client_code)
    if not handle_base.count():
        logger.error('client code unavailable, no such client %s' % client_code)
        raise ClientCodeInexistence

    data = handle_base[0]
    obj_string = data.manage_type
    if not obj_string:
        logger.error('No judge manage type in database, check this client: %s' % client_code)
        raise MissingManageType
    try:
        obj = import_string(obj_string)
        judger = obj(content, client_code)
    except Exception as e:
        logger.error('judger init error , massage is :\n %s' % e)
        raise JudgeInitializeFailed
    base_data = judger.work_stream()
    if not base_data:
        logger.error('judger work complete, nothing return')
        raise JudgeWorkError
    return base_data
