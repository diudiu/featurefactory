# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH(Shaohan Niu), All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/26
    Change Activity:
"""
from vendor.utils.encrypt import Cryption
from apps.datasource.models import DataSourceInfo, DsInterfaceInfo


class Courier(object):
    # TODO 传进来的参数已经过验证  全部是可用的
    # TODO 获取common_data , 和 apply_id
    # TODO 根据apply_id 查询历史数据库中是否有历史数据
    # TODO 有历史数据则直接返回, 没有的话  去DataOcean获取一下子
    # TODO 获取回来的原始数据留存一份, 然后甩到特征处理环节
    # TODO 特征处理返回的数据留存, 留存格式 (apply_id + 请求用参数包 + 访问接口 + 数据结果)
    # TODO 整合得到的结果  甩回去给上一步 准备返回
    def __init__(self, common_data, args):
        self.client_id = common_data.get('client_id', None)
        self.client_secret = common_data.get('client_secret', None)
        self.des_key = common_data.get('des_key', None)
        self.apply_id = common_data.get('apply_id', None)
        self.cryption = Cryption()
        self.keys = []
        self.args = args
        self.original_base = None  # MongoDB data
        self.process_base = None  # MongoDB data

    def _load_config(self):
        api_conf = DsInterfaceInfo.objects.filter(

        )
        data_source = DataSourceInfo.objects.filter()

    def _build_prams(self):
        prams = {}

        return prams

    def _get_key_from_cache(self, key):
        value = '1'
        return value

    def _get_key_from_interface(self, key):
        value = '1'
        prams = self._build_prams()

        return value

    def get_keys(self):
        self.keys = [arg['target_field_name'] for arg in self.args]
        cache_data = {}
        fresh_data = {}
        for key in self.keys:
            cache_value = self._get_key_from_cache(key)
            if cache_value:
                cache_data.update({key: cache_value})
            else:
                fresh_value = self._get_key_from_interface(key)
                fresh_data.update({key: fresh_value})
        return {'cache': cache_data, 'fresh': fresh_data}
