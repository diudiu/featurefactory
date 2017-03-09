# -*- coding:utf-8 -*-
"""
    feature factory api route
"""

from django.conf.urls import patterns, url

from .views.simulation import Simulation


urlpatterns = patterns(
    '',
    url(r'^gateway/(?P<data_identity>\w+)/$', Simulation.as_view(), name='simulation'),
)