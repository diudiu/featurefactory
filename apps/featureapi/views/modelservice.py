# -*- coding: utf-8 -*-

import logging

from braces.views import CsrfExemptMixin
from django.http.response import JsonResponse
from django.views.generic import View

from apps.featureapi.models import ClientOverview
from apps.pregranting.settings import get_pre_grant_model
from vendor.messages.response_code import ResponseCode
from vendor.errors.api_errors import UserIdentityError

logger = logging.getLogger('apps.featureapi')


class IdentityVerifyMixin(object):
    def verify(self):
        client_code = getattr(self, "client_code", None)
        if client_code is None:
            return False

        client_verify = ClientOverview.objects.filter(client_code=client_code)
        if client_verify.exists():
            return True

        return False


class ModelPreGranting(CsrfExemptMixin, IdentityVerifyMixin, View):

    def __init__(self, **kwargs):
        super(ModelPreGranting, self).__init__(**kwargs)
        self.client_code = None

    def get(self, request, client_code, proposer_id, *args, **kwargs):
        data = {
            'status': ResponseCode.SUCCESS,
            'message': ResponseCode.message(ResponseCode.SUCCESS)
        }
        self.client_code = client_code

        logger.info('Model pre granting, client_code=%s, proposer_id=%s', client_code, proposer_id)

        try:
            # check client_code is not valid
            if not self.verify():
                raise UserIdentityError()

            # 用proposer_id 获取
            model = get_pre_grant_model(proposer_id)
            pre_grant_amount = model.grant()

            data.update({
                'res_data': {
                    'result': 1,
                    'result_message': u'业务处理成功',
                    'pre_grant_amount': pre_grant_amount
                }
            })
        except (UserIdentityError, ) as e:
            logger.error(e.message)

            data.update({
                'status': e.status,
                'message': e.message
            })
        except Exception, e:
            logger.error(e)

            data.update({
                'status': ResponseCode.FAILED,
                'message': ResponseCode.message(ResponseCode.FAILED)
            })

        logger.info("response data = %s", data)
        return JsonResponse(data=data)
