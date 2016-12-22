# -*- coding:utf-8 -*-
"""
    common models
"""
from django.db import models

__author__ = "Shaohan Niu"
__datetime__ = "2016/1/31"


class BaseModel(models.Model):
    """
        Base model
    """
    is_delete = models.BooleanField(u'是否逻辑删除', default=False)
    created_on = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True, blank=True, null=True)
    updated_on = models.DateTimeField(verbose_name=u'最后修改时间', auto_now=True)

    class Meta:
        abstract = True
