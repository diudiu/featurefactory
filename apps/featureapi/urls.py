# -*- coding:utf-8 -*-
"""
    feature factory api route
"""

from django.conf.urls import patterns, url

from .views.generic import FeatureExtract

urlpatterns = patterns(
    '',
    url(r'^extract/$', FeatureExtract.as_view(), name='feature_extract'),
)
