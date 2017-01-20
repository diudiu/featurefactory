# -*- coding:utf-8 -*-
"""
    Copyright (c) 2013-2016 SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/22
    Change Activity:

"""

import json
import logging

from braces.views import CsrfExemptMixin
from django.http.response import HttpResponse
from django.views.generic import View

from apps.featureapi.decorator import post_data_check
from apps.featureapi.response import JSONResponse
from apps.common.dispatcher import client_dispatch
from apps.common.dispatcher import data_get_dispatch
from apps.common.dispatcher import process_dispatch
from vendor.errors.api_errors import *
from vendor.utils.constant import cons

logger = logging.getLogger('apps.featureapi')


class FeatureExtract(CsrfExemptMixin, View):

    @staticmethod
    def get(self, request):
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
            client_dispatch(client_code, content)
            # TODO 这里调用一个原始数据收集分发器  再次返回一个数据对象
            data_get_dispatch()
            # TODO 这里调用一个特征处理分发器  依然返回一个数据对象
            process_dispatch()
            # TODO 未来这里讲调用异步任务流

        # judger = Judger(client_code=client_code, data=content)

        # use judger's work stream
        # try:
        #     index = judger.work_stream()
        #     if not index:
        #         raise ServerBusy
        #     useful_args = judger.ret_msg
        #     useful_common_data = {
        #         cons.CLIENT_ID: judger.client_id,
        #         cons.CLIENT_SECRET: judger.client_secret,
        #         cons.DES_KEY: judger.des_key,
        #         cons.APPLY_ID: judger.apply_id,
        #     }
        #     # args is useful_args and useful_common_data
        #     # packing the useful messages go to the next part of the syetem
        #     ret_data = dispatch(useful_common_data, useful_args)
        #     res_data = judger.encrypt(ret_data)
        #     data.update({
        #         cons.APPLY_ID: useful_common_data[cons.APPLY_ID],
        #         cons.RESPONSE_REQUEST_RES_DATA: res_data,
        #     })

        # TODO except Exceptions and do somethings
        except (UserIdentityError, EncryptError, GetApplyIdError,
                GetResKeysError, GetArgumentsError, ArgumentsAvailableError) as e:
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
