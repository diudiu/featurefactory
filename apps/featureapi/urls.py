# -*- coding:utf-8 -*-
"""
    feature factory api route
"""

from django.conf.urls import patterns, url

# from apps.featureapi.test.unit_api import ProcessDispatch, DataGetDispatch, DataOceanTest
from .views.generic import FeatureExtract

urlpatterns = patterns(
    '',
    url(r'^extract/$', FeatureExtract.as_view(), name='feature_extract'),
    # url(r'^data_get_dispatch/$', DataGetDispatch.as_view(), name='data_get_dispatch'),
    # url(r'^process_dispatch/$', ProcessDispatch.as_view(), name='process_dispatch'),
    # url(r'^rule/gateway/(?P<data_identity>\w+)/$', DataOceanTest.as_view(), name='dataocean_test'),
)
