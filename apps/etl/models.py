# -*- coding:utf-8 -*-
"""
    common models
"""
from django.db import models
from apps.common.models import BaseModel

from apps.datasource.models import DsInterfaceInfo


# 添加一个表  用来对应受信人特征和计算用的参数和参数来自哪个接口
class FeaturePrams(BaseModel):
    id = models.AutoField(u'主键', primary_key=True)
    feature_name = models.CharField(u'特征字段名', max_length=64)
    pram_field = models.CharField(u'特征计算参数', max_length=64)
    interface = models.ForeignKey(DsInterfaceInfo, verbose_name=u'数据源配置')

    class Meta:
        db_table = 'fic_feature_prams_info'
        verbose_name = u'特征与计算参数对照表'
        verbose_name_plural = u'特征与计算参数对照表'



