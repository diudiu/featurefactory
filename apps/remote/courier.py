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
from apps.etl.models import FeaturePrams


class Courier(object):
    """
    这个类用来获取全部原始数据
    原始数据来源包括:
        1.缓存数据库(有效期一天?????)
        2.接口获取(访问数据源 DataOcean)
    """
    def __init__(self, common_data, args):
        self.client_id = common_data.get('client_id', None)
        self.client_secret = common_data.get('client_secret', None)
        self.des_key = common_data.get('des_key', None)
        self.apply_id = common_data.get('apply_id', None)
        self.cryption = Cryption()
        self.keys = []
        self.args = args
        self.original_base = None  # MongoDB data
        self.cache_base = None  # MongoDB data
        self.base_data_list = None

    def _load_config(self):
        self.interface_list = FeaturePrams.objects.filter(
            feature_name__in=self.keys,
            is_delete=False
        )
        if self.base_data_list.count() > 0:
            for base_data in self.interface_list.iterator():
                pass
        else:
            raise  # E 查不到数据

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
        self._load_config()
        cache_data = {}
        fresh_data = {}
        # TODO 这堆接口按个先查一遍
        for api_conf in self.api_conf_list.iterator():
            pass
        return {'cache': cache_data, 'fresh': fresh_data}
