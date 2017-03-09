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
import time
import requests
import json

from apps.etl.dataclean import DataClean
from apps.etl.context import CacheContext, ArgsContext, ApplyContext, PortraitContext
from apps.datasource.models import DsInterfaceInfo
from vendor.errors.remote_error import *

logger = logging.getLogger('apps.remote')


class DataPrepare(object):

    def __init__(self, data_identity, apply_id, args_list):
        logger.info('Init DatePrepare')
        self.data_identity = data_identity
        self.apply_id = apply_id
        self.cache_base = CacheContext(self.apply_id)
        self.argument_base = ArgsContext(self.apply_id)
        self.parm_keys = args_list
        self.parm_dict = {}
        self.url = ''

    def get_original_data(self):
        ret_data = self.get_data_from_db()
        if not ret_data:
            ret_data = self.get_data_from_interface()
        if not ret_data:
            logger.error('Stream in call class name DataPrepare\nGet origin data error, data_identity is : ' %
                         self.data_identity)
            raise OriginDataGetError
        return ret_data

    def get_data_from_db(self):
        ret_data = {}
        data = self.cache_base.get(self.data_identity)
        if data:
            ret_data.update({
                self.data_identity: data[self.data_identity]
            })
        return ret_data

    def get_data_from_interface(self):
        ds_conf = DsInterfaceInfo.objects.filter(
            data_identity=self.data_identity,
            is_delete=False
        )
        if not ds_conf:
            raise
        else:
            ds_conf = ds_conf[0]
        self.prepare_parms()
        self.url = ds_conf.data_source.backend_url + ds_conf.route + self.data_identity + '/'
        data_prams = eval(ds_conf.must_data % self.parm_dict)
        origin_data = None
        if ds_conf.method == 'LOCALE':
            origin_data = self.do_local_request(ds_conf, data_prams)
        elif ds_conf.method == 'REMOTE':
            origin_data = self.do_request(data_prams)
        if not origin_data:
            raise  # TODO get data error
        cleaner = DataClean(origin_data, ds_conf.data_origin_type)
        clear_data = cleaner.worked()
        if not clear_data:
            # TODO 源数据 不符合规范
            raise
        self.cache_base.kwargs.update({
            self.data_identity: {
                'origin_data': clear_data,
                'prams': self.parm_dict,
            }
        })
        self.cache_base.save()
        return {self.data_identity: clear_data}

    def prepare_parms(self):
        arguments = self.argument_base.load()
        for key in self.parm_keys:
            value = arguments.get(key, None)
            if not value:
                raise
            self.parm_dict.update({
                key: value
            })

    def do_request(self, data):
        response = requests.post(self.url, json.dumps(data))
        content = response.content
        content = json.loads(content)
        return content

    @staticmethod
    def do_local_request(ds_conf, data_prams):
        base_index = ds_conf.data_identity
        data_bases = None
        if base_index == 'apply_data':
            data_bases = ApplyContext((data_prams.values())[0])
        if base_index == 'portrait_data':
            data_bases = PortraitContext((data_prams.values())[0])
        return data_bases.load() if data_bases else None

