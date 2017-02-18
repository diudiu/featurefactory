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
from apps.datasource.models import DsInterfaceInfo
from apps.remote.models import FeatureFieldRel
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


def data_get_dispatch(base_data):
    """
    数据收集分发器
    根据传入特征名和相应客户端标识确定数据获取渠道
    根据数据获取渠道获取原始数据
    打造数据对象做数据存储与输出
    返回数据对象:junkman (拾荒者)
    :return:
    """
    apply_id = base_data.get('apply_id', None)
    useful_args = base_data.get('useful_args', None)
    feature_list = base_data.get('feature_list', None)
    base_data_list = []
    for feature_name in feature_list:
        # TODO 初始化特征处理类
        pass

    if not apply_id or not useful_args:
        logger.error('judge return error , no apply_id or no usrful_args')
        raise JudgeReturenError
    collect_type_list = FeatureFieldRel.objects.filter(
        feature_name__in=feature_list,
        is_delete=False
    )
    if not collect_type_list.count():
        logger.error('no config in database about those features : %s' % feature_list)
        raise FeatureNameUnfound
    data_identity_list = [data['data_identity'] for data in useful_args]
    interface_data = DsInterfaceInfo.objects.filter(
        data_identity__in=data_identity_list,
        is_delete=False,
    )
    if not interface_data.count():
        logger.error('no config in database about those data_identity : %s' % data_identity_list)
        raise DataIdentityUnfound
    api_manager = interface_data[0].data_source.api_manager
    # TODO 这下面有BUG 当api_manager有多个时  需要对interface_data 和 useful_args做一下分组
    api_manager_list = [api_manager + '.' + collect_type.collect_type
                        for collect_type in collect_type_list.iterator()]
    api_manager_list = list(set(api_manager_list))
    for api_manager in api_manager_list:
        try:
            obj = import_string(api_manager)
            junkman = obj(apply_id, base_data, interface_data)
        except Exception as e:
            logger.error('junkman init error , massage is :\n %s' % e)
            raise JunkmanInitializeFailed
        base_data = junkman.work_stream()
        if not base_data:
            logger.error('junkman work complete, nothing return')
            raise JunkmanWorkError
        base_data_list.append(base_data)
    return base_data_list, collect_type_list


def process_dispatch(original_data_list, target_field_name, collect_type_list):
    """
    特征处理分发器
    根据传入上面两个数据对象确定每一个特征的处理逻辑路径
    出发特征计算任务, 获取特征
    特征留存????????
    特征返回
    :return:
    """
    ret_data = {}
    feature_map = {collect.feature_name: collect.data_identity for collect in collect_type_list}
    for original_data in original_data_list:
        for feature_name in target_field_name:
            obj_string = cons.LP_BASE_HANDLE + cons.HANDLE_COMBINE + 'lp_' + \
                         feature_name + cons.HANDLE_COMBINE + cons.HANDLE_CLASS
            try:
                obj = import_string(obj_string)
                handler = obj(original_data.get(feature_map[feature_name], None))
            except Exception as e:
                logger.error('%s \nhandle init error , massage is :\n %s' % (obj_string, e))
                raise HandleInitializeFailed
            logger.info('get handle --%s--' % obj_string)
            ret = handler.handle()
            logger.info('Handle completed, result is %s' % ret)
            if not ret:
                logger.error('handle work complete, nothing return: %s' % obj_string)
                raise HandleWorkError
            ret_data.update(ret)
        # TODO ret中是处理出来的特征 这一层循环结束 储存一下子
    return ret_data
