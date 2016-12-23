# -*- coding:utf-8 -*-
"""
    common models
"""
from django.db import models


class BaseModel(models.Model):
    """
        Base model
    """
    is_delete = models.BooleanField(u'是否逻辑删除', default=False)
    created_on = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True, blank=True, null=True)
    updated_on = models.DateTimeField(verbose_name=u'最后修改时间', auto_now=True)

    class Meta:
        abstract = True


class ClientOverview(BaseModel):
    """
        client_code and other messages
    """
    client_code = models.CharField(u'', max_length=128)
    client_id = models.CharField(u'', max_length=128)
    client_secret = models.CharField(u'', max_length=256)
    des_key = models.CharField(u'', max_length=128)

    class Meta:
        db_table = 'fic_client_overview'
        verbose_name = u''
        verbose_name_plural = u''
