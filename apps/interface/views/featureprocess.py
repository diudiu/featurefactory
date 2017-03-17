# -*- coding:utf-8 -*-
"""
    Copyright (c) 2013-2016 SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/3/16
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
import jsonpath

from braces.views import CsrfExemptMixin
from apps.featureapi.response import JSONResponse
from django.views.generic import View
from apps.interface.functions import *
from studio.feature_comment_handle.exec_chain_handle import func_exec_chain
from vendor.utils.constant import cons
from vendor.messages.response_code import ResponseCode


logger = logging.getLogger('apps.interface')


class FeatureProcessAPI(CsrfExemptMixin, View):

    def post(self, request):
        resp_data = {
            cons.RESPONSE_REQUEST_STATUS: ResponseCode.SUCCESS,
            cons.RESPONSE_REQUEST_MESSAGE: ResponseCode.message(ResponseCode.SUCCESS)
        }
        body = request.body
        data = json.loads(body)
        origin_data = data.get('origin_data', None)
        configx = data.get('config', None)
        if not configx:
            raise
        json_path_str = configx.get("json_path", None)
        assert_list_str = configx.get("assert_list", None)
        f_map_and_filter_chain = configx.get("f_map_and_filter_chain", None)
        reduce_chain = configx.get("reduce_chain", None)
        l_map_and_filter_chain = configx.get("l_map_and_filter_chain", None)

        temp_data = origin_data
        if json_path_str:
            temp_data = jsonpath.jsonpath(origin_data, json_path_str)
        if assert_list_str:
            temp_data = func_exec_chain(temp_data, assert_list_str)
        if f_map_and_filter_chain:
            temp_data = func_exec_chain(temp_data, f_map_and_filter_chain)
        if reduce_chain:
            temp_data = func_exec_chain(temp_data, reduce_chain)
        if l_map_and_filter_chain:
            temp_data = func_exec_chain(temp_data, l_map_and_filter_chain)

        resp_data.update({
            'ret_msg': temp_data
        })
        return JSONResponse(resp_data)
