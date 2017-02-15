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
    manage_type = models.CharField(u'', max_length=256)

    class Meta:
        db_table = 'fic_client_overview'
        verbose_name = u''
        verbose_name_plural = u''


class CityCodeField(BaseModel):
    """

    """
    id = models.AutoField(u'主键', primary_key=True)
    city_name_cn = models.CharField(u'城市中文名', max_length=256)
    city_name_en = models.CharField(u'城市英文名', max_length=256)
    father_tip = models.CharField(u'父类子类标识', max_length=256)
    father_code = models.CharField(u'父类编码', max_length=256, null=True)
    city_code = models.CharField(u'地区编码', max_length=256)
    seouri = models.CharField(u'', max_length=256)
    abbreviation = models.CharField(u'简称', max_length=256, null=True)
    city_level = models.IntegerField(u'城市等级', null=True)

    class Meta:
        db_table = 'fic_city_code_field'
        verbose_name = u''
        verbose_name_plural = u''
