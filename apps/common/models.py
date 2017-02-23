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


class FeatureCodeMapping(BaseModel):
    """
    feature code mapping list
    """
    VALUE_TYPE_OPTIONS = [
        ("string", "string"),
        ("int", "int"),
        ("float", "float"),
    ]

    feature_name = models.CharField(u'特征名称', max_length=128)
    feature_desc = models.CharField(u'特征中文解释', max_length=128)
    unitary_value = models.CharField(u'取值基准值', max_length=64)
    dual_value = models.CharField(u'取值的最大值', max_length=64, null=True)
    mapped_value = models.IntegerField(u'映射之后的值')
    value_type = models.CharField(u'特征原来值的类型', max_length=20, choices=VALUE_TYPE_OPTIONS)

    class Meta:
        db_table = 'fic_feature_code_mapping'
        verbose_name = u'特征码值对应表'
        verbose_name_plural = u'特征码值对应表'
