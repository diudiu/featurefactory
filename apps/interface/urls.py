# -*- coding:utf-8 -*-
"""
    feature factory web application api route
"""

from django.conf.urls import patterns, url

from apps.interface.views.authentication import Authentication
from apps.interface.views.configuration import Configuration


urlpatterns = patterns(
    '',
    url(r'^auth/login/$', Authentication.as_view(), name='authentication'),
    url(r'^auth/logout/$', Authentication.as_view(), name='authentication'),
    url(r'^conf/show/$', Configuration.as_view(), name='configuration'),
    url(r'^conf/update/$', Configuration.as_view(), name='configuration'),
)
