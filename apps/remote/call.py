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

from braces.views import CsrfExemptMixin
from apps.featureapi.response import JSONResponse
from django.views.generic import View

from apps.async.tasks import *
from apps.etl.dataclean import DataClean
from apps.etl.context import CacheContext, ArgsContext, ApplyContext, PortraitContext
from apps.datasource.models import DsInterfaceInfo
from vendor.errors.remote_error import *
from vendor.errors.contact_error import *

logger = logging.getLogger('apps.remote')


class DataPrepare(object):
    def __init__(self, data_identity, apply_id, args_list, collect_type):
        logger.info('Init DataPrepare')
        self.data_identity = data_identity
        self.apply_id = apply_id
        self.cache_base = CacheContext(self.apply_id)
        self.argument_base = ArgsContext(self.apply_id)
        self.parm_keys = args_list
        self.parm_dict = {}
        self.url = ''
        self.is_list_args = ''
        self.is_async = 0
        self.collect_type = collect_type

    def get_original_data(self):
        if self.data_identity in self.cache_base.smembers_async():
            raise DoingAsyncCallInterface
        ret_data = self.get_data_from_db()
        if not ret_data:
            ret_data = self.get_origin_data_from_interface()
        return ret_data

    def get_data_from_db(self):
        ret_data = {}
        data = self.cache_base.get(self.data_identity)
        if data:
            ret_data = data[self.data_identity]['origin_data']
            logger.info('Find cache_base data_identity:%s data:\n%s' % (self.data_identity, ret_data))
            if not ret_data:
                self.cache_base.delete(self.data_identity)
        return ret_data

    def get_origin_data_from_interface(self):
        logger.info('get_origin_data_from_interface data_identity:%s' % self.data_identity)
        ds_conf = DsInterfaceInfo.objects.filter(
            data_identity=self.data_identity,
            is_delete=False
        )
        if not ds_conf:
            logger.error('Stream in call class ,Get DsInterfaceInfo error, data_identity is : %s' %
                         self.data_identity)
            raise DataIdentityUnfound
        else:
            ds_conf = ds_conf[0]
        if self.collect_type == 'Courier':
            self.is_async = ds_conf.is_async
        self.prepare_parms()
        self.url = ds_conf.data_source.backend_url + ds_conf.route + self.data_identity + '/'
        if self.is_list_args:
            data_prams = []
            for i in self.parm_dict[self.is_list_args]:
                parm_dict = self.parm_dict.copy()
                parm_dict.update({self.is_list_args: i})
                prams = eval(ds_conf.must_data % parm_dict)
                data_prams.append([i, prams])
        else:
            data_prams = eval(ds_conf.must_data % self.parm_dict)

        logger.info('prams:%s' % data_prams)
        if self.is_async:
            self.get_origin_data_asyns(data_prams, self.is_list_args)
        else:
            return self.get_origin_data_sync(data_prams, ds_conf)

    def get_origin_data_sync(self, data_prams, ds_conf):
        """同步获取数据"""
        if isinstance(data_prams, list):
            origin_data = {}
            for flag, prams in data_prams:
                clear_data = self._get_data_from_interface(ds_conf, prams)
                if clear_data:
                    origin_data.update({flag: clear_data})
                else:
                    logger.warn('Stream in call class ,Get origin data error, data_identity is : %s args:%s' %
                                (self.data_identity, prams))
        else:
            origin_data = self._get_data_from_interface(ds_conf, data_prams)
        if origin_data:
            self.cache_base.kwargs.update({
                self.data_identity: {
                    'origin_data': origin_data,
                    'prams': self.parm_dict,
                }
            })
            self.cache_base.save()
        return origin_data

    def get_origin_data_asyns(self, data_prams, is_list_args):
        """异步获取数据"""
        self.cache_base.sadd_async(self.data_identity)
        if isinstance(data_prams, list):
            for flag, prams in data_prams:
                self.cache_base.sadd_async_args({is_list_args: prams[is_list_args]})
                request_data_from_interface_async.apply_async((prams, self.url, self.data_identity), retry=True,
                                                              queue='re_task_store', routing_key='re_task_store')
        else:
            request_data_from_interface_async.apply_async((data_prams, self.url, self.data_identity), retry=True,
                                                          queue='re_task_store', routing_key='re_task_store')
        logger.info("Start async call interface data_identify:%s" % self.data_identity)
        raise DoingAsyncCallInterface

    def _get_data_from_interface(self, ds_conf, data_prams):
        origin_data = None
        if ds_conf.method == 'LOCALE':
            origin_data = self.do_local_request(ds_conf, data_prams)
        elif ds_conf.method == 'REMOTE':
            origin_data = self.do_request(data_prams)

        cleaner = DataClean(origin_data, ds_conf.data_origin_type)
        clear_data = cleaner.worked()
        return clear_data

    def prepare_parms(self):
        arguments = self.argument_base.load()
        for key in self.parm_keys:
            value = arguments.get(key, None)
            if not value:
                logger.error('Stream in call class ,Get prepare_parms error, miss parms %s, data_identity is : %s'
                             % (key, self.data_identity))
                raise OriginDataGetParmsMiss
            if isinstance(value, list):
                self.is_list_args = key
            self.parm_dict.update({
                key: value
            })

    def do_request(self, data):
        if 'int(time.time())' in data.values():
            for k, v in data.items():
                if v == 'int(time.time())':
                    data.update({k: eval(v)})
        data = {
            "client_token": "test_lp_syph_code",
            "req_data": data
        }
        logger.info('From REMOTE get data, data_identity:%s param:%s' % (self.data_identity, data))
        response = requests.post(self.url, json.dumps(data))
        content = response.content
        content = json.loads(content)
        logger.info('data_identity:%s, REMOTE interface return:\n%s' % (self.data_identity, content))
        return content

    @staticmethod
    def do_local_request(ds_conf, data_prams):
        base_index = ds_conf.data_identity
        data_bases = None
        if base_index == 'apply_data':
            logger.info('From LOCAL get interface data, data from apply_data')
            data_bases = ApplyContext((data_prams.values())[0])
        if base_index == 'portrait_data':
            logger.info('From LOCAL get interface data, data from portrait_data')
            data_bases = PortraitContext((data_prams.values())[0])
        return data_bases.load() if data_bases else None


