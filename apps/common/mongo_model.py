# -*- coding:utf-8 -*-
"""
    mongoengine models
"""
from django.conf import settings
from django.utils.timezone import datetime

from mongoengine import connect, DynamicDocument, Document
from mongoengine import StringField, DictField, DateTimeField, ListField, FloatField

__author__ = "Shaohan Niu"
__datetime__ = "2016/1/31"

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


class SubmitExceptionRecord(BaseDynamicDocument):
    """
        API submit data occur exception.
    """
    meta = {
        'collection': 'submit_exception_record'
    }


class ApplyBase(BaseDynamicDocument):
    """

    """

    apply_id = StringField(max_length=64, help_text=u'申请唯一标识', unique=True)
    proposer_id = StringField(max_length=64, help_text=u'申请人唯一标识')
    name = StringField(max_length=64, help_text=u'申请姓名')
    card_id = StringField(max_length=32, help_text=u'申请身份证')
    product_code = StringField(max_length=32, help_text=u'产品编码')
    product_version = StringField(max_length=32, help_text=u'产品版本号', null=True)

    meta = {
        'collection': 'apply_base'
    }


class AuditBase(BaseDynamicDocument):
    """

    """

    # apply_id = DictField(help_text=u'申请唯一标识', null=True)
    # proposer_id = DictField(help_text=u'申请人唯一标识', null=True)
    name = DictField(help_text=u'申请姓名', null=True)
    card_id = DictField(help_text=u'申请身份证', null=True)
    product_code = DictField(help_text=u'产品编码', null=True)
    audit_status = DictField(help_text=u'申请信息审核状态', null=True)
    audit_score = DictField(help_text=u'审核分数', null=True)

    meta = {
        'collection': 'audit_base'
    }


class PortraitBase(BaseDynamicDocument):
    """

    """
    # apply_id = DictField(help_text=u'申请唯一标识', null=True)
    # proposer_id = DictField(help_text=u'申请人唯一标识', null=True)
    name = DictField(help_text=u'申请姓名', null=True)
    card_id = DictField(help_text=u'申请身份证', null=True)
    last_audit_status = DictField(help_text=u'上次申请信息审核状态', null=True)

    meta = {
        'collection': 'portrait_base'
    }


class ConvertModel(Document):
    """

    """
    convert_code = StringField(max_length=128, help_text=u'转换模型编码', unique=True)
    convert_name = StringField(max_length=128, help_text=u'转换模型名称')
    conf = DictField(help_text=u'转换配置', null=True)
    created_on = DateTimeField(help_text=u'创建时间', null=True)
    updated_on = DateTimeField(help_text=u'最后修改时间', null=True)

    meta = {
        'collection': 'convert_model_info'
    }
