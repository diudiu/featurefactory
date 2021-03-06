# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/26
    Change Activity:

"""
import logging
from functools import wraps
import json

from vendor.utils.constant import cons
from vendor.errors.api_errors import *
from apps.featureapi.response import JSONResponse

logger = logging.getLogger('apps.featureapi')


def post_data_check(view_func):
    """
        decorators for request
    """
    @wraps(view_func)
    def _wrapped_view_func(request, *args, **kwargs):
        try:
            request_json = request.request.body
            request_data = json.loads(request_json)
            logger.info('Receive data from request data=%s' % request_data)
            return view_func(request, *args, **kwargs)
        except AttributeError as e:
            data = {
                cons.RESPONSE_REQUEST_STATUS: ResponseCode.REQUEST_TYPE_ERROR,
                cons.RESPONSE_REQUEST_MESSAGE: ResponseCode.message(ResponseCode.REQUEST_TYPE_ERROR),
            }
            logger.error('Response from the decorators of `post_data_check`, data=%s, error_msg=%s, rel_err_msg=%s'
                         % (str(data), ResponseCode.message(ResponseCode.REQUEST_TYPE_ERROR), e.message), exc_info=True)
        except Exception as e:
            data = {
                cons.RESPONSE_REQUEST_STATUS: ResponseCode.FAILED,
                cons.RESPONSE_REQUEST_MESSAGE: e.message,
            }
            logger.error('Response from the decorators of `post_data_check`, data=%s, unknown error, rel_err_msg=%s'
                         % (str(data), e.message), exc_info=True)
        return JSONResponse(data=data)
    return _wrapped_view_func