class AsyncCallback(CsrfExemptMixin, View):
    def cache_base_handle(self, apply_id, data_identity, origin_data, parm_dict):
        cache_base = CacheContext(apply_id)
        try:
            ds_conf = DsInterfaceInfo.objects.filter(
                data_identity=data_identity,
                is_delete=False
            )
            ds_conf = ds_conf[0]
            cleaner = DataClean(origin_data, ds_conf.data_origin_type)
            clear_data = cleaner.worked()
            is_list_args_value = ''
            for i in cache_base.smembers_async_args():
                if set(i.items()).issubset(set(parm_dict.items())):
                    is_list_args_value = i.values()[0]
                    cache_base.srem_async_args(i)
                    break
            if not cache_base.smembers_async_args():
                cache_base.srem_async(data_identity)

            if is_list_args_value:
                clear_data = {is_list_args_value: clear_data}
            cache_data = cache_base.get(data_identity)
            if cache_data:
                cache_data = cache_data[data_identity]['origin_data']
                clear_data.update(cache_data)

            cache_base.kwargs.update({
                data_identity: {
                    'origin_data': clear_data,
                    'prams': parm_dict,
                }
            })
            cache_base.save()

        except Exception as e:
            cache_base.delete(data_identity)
            logger.error(e.message)

    def post(self, request, *args, **kwargs):
        """异步回调接口"""
        res = {
            'status': 1,
            'message': 'success'
        }
        try:
            body = json.loads(request.body)
            apply_id = body.get('apply_id')
            data_identity = body.get('data_identity')
            parm_dict = body.get('parm_dict')
            origin_data = body.get('res_data')
            if not (apply_id and data_identity and parm_dict and origin_data):
                logger.error("async callback function request pattern error, body:%s" % body)
                raise Exception("async callback function request pattern error, body:%s" % body)
            if apply_id and data_identity:
                self.cache_base_handle(apply_id, data_identity, origin_data, parm_dict)

        except Exception as e:
            res = {
                'status': 0,
                'message': e.message
            }
        return JSONResponse(res)
