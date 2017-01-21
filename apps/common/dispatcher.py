# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/26
    Change Activity:
"""

from django.utils.module_loading import import_string

from apps.common.models import ClientOverview
from apps.datasource.models import DsInterfaceInfo
from apps.etl.models import FeatureProcessInfo


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
        # TODO 数据库里面查不到这个客户端code
        raise

    data = handle_base[0]
    obj_string = data.manage_type

    if not obj_string:
        # TODO 这个记录里面的manage_type字段没有值
        raise

    try:
        obj = import_string(obj_string)
        judger = obj(content)
    except Exception as e:
        # TODO 初始化对象失败, 可能是manage_type错误 或者参数错误乱七八糟的  具体异常会抛出
        raise

    base_data = judger.work_stream()
    if not base_data:
        raise
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
    base_data_list = []

    if not apply_id or not useful_args:
        raise
    data_identity_list = [data['data_identity'] for data in useful_args]
    interface_data = DsInterfaceInfo.objects.filter(
        data_identity__in=data_identity_list,
        is_delete=False,
    )
    # TODO 这下面有BUG 当api_manager有多个时  需要对interface_data 和 useful_args做一下分组
    api_manager_list = [interface.data_source.api_manager for interface in interface_data.iterator()]
    api_manager_list = list(set(api_manager_list))
    for api_manager in api_manager_list:
        try:
            obj = import_string(api_manager)
            junkman = obj(apply_id, useful_args, interface_data)
        except Exception as e:
            raise
        base_data = junkman.work_stream()
        if not base_data:
            raise
        base_data_list.append(base_data)
    return base_data_list


def process_dispatch(original_data_list):
    """
    特征处理分发器
    根据传入上面两个数据对象确定每一个特征的处理逻辑路径
    出发特征计算任务, 获取特征
    特征留存????????
    特征返回
    :return:
    """
    for original_data in original_data_list:
        di_list = original_data.keys()
        studio_conf = FeatureProcessInfo.objects.filter(
            data_identity__in=di_list,
            is_delete=False
        )
        for studio_data in studio_conf.iterator():
            data_identity = studio_data.data_identity
            obj_string = studio_data.process_type
            obj = import_string(obj_string)
            handler = obj(original_data.get(data_identity, None))
            ret = handler.handle()
        # TODO ret中是处理出来的特征 这一层循环结束 储存一下子

    return True
