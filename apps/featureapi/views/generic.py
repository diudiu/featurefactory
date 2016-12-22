# -*- coding:utf-8 -*-
"""
    Copyright (c) 2013-2016 SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/22
    Change Activity:

"""

import logging
import json

from apps.featureapi.response import JSONResponse
# from django.http.response import HttpResponse
from django.views.generic import View
from braces.views import CsrfExemptMixin


logger = logging.getLogger('apps.feature')


class FeatureExtract(CsrfExemptMixin, View):

    # def get(self, request):
    #     return HttpResponse("Feature Factory !!!!!")

    def post(self, request):
        response_data = {}

        return JSONResponse(response_data)
