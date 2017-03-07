# -*- coding:utf-8 -*-
"""
    feature factory web application api route
"""

from django.conf.urls import patterns, url

from apps.interface.views.authentication import Authentication


urlpatterns = patterns(
    '',
    url(r'^login/$', Authentication.as_view(), name='authentication'),
)
