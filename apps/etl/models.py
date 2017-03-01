# -*- coding:utf-8 -*-
"""
    common models
"""
from django.db import models
from apps.common.models import BaseModel

from apps.datasource.models import DsInterfaceInfo


class FeatureConf(BaseModel):
    id = models.AutoField(u'主键', primary_key=True)
    feature_name = models.CharField(u'特征字段名', max_length=64)
    feature_name_cn = models.CharField(u'特征中文名', max_length=128)
    data_identity = models.CharField(u'原始数据标识', max_length=512)
    collect_type = models.CharField(u'数据获取方式', max_length=64, null=True)
    raw_field_name = models.CharField(u'参数字段名', max_length=2048)

    class Meta:
        db_table = 'fic_feature_common_conf'
        verbose_name = u'一般特征处理逻辑配置表'
        verbose_name_plural = u'一般特征处理逻辑配置表'


class FeatureShuntConf(BaseModel):

    id = models.AutoField(u'主键', primary_key=True)
    feature_name = models.CharField(u'特征字段名', max_length=64)
    shunt_key = models.CharField(u'分流依据字段名称', max_length=64)
    shunt_type = models.CharField(u'分流逻辑名', max_length=256)
    shunt_value = models.CharField(u'分流比较值', max_length=256)
    data_identity = models.CharField(u'原始数据标识', max_length=64)

    class Meta:
        db_table = 'fic_feature_shunt_conf'
        verbose_name = u'分流处理逻辑配置表'
        verbose_name_plural = u'分流处理逻辑配置表'


class FeatureRelevanceConf(BaseModel):

    id = models.AutoField(u'主键', primary_key=True)
    feature_name = models.CharField(u'特征字段名', max_length=64)
    depend_feature = models.CharField(u'此特征依赖的其他特征名', max_length=64, null=True)
    data_identity = models.CharField(u'', max_length=64)
    depend_di = models.CharField(u'依赖特征数据获取标识', max_length=64, null=True)

    class Meta:
        db_table = 'fic_feature_relevance_conf'
        verbose_name = u'依赖关系处理逻辑配置表'
        verbose_name_plural = u'依赖关系处理逻辑配置表'


class PreFieldInfo(BaseModel):

    id = models.AutoField(u'主键', primary_key=True)
    field_name = models.CharField(u'字段名称', max_length=64)
    field_name_cn = models.CharField(u'中文名称', max_length=64)
    source = models.CharField(u'数据来源', max_length=64)
    path = models.CharField(u'JsonPath路径', max_length=256)

    class Meta:
        db_table = 'fic_pre_field_info'
        verbose_name = u'预处理字段表'
        verbose_name_plural = u'预处理字段表'


class FeatureProcess(BaseModel):

    id = models.AutoField(u'主键', primary_key=True)
    feature_name = models.CharField(u'特征字段名', max_length=64)
    feature_data_type = models.CharField(u'特征字段类型', max_length=64)
    default_value = models.CharField(u'特征缺省值', max_length=64)
    json_path_list = models.CharField(u'特征处理流程', max_length=2048)
    map_and_filter_chain = models.CharField(u'特征处理map链', max_length=1024, null=True)
    reduce_chain = models.CharField(u'特征处理reduce链', max_length=1024)

    class Meta:
        db_table = 'fic_feature_process_info'
        verbose_name = u'特征计算方式配置表'
        verbose_name_plural = u'特征计算方式配置表'
