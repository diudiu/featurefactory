# -*- coding:utf-8 -*-

import logging
import datetime

from apps.common.mongo_handle import MongoBase

logger = logging.getLogger('apps.etl')
ORIGINAL_BASE_NAME = 'original_base'
PROCESS_BASE_NAME = 'process_base'
CACHE_BASE_NAME = 'cache_base'


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
            self.cache_base.save(self.kwargs)
        else:
            self.original_base.save(self.kwargs)
            self.cache_base.save(self.kwargs)


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
        self.cache_base = MongoBase(collection_name=CACHE_BASE_NAME)

    def save(self):
        """save kwargs to backend"""
        query = {'apply_id': self.apply_id}
        cache_info = self.cache_base.search(query=query)
        self.kwargs.update(query)
        if cache_info:
            self.cache_base.update(query=query, data=self.kwargs)
        else:
            self.cache_base.save(self.kwargs)

    def get(self, key):
        """get value for key"""
        data = self.cache_base.search(query={'apply_id': self.apply_id})
        if data:
            return data.get(key)
        else:
            return None
