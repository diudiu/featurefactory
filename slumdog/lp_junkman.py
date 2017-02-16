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
import json
import requests
import time

from apps.etl.context import OriginalContext, CacheContext
from apps.etl.models import FeatureShuntConf, FeatureRelevanceConf
from apps.remote.models import FeatureFieldRel
from vendor.utils.phone_operator_judge import PhoneOperator

logger = logging.getLogger('apps.remote')


class Courier(object):
    """
    这个类用来获取全部原始数据
    针对单一数据源获取逻辑
    原始数据来源包括:
        1.缓存数据库(有效期一天?????)
        2.接口数据获取
    """
    def __init__(self, apply_id, base_data, interface_data):
        self.apply_id = apply_id
        self.interface_conf = interface_data
        self.args = {arg['data_identity']: arg['arguments'] for arg in base_data['useful_args']}
        self.data_identity_list = self.args.keys()
        self.original_base = OriginalContext(self.apply_id)  # MongoDB data
        self.cache_base = CacheContext(self.apply_id)  # MongoDB data

    def work_stream(self):
        return self._get_data_by_keys

    @property
    def _get_data_by_keys(self):
        cache_data = {}
        fresh_data = {}
        for interface in self.interface_conf.iterator():
            data_identity = interface.data_identity
            data = self.cache_base.get(data_identity)
            if data:
                cache_data.update({
                    data_identity: data[data_identity]
                })
            else:
                prams = self.args[interface.data_identity]
                if not prams:
                    raise
                data = self._get_data_from_interface(interface, prams)
                if data:
                    fresh_data.update(data)
                    self.cache_base.kwargs.update(data)
                    self.cache_base.data_identity = data.keys()[0]
                self.cache_base.save()
            self.original_base.save()
        fresh_data.update(cache_data)
        return fresh_data

    def _get_data_from_interface(self, interface, prams):
        url = interface.data_source.backend_url + interface.route
        data_prams = eval(interface.must_data % prams)
        origin_data = self.do_request(url, data_prams)
        if not origin_data:
            raise  # TODO get data error
        self.original_base.kwargs.update({
            interface.data_identity: {
                'origin_data': origin_data,
                'prams': prams,
            }
        })
        return {interface.data_identity: origin_data}

    def do_request(self, url, data):
        # json_data = json.dumps(data, encoding="UTF-8", ensure_ascii=False)
        # response = requests.post(url, json_data)
        # content = response.content
        # content = json.loads(content)
        result = {'time': time.ctime(time.time())}
        return result


class ShuntCourier(object):
    """
    这个类用来获取全部原始数据
    针对根据参数进行数据源分流获取逻辑
    原始数据来源包括:
        1.缓存数据库(有效期一天?????)
        2.接口数据获取
    """

    def __init__(self, apply_id, base_data, interface_data):
        self.apply_id = apply_id
        self.feature_list = base_data['feature_list']
        self.interface_conf = interface_data
        self.args = {arg['data_identity']: arg['arguments'] for arg in base_data['useful_args']}
        self.data_identity_list = self.args.keys()
        self.original_base = OriginalContext(self.apply_id)  # MongoDB data
        self.cache_base = CacheContext(self.apply_id)  # MongoDB data

    def work_stream(self):
        # TODO 嗯  这次这个应该好使了
        return self._get_data_by_keys()

    def _get_data_by_keys(self):
        useful_identity_list = self._get_useful_key()
        cache_data = {}
        fresh_data = {}
        for interface in self.interface_conf.iterator():
            data_identity = interface.data_identity
            if data_identity not in useful_identity_list:
                continue
            data = self.cache_base.get(data_identity)
            if data:
                cache_data.update({
                    data_identity: data[data_identity]
                })
            else:
                prams = self.args[interface.data_identity]
                if not prams:
                    raise
                data = self._get_data_from_interface(interface, prams)
                if data:
                    fresh_data.update(data)
                    self.cache_base.kwargs.update(data)
                    self.cache_base.data_identity = data.keys()[0]
                self.cache_base.save()
            self.original_base.save()
        fresh_data.update(cache_data)
        return fresh_data

    def _get_useful_key(self):
        useful_data_identity = []
        feature_conf_list = FeatureShuntConf.objects.filter(
            feature_name__in=self.feature_list,
            is_delete=False
        )
        for feature_conf in feature_conf_list:
            shunt_key = feature_conf.shunt_key
            data_identity = feature_conf.data_identity
            parms = self.args.get(data_identity, None)
            if not parms:
                raise
            value = parms.get(shunt_key, None)
            if not value:
                raise
            oper = feature_conf.shunt_type
            if oper == 'PhoneOperator':
                po = PhoneOperator(value)
                shunt = po.distinguish()
                if shunt in eval(feature_conf.shunt_value):
                    useful_data_identity.append(data_identity)
                else:
                    continue
        return list(set(useful_data_identity))

    def _get_data_from_interface(self, interface, prams):
        url = interface.data_source.backend_url + interface.route
        data_prams = eval(interface.must_data % prams)
        origin_data = self.do_request(url, data_prams)
        if not origin_data:
            raise  # TODO get data error
        self.original_base.kwargs.update({
            interface.data_identity: {
                'origin_data': origin_data,
                'prams': prams,
            }
        })
        return {interface.data_identity: origin_data}

    def do_request(self, url, data):
        # json_data = json.dumps(data, encoding="UTF-8", ensure_ascii=False)
        # response = requests.post(url, json_data)
        # content = response.content
        # content = json.loads(content)
        result = {'time': time.ctime(time.time())}
        return result


