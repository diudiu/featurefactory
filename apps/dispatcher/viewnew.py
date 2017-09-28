# -*- coding:utf-8 -*-
import requests
import json
import time
from braces.views import CsrfExemptMixin
import logging

# Create your views here.

from django.views.generic import View
from rest_framework.views import APIView
from apps.featureapi.response import JSONResponse
from apps.dispatcher.interviewnew import RiskControl2

logger = logging.getLogger('apps.dispatcher')


class ApplyCreditView(APIView):
    def post(self, request, *args, **kwargs):
        # 这是第一步 拿到访问数据
        post_data = request.data

        rc2 = RiskControl2()
        # 封装两个系统需要的数据
        data_2_0 = {
            "scan_code_city": post_data.get("scan_code_city", ""),
            "san_code_time": post_data.get("san_code_time", ""),
            "product_code": post_data.get("product_code", ""),
            "name": post_data.get("name", ""),
            "mobile": post_data.get("mobile", ""),
            "product_version": post_data.get("product_version", ""),
            "validation_status": post_data.get("validation_status", True),
            "card_id": post_data.get("card_id", ""),
            "apply_id": post_data.get("apply_id", ""),
            "gps_latitude": post_data.get("gps_latitude", ""),
            "gps_longitude": post_data.get("gps_longitude", ""),
            "call_back": post_data.get("call_back", ""),
        }

        # 访问2.0 得到相应的apply_id
        ret_data = rc2.do_formal_request(data_2_0)
        return JSONResponse(ret_data)


class AsyncCallbackView(CsrfExemptMixin, View):

    def post(self, request, *args, **kwargs):
        # 封装两个系统需要的数据
        post_data = json.loads(request.body)
        rc2 = RiskControl2()
        apply_id_2 = post_data.get("apply_id")
        logger.info("apply_id_2:%s" % apply_id_2)
        ret_data = rc2.do_request_2(post_data)

        return JSONResponse(ret_data)
