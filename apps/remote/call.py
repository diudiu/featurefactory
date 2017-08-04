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
import requests
import json
import re

from braces.views import CsrfExemptMixin
from apps.featureapi.response import JSONResponse
from django.views.generic import View

from apps.async.request_post import request_data_from_interface_async
from apps.etl.dataclean import DataClean
from apps.etl.context import CacheContext, ArgsContext, ApplyContext, PortraitContext
from apps.datasource.models import DsInterfaceInfo
from vendor.errors.remote_error import *
from vendor.errors.contact_error import *
from vendor.utils.constant import cons
from vendor.utils.encrypt import Cryption
import config

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
        self.token_url = ''
        self.access_token = ''
        self.is_list_args = ''
        self.is_list_args_to_real = ''
        self.is_async = 0
        self.is_cache = False
        self.collect_type = collect_type
        self.des_key = config.DES_KEY
        self.client_id = config.CLIENT_ID
        self.client_secret = config.CLIENT_SECRET

    def get_original_data(self):
        ret_data = self.get_data_from_db()
        # TODO
        # self.is_cache = False
        if not self.is_cache:
            ret_data = self.get_origin_data_from_interface()
        return ret_data

    def get_data_from_db(self):
        ret_data = {}
        data = self.cache_base.get(self.data_identity)
        if data:
            self.is_cache = True
            ret_data = data[self.data_identity]['origin_data']
            logger.info('Find cache_base data_identity:%s data:\n%s' % (self.data_identity, ret_data))
            if not ret_data and self.collect_type != cons.SHUNT_TYPE:
                self.cache_base.delete_cache(self.data_identity)
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
        self.is_async = ds_conf.is_async
        logger.info('data_identity request is_async: %s' % self.is_async)
        data_prams = self.prepare_parms(ds_conf)
        if not data_prams:
            return {}
        self.url = ds_conf.data_source.backend_url + ds_conf.route
        self.token_url = ds_conf.data_source.backend_url + "/oauth2/token/"
        if self.is_async:
            if self.data_identity in self.cache_base.smembers_async():
                DoingAsyncCallInterface.data_identify = self.data_identity
                raise DoingAsyncCallInterface
            self.get_origin_data_asyns(data_prams)
        else:
            return self.get_origin_data_sync(data_prams, ds_conf)

    def get_origin_data_sync(self, data_prams, ds_conf):
        """同步获取数据"""
        origin_data = {}
        if isinstance(data_prams, list):

            for flag, prams in data_prams:
                clear_data = self._get_data_from_interface(ds_conf, prams)
                if clear_data:
                    origin_data.update({flag: clear_data})
                else:
                    logger.warn('Stream in call class ,Get origin data error, data_identity is : %s args:%s' %
                                (self.data_identity, prams))
        else:
            origin_data = self._get_data_from_interface(ds_conf, data_prams)
        if ds_conf.method == 'REMOTE' and origin_data:
            self.cache_base.kwargs.update({
                self.data_identity: {
                    'origin_data': origin_data,
                    'prams': self.parm_dict,
                }
            })
            self.cache_base.save()
        return origin_data

    def get_origin_data_asyns(self, data_prams):
        """异步获取数据"""
        if isinstance(data_prams, list):
            logger.info(
                "data_identity:%s argument is a list , multiple async requests will be performed" % self.data_identity)
            for flag, prams in data_prams:
                redis_cache = {u'%s' % self.is_list_args_to_real: u'%s' % prams[self.is_list_args_to_real]}
                self.cache_base.sadd_async_args(self.data_identity, redis_cache)
                request_data_from_interface_async.apply_async((prams, self.url, self.apply_id, self.data_identity),
                                                              retry=True,
                                                              queue='re_task_store', routing_key='re_task_store')
        else:
            request_data_from_interface_async.apply_async((data_prams, self.url, self.apply_id, self.data_identity),
                                                          retry=True, queue='re_task_store',
                                                          routing_key='re_task_store')
        self.cache_base.sadd_async(self.data_identity)
        logger.info("Start async call interface data_identify:%s" % self.data_identity)
        DoingAsyncCallInterface.data_identify = self.data_identity
        raise DoingAsyncCallInterface

    def _get_data_from_interface(self, ds_conf, data_prams):
        origin_data = None
        if ds_conf.method == 'LOCALE':
            origin_data = self.do_local_request(ds_conf, data_prams)

        elif ds_conf.method == 'REMOTE':
            self.set_token()
            data_prams.update({
                "data_identity": self.data_identity,
                "access_token": self.access_token,
            })
            origin_data = self.do_request(self.url, data_prams)

        cleaner = DataClean(origin_data, ds_conf.data_origin_type)
        clear_data = cleaner.worked()
        return clear_data

    def prepare_parms(self, ds_conf):
        arguments = self.argument_base.load()
        for key in self.parm_keys:
            value = arguments.get(key, None)
            if not value:
                self.argument_base.reload()
                arguments = self.argument_base.load()
                value = arguments.get(key, None)
                if not value:
                    logger.error('Stream in call class ,Get prepare_prams error, miss prams %s, data_identity is : %s'
                                 % (key, self.data_identity))
                    return None
                    # raise OriginDataGetParmsMiss
            if isinstance(value, list):
                self.is_list_args = key
            self.parm_dict.update({
                key: value
            })
        if self.is_list_args:
            data_prams = []
            for i in self.parm_dict[self.is_list_args]:
                parm_dict = self.parm_dict.copy()
                parm_dict.update({self.is_list_args: i})
                is_list_args_to_real = re.search(r"'(\w+)':\s*'%%\(%s\)s'" % self.is_list_args, ds_conf.must_data)
                if not is_list_args_to_real:
                    logger.error("The key is not found in config:%s, the value code string is %s"
                                 % (ds_conf.must_data, self.is_list_args))
                    raise InterfaceInfoTableConfigError
                self.is_list_args_to_real = is_list_args_to_real.group(1)
                prams = eval(ds_conf.must_data % parm_dict)
                data_prams.append([i, prams])
        else:
            data_prams = eval(ds_conf.must_data % self.parm_dict)
        logger.info('prams:%s' % data_prams)
        return data_prams

    def do_token_request(self, url, data):
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
        logger.info(url)
        response = requests.post(url, post_data)
        content = response.content
        content = json.loads(content)
        if content.get('res_data', None):
            content['res_data'] = Cryption.aes_base64_decrypt(content['res_data'], self.des_key)
        result = json.loads(content['res_data'])
        return result

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
        logger.info(url)
        response = requests.post(url, post_data)
        content = response.content
        content = json.loads(content)
        if content.get('res_data', None):
            content['res_data'] = Cryption.aes_base64_decrypt(content['res_data'], self.des_key)
        result = json.loads(content['res_data'])
        content['res_data'] = result
        return content

    def set_token(self):
        grant_type = "client_credentials"
        url = self.token_url
        data = dict(
            grant_type=grant_type,
            client_secret=self.client_secret,
        )
        res = self.do_token_request(url, data)
        access_token = res['access_token']
        self.access_token = access_token.encode('utf-8')

    @staticmethod
    def do_local_request(ds_conf, data_prams):
        base_index = ds_conf.data_identity
        data_bases = None
        if base_index == 'apply_data':
            logger.info('From LOCALE get interface data, data from apply_data')
            data_bases = ApplyContext((data_prams.values())[0])
        if base_index == 'portrait_data':
            logger.info('From LOCALE get interface data, data from portrait_data')
            data_bases = PortraitContext((data_prams.values())[0])
        return data_bases.load() if data_bases else None


