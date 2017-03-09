# -*- coding:utf-8 -*-
"""
    feature factory api route
"""

from django.conf.urls import patterns, url

from .views.generic import FeatureExtract
from .views.modelservice import ModelPreGranting

urlpatterns = patterns(
    '',
    url(r'^extract/$', FeatureExtract.as_view(), name='feature_extract'),
    url(r'^model/pregranting/(?P<client_code>\w+)/(?P<proposer_id>\w+)/$', ModelPreGranting.as_view(),
        name='feature_model_pre_granting'),
)
