# -*- coding:utf-8 -*-
"""
    feature factory web application api route
"""

from django.conf.urls import patterns, url

from apps.interface.views.authentication import Authentication
from apps.interface.views.featureconfig import *
from apps.interface.views.featureprocess import *

urlpatterns = patterns(
    '',
    url(r'^auth/login/$', Authentication.as_view(), name='authentication'),
    url(r'^auth/logout/$', Authentication.as_view(), name='authentication'),
    url(r'^common_conf/show/(?P<featurename>\w+)/(?P<page>\d+)/$', FeatureConfig.as_view(),
        name='feature_config_show'),
    url(r'^common_conf/update/(?P<item>\w+)/(?P<featureid>\d+)/$', FeatureConfig.as_view(), name='feature_config_update'),
    url(r'^common_conf/add/$', FeatureConfig.as_view(), name='feature_config_add'),
    url(r'^shunt_conf/show/(?P<featurename>\w+)/(?P<page>\d+)/$', FeatureShuntConfig.as_view(),
        name='feature_shunt_config_show'),
    url(r'^shunt_conf/update/(?P<featureid>\d+)/$', FeatureShuntConfig.as_view(),
        name='feature_relevance_config_update'),
    url(r'^shunt_conf/add/$', FeatureShuntConfig.as_view(), name='feature_shunt_config_add'),
    url(r'^relevance_conf/show/(?P<featurename>\w+)/(?P<page>\d+)/$', FeatureRelevanceConfig.as_view(),
        name='feature_shunt_config_show'),
    url(r'^relevance_conf/update/(?P<featureid>\d+)/$', FeatureRelevanceConfig.as_view(),
        name='feature_relevance_config_update'),
    url(r'^relevance_conf/add/$', FeatureRelevanceConfig.as_view(), name='feature_relevance_config_add'),
    url(r'^remote_conf/show/(?P<data_identity>\w+)/(?P<page>\d+)/$', RemoteConfig.as_view(), name='remote_config_show'),
    url(r'^remote_conf/update/(?P<id>\w+)/$', RemoteConfig.as_view(), name='remote_config_update'),
    url(r'^remote_conf/add/$', RemoteConfig.as_view(), name='remote_config_add'),

    url(r'^feature_process/config/$', FeatureProcessAPI.as_view(), name='feature_process'),
)
