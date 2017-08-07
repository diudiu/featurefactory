# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin

from apps.featureapi import urls as feature_url
from apps.interface import urls as app_url
from apps.integration import urls as integ_url
from apps.dispatcher import urls as dispatcher_url

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'featurefactory.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^syph-ff/feature/', include(feature_url)),
    url(r'^api/', include(dispatcher_url)),
    url(r'^feature_config/', include(app_url)),
    url(r'^rule/', include(integ_url)),
)