class RelevanceCourier(object):
    """
    这个类用来获取全部原始数据
    针对多个数据源包含层级关系的逻辑
    如:
        查询接口A 获得特征a
        用特征a做参数查询接口B 获取目标数据包
    原始数据来源包括:
        1.缓存数据库(有效期一天?????)
        2.接口数据获取
    """

    def __init__(self, apply_id, base_data, interface_data):
        self.apply_id = apply_id
        self.interface_conf = interface_data
        self.feature_list = base_data['feature_list']
        self.args = {arg['data_identity']: arg['arguments'] for arg in base_data['useful_args']}
        self.data_identity_list = self.args.keys()
        self.stop = False
        self.index = 0
        self.fresh_data = {}
        self.feature_conf_list = FeatureRelevanceConf.objects.filter(
            feature_name__in=self.feature_list,
            is_delete=False
        )
        self.sum = self.feature_conf_list.count()
        self.original_base = OriginalContext(self.apply_id)  # MongoDB data
        self.cache_base = CacheContext(self.apply_id)  # MongoDB data

    def work_stream(self):
        # TODO 太恶心啦 重构!
        while not self.stop:
            target_data_identity = self._data_prepare()
            self._get_data_by_keys(target_data_identity)
        return self.fresh_data

    def _get_data_by_keys(self, target_data_identity):
        cache_data = {}
        fresh_data = {}
        for interface in self.interface_conf.iterator():
            data_identity = interface.data_identity
            if target_data_identity != data_identity:
                continue
            data = self.cache_base.get(data_identity)
            if data:
                cache_data.update({
                    data_identity: data[data_identity]
                })
            else:
                prams = self.args[interface.data_identity]
                if not prams:
                    raise
                data = self._get_data_from_interface(interface, prams)
                if data:
                    fresh_data.update(data)
                    self.cache_base.kwargs.update(data)
                    self.cache_base.data_identity = data.keys()[0]
                self.cache_base.save()
            self.original_base.save()
        fresh_data.update(cache_data)
        self.fresh_data = fresh_data

    def _data_prepare(self):

        feature_conf = self.feature_conf_list[self.index]
        self.index += 1

        depend_feature = feature_conf.depend_feature
        f_c = FeatureFieldRel.objects.filter(
            feature_name=depend_feature,
            is_delete=False
        )
        if self.index == self.sum:
            self.stop = True
        return f_c[0].data_identity

    def _get_data_from_interface(self, interface, prams):
        url = interface.data_source.backend_url + interface.route
        data_prams = eval(interface.must_data % prams)
        origin_data = self.do_request(url, data_prams)
        if not origin_data:
            raise  # TODO get data error
        self.original_base.kwargs.update({
            interface.data_identity: {
                'origin_data': origin_data,
                'prams': prams,
            }
        })
        return {interface.data_identity: origin_data}

    def do_request(self, url, data):
        # json_data = json.dumps(data, encoding="UTF-8", ensure_ascii=False)
        # response = requests.post(url, json_data)
        # content = response.content
        # content = json.loads(content)
        result = {'time': time.ctime(time.time())}
        return result
