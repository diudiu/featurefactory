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
from bson import ObjectId
from jsonpath_rw_ext import parse

from apps.common.mongo_handle import MongoBase
from vendor.utils.cache import RedisX
from vendor.utils.constant import cons
from vendor.errors.api_errors import *
from apps.etl.models import PreFieldInfo

logger = logging.getLogger('apps.etl')

ORIGINAL_BASE_NAME = 'original_base'
PROCESS_BASE_NAME = 'process_base'
CACHE_BASE_NAME = 'cache_base'
APPLY_BASE_NAME = 'apply_base'
PORTRAIT_BASE_NAME = 'portrait_base'
BASE_ARGS_NAME = 'base_args'


class BaseContext(object):
    def __init__(self, apply_id, **kwargs):
        self.apply_id = apply_id
        self.kwargs = kwargs if kwargs else {}

    def save(self):
        pass

    def get(self, key):
        """get value for key from kwargs"""

        return self.kwargs.get(key, None)

    @property
    def data(self):
        """return all attribute for apply info dict"""
        return self.kwargs


class ApplyContext(BaseContext):
    """
    这是一个储存受信人输入的Mongo集合
    以受信人为文档标识
    每一组数据包含:
        受信人输入的基本数据
    储存模式:永久
    """

    def __init__(self, apply_id, **kwargs):
        super(ApplyContext, self).__init__(apply_id, **kwargs)
        self.apply_base = MongoBase(collection_name=APPLY_BASE_NAME)
        # self.cache_base = MongoBase(collection_name=CACHE_BASE_NAME)

    def load(self):
        query = {'apply_id': self.apply_id, 'is_delete': False}
        data = self.apply_base.search(query)
        return data


class OriginalContext(BaseContext):
    """
    这是一个储存原始数据的Mongo集合
    以受信人为文档标识
    每一组数据包含:
        1.数据源直接返回的查询结果
        2.请求数据源用到的参数
        3.查询时间
    储存模式:永久
    """

    def __init__(self, apply_id, **kwargs):
        super(OriginalContext, self).__init__(apply_id, **kwargs)
        self.original_base = MongoBase(collection_name=ORIGINAL_BASE_NAME)
        self.cache_base = MongoBase(collection_name=CACHE_BASE_NAME)

    def save(self):
        """save kwargs to backend"""
        query = {'apply_id': self.apply_id}
        original_info = self.original_base.search(query=query)
        self.kwargs.update(query)
        if original_info:
            self.original_base.update(query=query, data=self.kwargs)
            # self.cache_base.save(self.kwargs)
        else:
            self.original_base.save(self.kwargs)
            # self.cache_base.save(self.kwargs)


class ProcessContext(BaseContext):
    """
    这是一个特征数据的Mongo集合
    以受信人为文档标识
    每一组数据包含:
        1.特征计算的结果
        2.计算特征用到的参数和方法编号
        3.生成时间
    储存模式:永久
    """

    def __init__(self, apply_id, **kwargs):
        super(ProcessContext, self).__init__(apply_id, **kwargs)
        self.process_base = MongoBase(collection_name=PROCESS_BASE_NAME)

    def save(self):
        """save kwargs to backend"""
        query = {'apply_id': self.apply_id, 'is_delete': False}
        original_info = self.process_base.search(query=query)
        self.kwargs.update(query)
        if original_info:
            self.process_base.update(query=query, data=self.kwargs)
        else:
            self.process_base.save(self.kwargs)


