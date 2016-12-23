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

from apps.featureapi.judger import Judger
from vendor.errors.api_errors import *

logger = logging.getLogger('apps.feature')


class FeatureExtract(CsrfExemptMixin, View):

    # def get(self, request):
    #     return HttpResponse("Feature Factory !!!!!")

    def post(self, request):

        message = {}
        if not request.body:
            raise
        post_data = json.loads(request.body)

        # get client code
        client_code = post_data.get('client_code')
        content = post_data.get('content')

        judger = Judger(client_code=client_code, data=content)

        # TODO use judger's work stream
        useful_data = judger.work_stream()

        # TODO packing the useful messages go to the next part of the syetem

        # TODO except Exceptions and do somethings

        # TODO finaly packing the response messages

        # TODO return JSONResponse

        return JSONResponse(message)
