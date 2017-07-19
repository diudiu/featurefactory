# -*- coding:utf-8 -*-

from braces.views import CsrfExemptMixin

# Create your views here.
from django.views.generic import View
from rest_framework.views import APIView
from apps.featureapi.response import JSONResponse
from settings import *


class ApplyCreditView(APIView):

    def post(self, request, *args, **kwargs):
        data = {
            "message": "这是测试数据"
        }

        post_data = request.data
        
        data_1_0 = post_data
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
        }

        return JSONResponse(data)


class ObtainCreditResultView(APIView):

    def get(self, request, *args, **kwargs):
        data = {
            "message": "这是测试数据"
        }
        return JSONResponse(data)


class AsyncCallbackView(CsrfExemptMixin, View):

    def post(self, request, *args, **kwargs):
        data = {
            "message": "这是测试数据"
        }
        return JSONResponse(data)


class ReceiveResult(CsrfExemptMixin, View):

    def post(self, request, *args, **kwargs):
        data = {
            "message": "这是测试数据"
        }
        return JSONResponse(data)