class CacheContext(BaseContext):
    """
    这是一个储存原始数据的Mongo集合
    以受信人为文档标识
    每一组数据包含:
        1.数据源直接返回的查询结果
        2.请求数据源用到的参数
        3.查询时间
    储存模式:缓存模式  时效24h
    """

    def __init__(self, apply_id, **kwargs):
        super(CacheContext, self).__init__(apply_id, **kwargs)
        self.data_identity = ''
        self.red = RedisX()
        self.cache_base = MongoBase(collection_name=CACHE_BASE_NAME)

    def save(self):
        """save kwargs to backend"""
        self.red.ping()
        self.data_identity = self.kwargs.keys()[0]
        insert_id = self.cache_base.save(self.kwargs)
        self.kwargs = {}
        o_id = insert_id.inserted_id
        key = self.apply_id + ':' + self.data_identity
        if not self.red.set(key, o_id):
            raise Exception("redis cache_base %s key error!" % key)
        self.data_identity = ""

    def get(self, key):
        """get value for key"""
        self.red.ping()
        redis_key = self.apply_id + ':' + key
        o_id = self.red.get(redis_key)
        if o_id:
            query = {'_id': ObjectId(o_id)}
            ret = self.cache_base.search(query)
            return ret
        else:
            return None

    def delete_cache(self, key):
        """get value for key"""
        self.red.ping()
        redis_key = self.apply_id + ':' + key
        ret = self.red.delete(redis_key)
        return ret

    def sadd_async(self, value):
        self.red.ping()
        key = self.apply_id + '__data_identity'
        self.red.sadd(key, value)
        self.red.expire(name=key)

    def delete_async(self):
        self.red.ping()
        key = self.apply_id + '__data_identity'
        ret = self.red.delete(key)
        return ret

    def smembers_async(self):
        self.red.ping()
        key = self.apply_id + '__data_identity'
        ret = self.red.smembers(key)
        return ret

    def srem_async(self, value):
        self.red.ping()
        key = self.apply_id + '__data_identity'
        ret = self.red.srem(key, value)
        return ret

    def sadd_async_args(self, data_identity, value):
        self.red.ping()
        key = self.apply_id + '__' + data_identity + '__args'
        self.red.sadd(key, value)
        self.red.expire(name=key)

    def smembers_async_args(self, data_identity):
        self.red.ping()
        key = self.apply_id + '__' + data_identity + '__args'
        ret = self.red.smembers(key)
        return ret

    def srem_async_args(self, data_identity, value):
        self.red.ping()
        key = self.apply_id + '__' + data_identity + '__args'
        ret = self.red.srem(key, value)
        return ret


class PortraitContext(BaseContext):
    """
        这是一个储存受信人预授信的Mongo集合
        以受信人为文档标识
        每一组数据包含:
            受信人预授信的基本数据
            以proposer_id为唯一标识
        储存模式:永久
        """

    def __init__(self, proposer_id, **kwargs):

        self.context_data = None

        super(PortraitContext, self).__init__(proposer_id, **kwargs)
        self.portrait_base = MongoBase(collection_name=PORTRAIT_BASE_NAME)
        # self.cache_base = MongoBase(collection_name=CACHE_BASE_NAME)

    def load(self):
        query = {'proposer_id': self.apply_id, 'is_delete': False}
        data = self.portrait_base.search(query)
        return data

    def get_data(self, key):
        if self.context_data is None:
            self.context_data = self.load()

        return self.context_data.get(key) if self.context_data else None

    def set_data(self, **kwargs):
        if self.context_data is None:
            cache_data = self.load()
            self.context_data = cache_data if cache_data is not None else {}

        self.context_data.update(**kwargs)


class ArgsContext(BaseContext):
    """
    """

    def __init__(self, apply_id, **kwargs):
        super(ArgsContext, self).__init__(apply_id, **kwargs)
        self.args_base = MongoBase(collection_name=BASE_ARGS_NAME)
        self.arguments = {}
        # self.cache_base = MongoBase(collection_name=CACHE_BASE_NAME)

    def load(self):
        query = {'apply_id': self.apply_id}
        data = self.args_base.search(query)
        return data

    def save(self):
        """save kwargs to backend"""
        query = {'apply_id': self.apply_id, 'is_delete': False}
        original_info = self.args_base.search(query=query)
        self.kwargs.update(query)
        if original_info:
            self.args_base.update(query=query, data=self.kwargs)
        else:
            self.args_base.save(self.kwargs)

    def get(self, key):
        value = self.kwargs.get(key, None)
        if value:
            return value
        else:
            return (self.load()).get(key, None)

    def reload(self):
        self.arguments = {}
        apply_data = ApplyContext(self.apply_id).load()
        portrait_data = {}
        if cons.IS_PORTRAIT_BASE:
            proposer_id = apply_data.get('proposer_id', None)
            if not proposer_id:
                logger.error("Don't find proposer_id in apply_data,apply_id:%s" % self.apply_id)
                raise ProposerIdMissing
            portrait_data = PortraitContext(proposer_id).load()
            if not portrait_data:
                logger.error("Portrait_data is null in apply_data,proposer_id:%s apply_id:%s"
                             % (proposer_id, self.apply_id))
                raise NoPortraitData
        pre_conf = PreFieldInfo.objects.filter(
            is_delete=False
        )
        full_data = {
            'apply_data': apply_data,
            'portrait_data': portrait_data
        }
        for pre in pre_conf:
            self.arguments.update({
                pre.field_name: self.get_value(full_data[pre.source], pre.path)
            })
        self.kwargs.update(self.arguments)
        self.save()

    @staticmethod
    def get_value(data, path):
        path_expr = parse(path)
        temp = path_expr.find(data)
        result = []
        for val in temp:
            result.append(val.value)
        if result:
            return result[0]
        else:
            return None
