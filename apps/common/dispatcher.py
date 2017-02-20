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

from apps.common.models import ClientOverview
from apps.datasource.models import InterfaceFieldRel
from apps.remote.models import FeatureFieldRel
from apps.etl.context import ArgsContext, ApplyContext, PortraitContext
from vendor.utils.constant import cons
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

    if not pretreatment(content.get('apply_id', None)):
        raise

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


def pretreatment(apply_id):
    """
    对mongo中的apply_base和portrait_base进行数据预处理
    通过数据库配置读取所有来自基础数据的有用参数
    同一整合到另一集合中
    :return:
    """
    arg_base = ArgsContext(apply_id)
    arg_data = arg_base.load()
    if arg_data:
        return 1
    arg_conf = InterfaceFieldRel.objects.filter(
        is_delete=False,
    )
    arg_list = list(set([conf.raw_field_rel for conf in arg_conf]))
    feature_conf = FeatureFieldRel.objects.filter(
        feature_name__in=arg_list,
        is_delete=False
    )
    base_args = {}
    apply_base = ApplyContext(apply_id)
    apply_data = apply_base.load()
    base_args.update({
        'apply_data': apply_data.get('data', None)
    })
    proposer_id = apply_data.get('proposer_id', None)
    portrait_base = PortraitContext(proposer_id)
    portrait_data = portrait_base.load()
    base_args.update({
        'portrait_data': portrait_data.get('data', None)
    })
    arg_base.kwargs.update({
        'apply_id': apply_id,
    })
    for conf in feature_conf:
        feature_name = conf.feature_name
        data = feature_conf.data_identity
        if data in ('apply_data', 'portrait_data'):
            obj_string = cons.LP_BASE_HANDLE + cons.HANDLE_COMBINE \
                         + 'lp_' + feature_name + cons.HANDLE_COMBINE + cons.HANDLE_CLASS
            try:
                obj = import_string(obj_string)
                handler = obj(base_args[data])
            except Exception as e:
                logger.error('%s \nhandle init error , massage is :\n %s' % (obj_string, e))
                raise HandleInitializeFailed
            logger.info('get handle --%s--' % obj_string)
            ret = handler.handle()
            logger.info('Handle completed, result is %s' % ret)
            if not ret:
                logger.error('handle work complete, nothing return: %s' % obj_string)
                raise HandleWorkError
            if feature_name not in ret.keys():
                # TODO 配置错误 返回的特征名和期待的不同
                raise
            arg_base.kwargs.update(ret)
        arg_base.save()
