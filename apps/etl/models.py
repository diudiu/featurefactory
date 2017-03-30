# -*- coding:utf-8 -*-
"""
    common models
"""
from django.db import models
from apps.common.models import BaseModel

from apps.datasource.models import DsInterfaceInfo


class FeatureType(BaseModel):
    id = models.AutoField(u'主键', primary_key=True)
    feature_type_desc = models.CharField(u'特征类型解释', max_length=2048)

    class Meta:
        db_table = 'fic_feature_type'
        verbose_name = u'特征类型配置表'
        verbose_name_plural = u'特征类型配置表'

    def __unicode__(self):
        return "%s" % self.feature_type_desc


class FeatureCardType(BaseModel):
    id = models.AutoField(u'主键', primary_key=True)
    feature_type_desc = models.CharField(u'特征评分卡类型解释', max_length=2048)

    class Meta:
        db_table = 'fic_feature_card_type'
        verbose_name = u'特征评分卡类型配置表'
        verbose_name_plural = u'特征评分卡类型配置表'

    def __unicode__(self):
        return "%s" % self.feature_type_desc


class FeatureRuleType(BaseModel):
    id = models.AutoField(u'主键', primary_key=True)
    feature_type_desc = models.CharField(u'特征规则类型解释', max_length=2048)

    class Meta:
        db_table = 'fic_feature_rule_type'
        verbose_name = u'特征规则类型配置表'
        verbose_name_plural = u'特征规则类型配置表'

    def __unicode__(self):
        return "%s" % self.feature_type_desc


class FeatureConf(BaseModel):
    id = models.AutoField(u'主键', primary_key=True)
    feature_name = models.CharField(u'特征字段名', max_length=64)
    feature_name_cn = models.CharField(u'特征中文名', max_length=128)
    collect_type = models.CharField(u'数据获取方式', max_length=64, null=True)
    data_identity = models.CharField(u'参数字段名', max_length=2048, null=True)
    feature_type = models.ForeignKey(FeatureType, db_column="feature_type", null=True)
    feature_rule_type = models.ForeignKey(FeatureRuleType, db_column="feature_rule_type", null=True)
    feature_card_type = models.ForeignKey(FeatureCardType, db_column="feature_card_type", null=True)
    feature_select_value = models.CharField(u'特征可选值', max_length=2048, null=True)

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

    class Meta:
        db_table = 'fic_feature_relevance_conf'
        verbose_name = u'依赖关系处理逻辑配置表'
        verbose_name_plural = u'依赖关系处理逻辑配置表'


class PreFieldInfo(BaseModel):

    id = models.AutoField(u'主键', primary_key=True)
    field_name = models.CharField(u'字段名称', max_length=64)
    field_name_cn = models.CharField(u'中文名称', max_length=64)
    source = models.CharField(u'数据来源', max_length=64, null=True)
    path = models.CharField(u'JsonPath路径', max_length=256, null=True)

    class Meta:
        db_table = 'fic_pre_field_info'
        verbose_name = u'预处理字段表'
        verbose_name_plural = u'预处理字段表'


class FeatureProcess(models.Model):
    id = models.AutoField(u'主键', primary_key=True)
    feature_name = models.CharField(u'特征字段名', max_length=100, unique=True)
    feature_data_type = models.CharField(u'特征字段类型', max_length=50)
    default_value = models.CharField(u'特征缺省值', max_length=100)
    json_path_list = models.TextField(u'特征处理流程', null=True)
    f_map_and_filter_chain = models.CharField(u'特征处理前置map链', max_length=2048, null=True)
    reduce_chain = models.CharField(u'特征处理reduce链', max_length=2048, null=True)
    l_map_and_filter_chain = models.CharField(u'特征处理后置map链', max_length=2048, null=True)

    class Meta:
        db_table = 'fic_feature_process_info'
        verbose_name = u'特征计算方式配置表'
        verbose_name_plural = u'特征计算方式配置表'


class FuncLibSource(models.Model):
    FUNC_TYPE_CHOICES = [
        ('M', u'map'),
        ('F', u'filter'),
        ('R', u'reduce'),
        ('A', u'assert'),
    ]
    func_name = models.CharField(u'函数名', max_length=80, primary_key=True)
    func_desc = models.TextField(u'函数描述', null=True)
    func_type = models.CharField(u'函数类型', choices=FUNC_TYPE_CHOICES, default="M", max_length=10, db_index=True)

    class Meta:
        db_table = 'fic_func_lib'
        verbose_name = u'函数库配置表'
        verbose_name_plural = u'函数库配置表'

