# -*- coding:utf-8 -*-
"""
    feature factory web application api route
"""

from django.conf.urls import patterns, url

from apps.interface.views.authentication import Authentication
from apps.interface.views.configuration import FeatureConfig, RemoteConfig


urlpatterns = patterns(
    '',
    url(r'^auth/login/$', Authentication.as_view(), name='authentication'),
    url(r'^auth/logout/$', Authentication.as_view(), name='authentication'),
    url(r'^feature_conf/show/(?P<page>\w+)/$', FeatureConfig.as_view(), name='feature_config'),
    url(r'^feature_conf/update/$', FeatureConfig.as_view(), name='feature_config'),
    url(r'^remote_conf/show/(?P<page>\w+)/$', RemoteConfig.as_view(), name='remote_config'),
    url(r'^remote_conf/update/$', RemoteConfig.as_view(), name='remote_config'),
)
