# -*- coding:utf-8 -*-
"""
    Copyright (c) 2013-2016 SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/22
    Change Activity:


        _==/          i     i          \==_
      /XX/            |\___/|            \XX\
    /XXXX\            |XXXXX|            /XXXX\
   |XXXXXX\_         _XXXXXXX_         _/XXXXXX|
  XXXXXXXXXXXxxxxxxxXXXXXXXXXXXxxxxxxxXXXXXXXXXXX
 |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
 |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
  XXXXXX/^^^^"\XXXXXXXXXXXXXXXXXXXXX/^^^^^\XXXXXX
   |XXX|       \XXX/^^\XXXXX/^^\XXX/       |XXX|
     \XX\       \X/    \XXX/    \X/       /XX/
        "\       "      \X/      "      /"
"""

import json
import logging

from braces.views import CsrfExemptMixin
from django.http.response import HttpResponse
from django.views.generic import View

from apps.async.tasks import audit_task
from apps.common.dispatcher import client_dispatch
from apps.featureapi.decorator import post_data_check
from apps.featureapi.response import JSONResponse
from vendor.errors.api_errors import *
from vendor.utils.constant import cons

logger = logging.getLogger('apps.featureapi')


class FeatureExtract(CsrfExemptMixin, View):

    @staticmethod
    def get(request):
        return HttpResponse("Feature Factory !!!!!")

    # @装饰器验证一下request包完整性
    @post_data_check
    def post(self, request):
        data = {
            cons.RESPONSE_REQUEST_STATUS: ResponseCode.SUCCESS,
            cons.RESPONSE_REQUEST_MESSAGE: ResponseCode.message(ResponseCode.SUCCESS)
        }
        post_data = json.loads(request.body)
        # get client code
        client_code = post_data.get(cons.CLIENT_CODE, None)
        content = post_data.get(cons.RESPONSE_HANDLE_CONTENT, None)

        try:
            # TODO 这里调用分发器->客户端分发器  返回一个数据对象
            base_data = client_dispatch(client_code, content)

            audit_task.apply_async((base_data, ), retry=True, queue='re_task_audit', routing_key='re_task_audit')

        # TODO except Exceptions and do somethings
        except (UserIdentityError, EncryptError, GetApplyIdError, GetResKeysError,
                GetArgumentsError, ArgumentsAvailableError) as e:
            data = {
                cons.RESPONSE_REQUEST_STATUS: e.status,
                cons.RESPONSE_REQUEST_MESSAGE: e.message,
            }

        except Exception as e:
            data = {
                cons.RESPONSE_REQUEST_STATUS: ResponseCode.FAILED,
                cons.RESPONSE_REQUEST_MESSAGE: e.message,
            }

        # TODO finaly packing the response messages
        finally:
            pass

        # TODO return JSONResponse
        return JSONResponse(data)
