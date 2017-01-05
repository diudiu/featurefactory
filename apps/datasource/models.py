# -*- coding:utf-8 -*-
"""
    data datasource models
"""
from django.db import models

from vendor.utils import constant as cons
from apps.common.models import BaseModel


class DataSourceInfo(BaseModel):
    id = models.AutoField(u'主键', primary_key=True)
    name = models.CharField(u'数据源中文名', max_length=128)
    data_source_identity = models.CharField(u'数据源标识', max_length=64, default=u'')
    desc = models.CharField(u'数据源描述', max_length=512, null=True, blank=True)
    protocol_type = models.CharField(u'协议类型', max_length=15, choices=cons.REQUEST_PROTOCOL_TYPE)
    backend_url = models.CharField(u'域名', max_length=64)

    class Meta:
        db_table = 'fic_data_source_info'
        verbose_name = u'数据源基本信息表'
        verbose_name_plural = u'数据源基本信息表'


class DsInterfaceInfo(BaseModel):
    """
    Data source interface config
    """
    id = models.AutoField(u'主键', primary_key=True)
    name = models.CharField(u'接口名称', max_length=128)
    data_identity = models.CharField(u'接口标识', max_length=64)
    data_source = models.ForeignKey(DataSourceInfo, verbose_name=u'数据源配置')
    route = models.CharField(u'访问路由', max_length=128, help_text=u'/api/gateway/')
    method = models.CharField(u'访问方式', max_length=32, choices=cons.HTTP_METHOD)
    comment = models.CharField(u'描述', max_length=512, blank=True, null=True)
    common_data = models.CharField(u'公共参数', max_length=1024, null=True)
    must_data = models.CharField(u'必传参数', max_length=1024)
    is_need_token = models.BooleanField(u'是否需要access_token', default=False)
    is_need_encrypt = models.BooleanField(u'是否需要加密', default=True)
    is_async = models.BooleanField(u'是否异步调用', default=False)
    encrypt_type = models.CharField(u'加解密类型', max_length=32, null=True)

    class Meta:
        db_table = 'fic_interface_info'
        verbose_name_plural = u'接口表'
        verbose_name = u'接口表'

    @property
    def request_url(self):
        if self.call_type == cons.CALL_DATA_SOURCE_REMOTE:
            return '%s://%s%s' % (self.data_source.protocol_type,
                                  self.data_source.backend_url, self.route)
        else:
            return '%s' % self.route
