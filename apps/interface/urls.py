# -*- coding:utf-8 -*-
"""
    feature factory web application api route
"""

from django.conf.urls import patterns, url

from apps.interface.views.featureconfig import *
# from apps.interface.views.featureprocess import *

urlpatterns = patterns(
    '',
    url(r'^common_conf/show/(?P<featurename>\w+)/(?P<page>\d+)/$', FeatureConfig.as_view(),
        name='feature_config_show'),
    url(r'^common_conf/update/(?P<item>\w+)/(?P<featureid>\d+)/$', FeatureConfig.as_view(), name='feature_config_update'),
    url(r'^common_conf/add/(?P<item>\w+)/$', FeatureConfig.as_view(), name='feature_config_add'),
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
    url(r'^relevance_conf/check/$', FeatureRelevanceConfig.as_view(), name='feature_relevance_config_check'),
    url(r'^remote_conf/show/(?P<data_identity>\w+)/(?P<page>\d+)/$', RemoteConfig.as_view(), name='remote_config_show'),
    url(r'^remote_conf/update/(?P<id>\w+)/$', RemoteConfig.as_view(), name='remote_config_update'),
    url(r'^remote_conf/add/$', RemoteConfig.as_view(), name='remote_config_add'),
    url(r'^feature_process/show/(?P<featurename>\w+)/(?P<page>\d+)/$', FeatureProcessAPI.as_view(), name='feature_process_get'),
    url(r'^feature_process/test/$', FeatureProcessAPI.as_view(), name='feature_process_test'),
    url(r'^feature_process/write/$', FeatureProcessAPI.as_view(), name='feature_process_write'),
    url(r'^feature_process/delete/$', FeatureProcessAPI.as_view(), name='feature_process_delete'),
    url(r'^get_list/(?P<item>\w+)/$', GetItemList.as_view(), name='get_list'),

    url(r'^pre_filed_conf/show/(?P<fieldname>\w+)/(?P<page>\d+)/$', PreFieldInfoConfig.as_view(),
        name='pre_filed_conf_show'),
    url(r'^pre_filed_conf/update/(?P<fieldid>\d+)/$', PreFieldInfoConfig.as_view(), name='pre_filed_conf_update'),
    url(r'^pre_filed_conf/add/$', PreFieldInfoConfig.as_view(), name='pre_filed_conf_add'),

)
