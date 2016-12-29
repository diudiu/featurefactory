# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH(Shaohan Niu), All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/26
    Change Activity:
"""
import json
import requests
from django.utils.timezone import datetime

from apps.etl.context import OriginalContext, CacheContext
from vendor.utils.encrypt import Cryption
from apps.datasource.models import DsInterfaceInfo


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
        self.data_identity_list = []
        self.interface_conf = None
        self.args = args
        self.original_base = OriginalContext(self.apply_id)  # MongoDB data
        self.cache_base = CacheContext(self.apply_id)  # MongoDB data

    def _load_config(self):
        self.interface_conf = DsInterfaceInfo.objects.filter(
            data_identity__in=self.data_identity_list,
            is_delete=False
        )

    def _get_data_from_cache(self, key):
        value = '1'
        return value

    def _get_data_from_interface(self, interface, prams):
        fresh_data = {}
        url = interface.data_source.backend_url + interface.route
        access_token = None
        if interface.is_need_token:
            token_url = interface.data_source.backend_url + '/oauth2/token/'
            token_data = dict(
                grant_type='client_credentials',
                client_secret=self.client_secret,
            )
            res = self.do_request(token_url, token_data)
            access_token = res['access_token'].encode('utf-8')
        common_data = eval(interface.common_data)
        data_prams = eval(interface.must_data % prams)
        if access_token:
            common_data.update({
                'access_token': access_token
            })
        data_prams.update(common_data)
        origin_data = self.do_request(url, data_prams)
        if not origin_data:
            raise
        self.original_base.kwargs.update({
            common_data['data_identity']: {
                'origin_data': origin_data,
                'prams': prams,
            }
        })
        return {common_data['data_identity']: origin_data}

    def do_request(self, url, data):
        json_data = json.dumps(data, encoding="UTF-8", ensure_ascii=False)
        req_data = Cryption.aes_base64_encrypt(json_data, self.des_key)
        data_bag = {
            "req_data": req_data,
            "client": self.client_id
        }
        post_data = json.dumps(
            data_bag,
            encoding="UTF-8",
            ensure_ascii=False
        )
        response = requests.post(url, post_data)
        content = response.content
        content = json.loads(content)
        result = None
        if content.get('res_data', None):
            content['res_data'] = Cryption.aes_base64_decrypt(content['res_data'], self.des_key)
            result = json.loads(content['res_data'])
            result.update({
                'create_time': datetime.now()
            })
        return result

    def get_data_by_keys(self):
        self.data_identity_list = [arg['data_identity'] for arg in self.args]
        cache_data = {}
        fresh_data = {}
        for i in range(len(self.data_identity_list)):
            data = self.cache_base.get(self.data_identity_list[i])
            if data:
                cache_data.update({
                    self.data_identity_list[i]: data
                })
                self.data_identity_list[i] = 0
            else:
                continue
        self.data_identity_list = list(set(self.data_identity_list))
        self.data_identity_list.remove(0)
        self._load_config()
        index = 0
        if not self.interface_conf and self.data_identity_list:
            raise
        if self.interface_conf:
            for interface in self.interface_conf.iterator():
                prams = self.args[index].get('arguments', None)
                if not prams:
                    pass
                data = self._get_data_from_interface(interface, prams)
                if data:
                    fresh_data.update(data)
                index += 1
            self.original_base.save()

        fresh_data.update(cache_data)
        return fresh_data
