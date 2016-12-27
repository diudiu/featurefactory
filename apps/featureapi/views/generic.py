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
from apps.remote.dispatch import dispatch
from vendor.utils.constant import cons
from vendor.errors.api_errors import *

logger = logging.getLogger('apps.featureapi')


class FeatureExtract(CsrfExemptMixin, View):

    # def get(self, request):
    #     return HttpResponse("Feature Factory !!!!!")

    # @装饰器验证一下request包完整性
    @post_data_check
    def post(self, request):
        data = {
            cons.RESPONSE_REQUEST_STATUS: ResponseCode.SUCCESS,
            cons.RESPONSE_REQUEST_MESSAGE: ResponseCode.message(ResponseCode.SUCCESS)
        }
        post_data = json.loads(request.body)
        # get client code
        client_code = post_data.get(cons.CLIENT_CODE)
        content = post_data.get(cons.RESPONSE_HANDLE_CONTENT)

        judger = Judger(client_code=client_code, data=content)

        # TODO use judger's work stream
        try:
            index = judger.work_stream()
            if index:
                useful_args = judger.ret_msg
                useful_common_data = {
                    cons.CLIENT_ID: judger.client_id,
                    cons.CLIENT_SECRET: judger.client_secret,
                    cons.DES_KEY: judger.des_key,
                    cons.APPLY_ID: judger.apply_id,
                }
            else:
                raise
            logger.info('useful_args: \n%s\nuseful_common_data: \n%s\n' % useful_args, useful_common_data)

            # TODO args is useful_args and useful_common_data
            # TODO packing the useful messages go to the next part of the syetem
            temp_data = dispatch(useful_common_data, useful_args)

            cache_data = temp_data['cache']
            fresh_data = temp_data['fresh']

            ret_data = fresh_data
            ret_data.update(cache_data)
            data.update({
                cons.APPLY_ID: useful_common_data[cons.APPLY_ID],
                cons.RESPONSE_REQUEST_RES_DATA: ret_data,
            })

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
