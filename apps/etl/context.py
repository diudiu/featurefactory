# -*- coding:utf-8 -*-

import logging
import datetime

from .backend import MongodbBackend
from apps.common.mongo_model import OriginalBase, ProcessBase, CacheBase

logger = logging.getLogger('apps.etl')


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
        self.original_model = OriginalBase
        if not self.kwargs:
            filters = dict(apply_id=self.apply_id, limit_start=0, limit_end=1)
            original_info = MongodbBackend(self.original_model, **filters).load(only_one=True)
            if original_info:
                self.kwargs.update(original_info)

    def save(self):
        """save kwargs to backend"""
        apply_info = MongodbBackend(self.original_model, apply_id=self.apply_id).load(only_one=True, obj=True)
        if apply_info:
            apply_info.update(**self.kwargs)
        else:
            backend = MongodbBackend(self.original_model, **self.kwargs)
            backend.save()

        return self.apply_id


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
        self.process_model = ProcessBase
        if not self.kwargs:
            filters = dict(apply_id=self.apply_id, limit_start=0, limit_end=1)
            process_info = MongodbBackend(self.process_model, **filters).load(only_one=True)
            if process_info:
                self.kwargs.update(process_info)

    def save(self):
        """save kwargs to backend"""
        process_info = MongodbBackend(self.process_model, apply_id=self.apply_id).load(only_one=True, obj=True)
        if process_info:
            process_info.update(**self.kwargs)
        else:
            backend = MongodbBackend(self.process_model, **self.kwargs)
            backend.save()

        return self.apply_id


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
        self.cache_model = CacheBase
        if not self.kwargs:
            filters = dict(apply_id=self.apply_id, limit_start=0, limit_end=1)
            cache_info = MongodbBackend(self.cache_model, **filters).load(only_one=True)
            if cache_info:
                self.kwargs.update(cache_info)

    def save(self):
        """update kwargs for portrait to backend"""
        cache_info = MongodbBackend(self.cache_model, apply_id=self.apply_id).load(only_one=True, obj=True)
        if cache_info:
            cache_info.update(**self.kwargs)
        else:
            backend = MongodbBackend(self.cache_model, **self.kwargs)
            backend.save()

        return self.apply_id