class AsyncCallback(CsrfExemptMixin, View):
    @staticmethod
    def cache_base_handle(apply_id, data_identity, origin_data, parm_dict):
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
            for i in cache_base.smembers_async_args(data_identity):
                logger.info('redis_cache_args:%s, request_args:%s' % (eval(i).items(), parm_dict.items()))
                if set(eval(i).items()).issubset(set(parm_dict.items())):
                    logger.info("remove data_identify:%s redis_cache_args:%s" % (data_identity, i))
                    is_list_args_value = eval(i).values()[0]
                    cache_base.srem_async_args(data_identity, i)
                    logger.info("remove redis_cache_args: %s" % i)
                    break
            if not cache_base.smembers_async_args(data_identity):
                cache_base.srem_async(data_identity)

            if is_list_args_value and clear_data:
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
            cache_base.delete_cache(data_identity)
            logger.error(e.message)

    def post(self, request):
        """异步回调接口"""
        data = {'status': 1, 'message': 'success'}
        try:
            body = json.loads(request.body)
            logger.info("Async callback receive:\n%s" % body)
            apply_id = body.get('apply_id')
            data_identity = body.get('data_identity')
            parm_dict = body.get('req_data')
            if not (apply_id and data_identity and parm_dict):
                logger.error("async callback function request pattern error, body:%s" % body)
                raise Exception("async callback function request pattern error, body:%s" % body)
            if apply_id and data_identity:
                self.cache_base_handle(apply_id, data_identity, body, parm_dict)
        except Exception as e:
            logger.error(e.message)
            data.update({'message': e.message})
        return JSONResponse(data)
