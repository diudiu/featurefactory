# -*- coding:utf-8 -*-
"""
    common models
"""
from django.db import models
from apps.common.models import BaseModel

from apps.datasource.models import DsInterfaceInfo


# 添加一个表  用来对应受信人特征和计算用的参数和参数来自哪个接口
class FeatureProcessInfo(BaseModel):
    id = models.AutoField(u'主键', primary_key=True)
    feature_name = models.CharField(u'特征字段名', max_length=64)
    process_type = models.CharField(u'特征计算类型', max_length=64)
    data_identity = models.CharField(u'原始数据标识', max_length=64)

    class Meta:
        db_table = 'fic_feature_process_info'
        verbose_name = u'特征与计算参数对照表'
        verbose_name_plural = u'特征与计算参数对照表'
