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
        self.data_identity_list = []
        self.interface_conf = None
        self.args = args
        self.original_base = None  # MongoDB data
        self.cache_base = None  # MongoDB data
        self.base_data_list = None

    def _load_config(self):
        self.interface_conf = DsInterfaceInfo.objects.filter(
            data_identity__in=self.data_identity_list,
            is_delete=False
        )

    def _build_prams(self):
        prams = {}

        return prams

    def _get_data_from_cache(self, key):
        value = '1'
        return value

    def _get_data_from_interface(self, interface):
        url = interface.data_source.backend_url + interface.route
        if interface.is_need_token:
            token_url = interface.data_source.backend_url + '/oauth2/token/'
            token_data = dict(
                grant_type='client_credentials',
                client_secret=self.client_secret,
            )
            res = self.do_request(token_url, token_data)
            access_token = res['access_token'].encode('utf-8')

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
        if content.get('res_data', None):
            content['res_data'] = Cryption.aes_base64_decrypt(content['res_data'], self.des_key)
        result = json.loads(content['res_data'])
        return result

    def get_data_by_keys(self):
        self.data_identity_list = [arg['data_identity'] for arg in self.args]
        self._load_config()
        if not self.interface_conf:
            raise
        for interface in self.interface_conf.iterator():
            self._get_data_from_interface(interface)

        cache_data = {}
        fresh_data = {}

