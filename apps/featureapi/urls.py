# -*- coding:utf-8 -*-
"""
    feature factory api route
"""

from django.conf.urls import patterns, url

from .views.generic import FeatureExtract
from data_test import DataTest

urlpatterns = patterns(
    '',
    url(r'^extract/$', FeatureExtract.as_view(), name='feature_extract'),
    url(r'^data_test/$', DataTest.as_view(), name='data_test'),
)
