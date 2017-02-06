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

from apps.async.tasks import audit_task
from apps.common.dispatcher import client_dispatch
from apps.featureapi.decorator import post_data_check
from apps.featureapi.response import JSONResponse
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
            base_data = client_dispatch(client_code, content)

            audit_task.apply_async((base_data, ), retry=True,
                                   queue='re_task_audit', routing_key='re_task_audit')
            # TODO 这里调用一个原始数据收集分发器  再次返回一个数据对象
            # original_data_list = data_get_dispatch(base_data)
            # TODO 这里调用一个特征处理分发器  依然返回一个数据对象
            # ret_data = process_dispatch(original_data_list)
            # if not ret_data:
            #     raise
            # data.update({'res_data': ret_data})
            # TODO 这里有按要求取特征逻辑, 计算结束的特征全部存在mongo里面  而且已经准备就绪  取出来返回
            # TODO 未来这里讲调用异步任务流
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
