# -*- coding:utf-8 -*-
"""
    mongoengine models
"""
from django.conf import settings
from django.utils.timezone import datetime

from mongoengine import connect, DynamicDocument, StringField, DateTimeField

__author__ = "S.Junpeng"
__datetime__ = "2016/12/28"

# Mongodb config
MONGODB_HOST = getattr(settings, 'MONGODB_HOST', '')
MONGODB_PORT = getattr(settings, 'MONGODB_PORT', 27107)
MONGODB_NAME = getattr(settings, 'MONGODB_NAME', '')
MONGODB_USERNAME = getattr(settings, 'MONGODB_USERNAME', '')
MONGODB_PASSWORD = getattr(settings, 'MONGODB_PASSWORD', '')

# connect to mongodb
connect(MONGODB_NAME,
        host=MONGODB_HOST,
        port=MONGODB_PORT,
        username=MONGODB_USERNAME,
        password=MONGODB_PASSWORD,
        connect=False)


class BaseDynamicDocument(DynamicDocument):
    created_time = DateTimeField(help_text=u'创建时间', default=datetime.now())
    updated_time = DateTimeField(help_text=u'最后修改时间', default=datetime.now())

    meta = {
        'abstract': True
    }

    def clean(self):
        if self.created_time is None:
            self.created_time = datetime.now()

        self.updated_time = datetime.now()


class OriginalBase(BaseDynamicDocument):
    """
        原始数据集合
    """
    apply_id = StringField(max_length=64, help_text=u'申请唯一标识', unique=True)

    meta = {
        'collection': 'original_base'
    }


class ProcessBase(BaseDynamicDocument):
    """
        申请人维度集合(经过处理的原始数据)
    """
    apply_id = StringField(max_length=64, help_text=u'申请唯一标识', unique=True)

    meta = {
        'collection': 'process_base'
    }


class CacheBase(BaseDynamicDocument):
    """
        缓存数据集合
    """
    apply_id = StringField(max_length=64, help_text=u'申请唯一标识', unique=True)

    meta = {
        'collection': 'cache_base'
    }
