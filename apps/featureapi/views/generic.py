# -*- coding:utf-8 -*-
"""
    Copyright (c) 2013-2016 SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/22
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
import traceback

from braces.views import CsrfExemptMixin
from django.views.generic import View

from apps.async.tasks import audit_task, mission_control
from apps.common.dispatcher import client_dispatch
from apps.featureapi.decorator import post_data_check
from apps.featureapi.response import JSONResponse
from vendor.errors.api_errors import *
from vendor.errors.contact_error import *
from vendor.utils.constant import cons

from apps.featureapi.test.temporary_func import temporary_func

logger = logging.getLogger('apps.featureapi')


class FeatureExtract(CsrfExemptMixin, View):
    @staticmethod
    def get(request):
        data = {
            'name': 'feature factory',
            'status': 'Success',
            'message': 'feature factory is working',
        }
        return JSONResponse(data)

    # @装饰器验证一下request包完整性
    @post_data_check
    def post(self, request):
        logger.info(request.body)
        post_data = json.loads(request.body)
        # get client code
        logger.info("post_data:%s" % post_data)
        client_code = post_data.get(cons.CLIENT_CODE, None)
        content = post_data.get(cons.RESPONSE_HANDLE_CONTENT, None)
        # if client_code == "bfm_test":
        #     ret_data = temporary_func(content)
        #     data.update({
        #         'ret_msg': ret_data
        #     })
        #     logger.info('Mission completed request data :\n %s' % data)
        #     return JSONResponse(data)
        data = {
            'apply_id': content.get('apply_id', None),
            cons.RESPONSE_REQUEST_STATUS: ResponseCode.SUCCESS,
            cons.RESPONSE_REQUEST_MESSAGE: ResponseCode.message(ResponseCode.SUCCESS)
        }
        try:
            base_data = client_dispatch(client_code, content)
            base_data.update({'apply_id': content.get('apply_id', None)})
            logger.info("base_data: %s" % base_data)
            if base_data['is_async']:
                # ASYNC
                logger.info(
                    '\n============Streams come in ASYNC apply_id: %s===========' % content.get('apply_id', None))
                process_apply_id = content.get('process_apply_id', None)
                task_id = audit_task.apply_async(args=({'apply_id': content.get('apply_id', None)},
                                                       base_data, process_apply_id), retry=True,
                                                 queue='re_task_audit', routing_key='re_task_audit')
                if task_id:
                    logger.info("apply_id: %s task_id:%s" % (content.get('apply_id', None), task_id))
                else:
                    logger.error("audit_task.apply_async don't return task_id")
            else:
                # SYNC
                logger.info('\n============Streams in SYNC mission control center, Collecting feature now===========')
                ret_data = mission_control(base_data)
                data.update({
                    'client_code': base_data.get('client_code', None),
                    'apply_id': base_data.get('apply_id', None),
                    'ret_msg': ret_data
                })
        except ServerError as e:
            traceback.print_exc()
            data = {
                'apply_id': content.get('apply_id', None),
                cons.RESPONSE_REQUEST_STATUS: e.status,
                cons.RESPONSE_REQUEST_MESSAGE: e.message,
                "post_data": content
            }
            logger.error('Mission completed response data :\n %s' % data)
        except Exception as e:
            traceback.print_exc()

            data = {
                'apply_id': content.get('apply_id', None),
                cons.RESPONSE_REQUEST_STATUS: ResponseCode.FAILED,
                cons.RESPONSE_REQUEST_MESSAGE: e.message,
                "post_data": content
            }
            logger.error('Mission completed response data :\n %s' % data)
        else:
            logger.info('Mission completed response data :\n %s' % data)
        return JSONResponse(data)
