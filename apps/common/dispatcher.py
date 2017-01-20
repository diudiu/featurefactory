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

    if not judger.work_stream():
        raise
    return judger


def data_get_dispatch():
    """
    数据收集分发器
    根据传入特征名和相应客户端标识确定数据获取渠道
    根据数据获取渠道获取原始数据
    打造数据对象做数据存储与输出
    返回数据对象:junkman (拾荒者)
    :return:
    """
    pass


def process_dispatch():
    """
    特征处理分发器
    根据传入上面两个数据对象确定每一个特征的处理逻辑路径
    出发特征计算任务, 获取特征
    特征留存????????
    特征返回
    :return:
    """
    pass
