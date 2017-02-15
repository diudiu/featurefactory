# -*- coding:utf-8 -*-
"""
    common models
"""
from django.db import models
from apps.common.models import BaseModel


class FeatureFieldRel(BaseModel):

    id = models.AutoField(u'主键', primary_key=True)
    feature_name = models.CharField(u'特征字段名', max_length=64)
    data_identity = models.CharField(u'接口标识', max_length=64)
    collect_type = models.CharField(u'数据获取方式', max_length=64, null=True)
    # select 'Courier'  'ShuntCourier'   'RelevanceCourier'

    class Meta:
        db_table = 'fic_feature_field_rel'
        verbose_name = u'特征-接口映射表'
        verbose_name_plural = u'特征-接口映射表'
