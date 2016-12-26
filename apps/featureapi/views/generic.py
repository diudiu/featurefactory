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
from django.views.generic import View
from braces.views import CsrfExemptMixin

from apps.featureapi.decorator import post_data_check
from apps.featureapi.judger import Judger
from vendor.errors.api_errors import *

logger = logging.getLogger('apps.feature')


class FeatureExtract(CsrfExemptMixin, View):

    # def get(self, request):
    #     return HttpResponse("Feature Factory !!!!!")

    # @装饰器验证一下request包完整性
    @post_data_check
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
        try:
            index = judger.work_stream()
            if index:
                useful_args = judger.ret_msg
                useful_common_data = {
                    'client_id': judger.client_id,
                    'client_secret': judger.client_secret,
                    'des_key': judger.des_key,
                }
            else:
                raise

            # TODO packing the useful messages go to the next part of the syetem
            print 'useful_args: '
            print useful_args
            print 'useful_common_data'
            print useful_common_data

        # TODO except Exceptions and do somethings
        except Exception as e:
            pass
        # TODO finaly packing the response messages
        finally:
            pass

        # TODO return JSONResponse
        return JSONResponse(message)
