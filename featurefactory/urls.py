# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin

from apps.featureapi import urls as feature_url

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'featurefactory.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^feature/', include(feature_url)),
)
