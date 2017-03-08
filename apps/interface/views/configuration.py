# -*- coding:utf-8 -*-
"""
    Copyright (c) 2013-2016 SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/22
    Change Activity:

        _==/          i     i           \==_
      /XX/            |\___/|            \XX\
    /XXXX\            |XXXXX|            /XXXX\
   |XXXXXX\_         _XXXXXXX_         _/XXXXXX|
  XXXXXXXXXXXxxxxxxxXXXXXXXXXXXxxxxxxxXXXXXXXXXXX
 |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
 |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
  XXXXXX/^^^^^\XXXXXXXXXXXXXXXXXXXXX/^^^^^\XXXXXX
   |XXX|       \XXX/^^\XXXXX/^^\XXX/       |XXX|
     \XX\       \X/    \XXX/    \X/       /XX/
        "\       "      \X/      "       /"
"""

import json
import logging

from braces.views import CsrfExemptMixin
from django.http.response import HttpResponse
from django.views.generic import View

from apps.interface.decorator import data_check, data_send, json_load


class FeatureConfig(CsrfExemptMixin, View):

    @staticmethod
    @data_check
    @json_load
    @data_send
    def get(request):
        return HttpResponse('Feature Factory FeatureConfiguration!!!')

    @staticmethod
    @data_check
    @json_load
    @data_send
    def post(request):
        return HttpResponse('Feature Factory FeatureConfiguration Post !!!')


class RemoteConfig(CsrfExemptMixin, View):

    @staticmethod
    @data_check
    @json_load
    @data_send
    def get(request):
        return HttpResponse('Feature Factory RemoteConfiguration!!!')

    @staticmethod
    @data_check
    @json_load
    @data_send
    def post(request):
        return HttpResponse('Feature Factory RemoteConfiguration Post !!!')
