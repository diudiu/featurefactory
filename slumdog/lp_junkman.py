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
from django.utils.timezone import datetime

from apps.etl.context import OriginalContext, CacheContext

logger = logging.getLogger('apps.remote')


class Courier(object):
    """
    这个类用来获取全部原始数据
    原始数据来源包括:
        1.缓存数据库(有效期一天?????)
        2.接口获取(访问数据源 DataOcean)
    """
    def __init__(self, apply_id, useful_args, interface_data):
        self.apply_id = apply_id
        self.interface_conf = interface_data
        self.args = {arg['data_identity']: arg['arguments'] for arg in useful_args}
        self.data_identity_list = self.args.keys()
        self.original_base = OriginalContext(self.apply_id)  # MongoDB data
        self.cache_base = CacheContext(self.apply_id)  # MongoDB data

    def work_stream(self):
        return self.get_data_by_keys()

    def get_data_by_keys(self):
        cache_data = {}
        fresh_data = {}
        for i in range(len(self.data_identity_list)):
            data = self.cache_base.get(self.data_identity_list[i])
            if data:
                cache_data.update({
                    self.data_identity_list[i]: data[self.data_identity_list[i]]
                })
                self.data_identity_list[i] = 0
            else:
                continue
        self.data_identity_list = list(set(self.data_identity_list))
        if 0 in self.data_identity_list:
            self.data_identity_list.remove(0)
        if not self.interface_conf and self.data_identity_list:
            raise
        for interface in self.interface_conf.iterator():
            prams = self.args[interface.data_identity]
            if not prams:
                pass
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
