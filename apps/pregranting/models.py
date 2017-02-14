# -*- coding: utf-8 -*-

from django.db import models


class BaseModel(models.Model):
    is_delete = models.BooleanField(u'是否逻辑删除', default=False)
    created_on = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True, blank=True, null=True)
    updated_on = models.DateTimeField(verbose_name=u'最后修改时间', auto_now=True)

    class Meta:
        abstract = True


# class ModelFeatureRel(BaseModel):
#     """ model feature rel """
#     model_name = models.CharField(u'模型名称', max_length=128)
#     field_name = models.CharField(u'字段名称', max_length=128)
#
#     class Meta:
#         db_table = 'pgc_model_feature_rel'
#         verbose_name = u'授信模型特征关系表'
#         verbose_name_plural = u'授信模型特征关系表'


class ModelCoefficientConf(BaseModel):
    """ model coefficient conf """
    model_name = models.CharField(u'模型名称', max_length=128)
    coefficient = models.FloatField(u'系数', default=1.0)
    income_interval_min = models.IntegerField(u'收入区间最小值', default=0)
    income_interval_max = models.IntegerField(u'收入区间最大值', default=0)
    computational_formula = models.CharField(u'计算公式', max_length=512, default='')

    class Meta:
        db_table = 'pgc_model_coefficient_conf'
        verbose_name_plural = u'授信模型系数配置表'
        verbose_name = u'授信模型系数配置表'

    def _model_desc(self):
        model_str = ''
        try:
            for field in self._meta.fields:
                model_str += '%s=%s,\n' % (field.name, getattr(self, field.name, 'None'))
        except UnicodeError:
            model_str = 'unicode error'

        return model_str

    def __str__(self):
        return '%s:%s' % (str(self.__class__), self._model_desc())

    def __unicode__(self):
        return '%s:%s' % (str(self.__class__), self._model_desc())


class ModelFieldOptionWeight(BaseModel):
    """ model field option weight """
    model_name = models.CharField(u'模型名称', max_length=128)
    field_name = models.CharField(u'字段名称', max_length=128)
    field_option_value = models.CharField(u'字段选项', max_length=20, null=True, default='')
    field_option_name = models.CharField(u'字段选项中文名称', max_length=64, null=True)
    field_option_weight = models.FloatField(u'字段选项权重', default=1.0, null=True)

    class Meta:
        db_table = 'pgc_model_field_option_weight'
        verbose_name = u'授信模型字段权重表'
        verbose_name_plural = u'授信模型字段权重表'
