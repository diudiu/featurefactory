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

from vendor.utils.encrypt import Cryption
from vendor.errors.api_errors import *

logger = logging.getLogger('apps.feature')


class FeatureExtract(CsrfExemptMixin, View):

    # def get(self, request):
    #     return HttpResponse("Feature Factory !!!!!")

    def post(self, request):
        des_key = 'yyyyyyuuuuoooooo'
        post_data = json.loads(request.body)

        # get client code
        client_code = post_data.get('client_code')

        # TODO is client code useful and get messages belong to this client

        # decrypt the messages
        data = Cryption.aes_base64_decrypt(post_data['content'], des_key)
        message = json.loads(data)

        # TODO get target keys and arguments, check them in the DB

        # TODO packing the useful messages go to the next part of the syetem

        return JSONResponse(message)
