# -*- coding:utf-8 -*-
"""
    urls route
"""
from django.conf.urls import url, patterns
from apps.dispatcher.views import ApplyCreditView
from apps.dispatcher.views import ObtainCreditResultView
from apps.dispatcher.views import AsyncCallbackView
from apps.dispatcher.views import ReceiveResult


urlpatterns = patterns(
    '',
    url(r'^credit/apply/$', ApplyCreditView.as_view(), name='api_credit_apply'),
    url(r'^credit/result/$', ObtainCreditResultView.as_view(), name='api_obtain_credit_result'),
    url(r'^async/callback/$', AsyncCallbackView.as_view(), name='api_async_callback'),
    url(r'^async/result/$', ReceiveResult.as_view(), name='receive_result'),

)
