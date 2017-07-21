# -*- coding:utf-8 -*-
import requests
import json
from braces.views import CsrfExemptMixin
import logging

# Create your views here.

from django.views.generic import View
from rest_framework.views import APIView
from apps.featureapi.response import JSONResponse
from apps.dispatcher.interviews import RiskControl1
from apps.dispatcher.interviews import RiskControl2
from vendor.utils.cache import RedisX
logger = logging.getLogger('apps.dispatcher')


class ApplyCreditView(APIView):
    def post(self, request, *args, **kwargs):
        post_data = request.data

        rc1 = RiskControl1()
        rc2 = RiskControl2()
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
        ret_data_list = rc1.do_request_1_apply(post_data)
        apply_id_1 = ret_data_list[0]
        ret_data = ret_data_list[1]
        apply_id_2 = rc2.do_formal_request(data_2_0, data_1_0)
        red = RedisX()
        redis_status = {
            "status": "RUNNING",
            "apply_id_2_0": apply_id_2
        }
        red.set(apply_id_1, json.dumps(redis_status))
        red.set(apply_id_2, apply_id_1)
        return JSONResponse(json.loads(ret_data))


class ObtainCreditResultView(APIView):
    def get(self, request, *args, **kwargs):
        red = RedisX()
        rc1 = RiskControl1()
        apply_id = request.query_params.get("apply_id")
        not_ok_data = {"status": 1, "res_data": {"result": 100, "result_message": "审核中"}, "message": "操作成功"}
        redis_status = red.get(apply_id)
        if redis_status:
            redis_status = json.loads(redis_status)
        if redis_status.get("status") == "OK":
            ret_data = rc1.do_request_1_result(request.query_params)
            logger.info("1.0 result go back, data is: %s" % ret_data)
            return JSONResponse(ret_data)
        else:
            return JSONResponse(not_ok_data)


class AsyncCallbackView(CsrfExemptMixin, View):
    def post(self, request, *args, **kwargs):
        post_data = json.loads(request.body)
        rc1 = RiskControl1()
        rc2 = RiskControl2()
        ret_data_list = rc1.do_request_1_callback(request.body)
        red = RedisX()
        apply_id_1 = ret_data_list[0]
        apply_id_2 = red.get(apply_id_1)
        ret_data = ret_data_list[1]
        rc2.do_request_2(post_data, apply_id_2)
        return JSONResponse(JSONResponse(json.loads(ret_data)))


class ReceiveResult(CsrfExemptMixin, View):

    def post(self, request, *args, **kwargs):
        red = RedisX()
        req_data = json.loads(request.body)
        logger.info("2.0 callback data is: %s" % req_data)
        apply_id_2 = req_data.get("apply_id")
        apply_id_1 = red.get(apply_id_2)
        redis_status_json = red.get(apply_id_1)
        logger.info("receive result redis data is: %s" % redis_status_json)
        redis_status = json.loads(redis_status_json)
        redis_status.update({"status": "OK"})
        red.set(apply_id_1, json.dumps(redis_status))
        res_data = {
            "status": 1,
            "message": "结果接收成功",
            "resData": req_data,
        }
        return JSONResponse(res_data)
