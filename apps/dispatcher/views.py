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
from apps.dispatcher.interviews import RiskControl1
from apps.dispatcher.interviews import RiskControl2
from vendor.utils.cache import RedisX
logger = logging.getLogger('apps.dispatcher')


class ApplyCreditView(APIView):
    def post(self, request, *args, **kwargs):
        # 这是第一步 拿到访问数据
        post_data = request.data

        rc1 = RiskControl1()
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
        }

        # 访问风控1.0, 得到相应的apply_id和返回数据
        ret_data_list = rc1.do_request_1_apply(post_data)
        apply_id_1 = ret_data_list[0]
        logger.info("ApplyCreditView apply_id_1: %s" % apply_id_1)
        ret_data = ret_data_list[1]

        # 访问2.0 得到相应的apply_id
        apply_id_2 = rc2.do_formal_request(data_2_0)
        if apply_id_2:
            logger.info("ApplyCreditView apply_id_2: %s" % apply_id_2)
        else:
            apply_id_2 = "Error%s" % int(time.time()*1000)
            logger.error("ApplyCreditView apply_id_2: %s" % apply_id_2)

        red = RedisX()

        # 准备redis数据 包含审核状态和 apply_id映射
        redis_status = {
            "status": "RUNNING",
            "apply_id_2_0": apply_id_2
        }
        # 储存第一个redis数据, 以apply_id1做键 redis数据转json串做值
        red.set(apply_id_1, json.dumps(redis_status))

        # 储存第二个redis数据, apply_id2与apply_id1的映射
        # redis两条数据保证通过任意apply_id可以找到另一个apply_id
        red.set(apply_id_2, apply_id_1)

        # 返回1.0返回信息 表示审核任务提交状况
        return JSONResponse(json.loads(ret_data))


class ObtainCreditResultView(APIView):

    def get(self, request, *args, **kwargs):

        # 获取结果接口
        red = RedisX()
        rc1 = RiskControl1()
        # 获取需要获取的申请人apply_id  此时是1.0版本的apply_id
        apply_id = request.query_params.get("apply_id")
        logger.info("apply_id_1: %s" % apply_id)
        # 拼装返回正在审核中的返回结果
        not_ok_data = {"status": 1, "res_data": {"result": 100, "result_message": "审核中"}, "message": "操作成功"}
        # 取得redis中的状态信息
        redis_status = red.get(apply_id)
        if redis_status:
            redis_status = json.loads(redis_status)
            apply_id_first_req = red.get("%s_first_req" % apply_id)
            if apply_id_first_req:
                time_interval = int(time.time())-int(apply_id_first_req)
                if time_interval > 180:
                    redis_status["status"] = "OK"
            else:
                red_ret = red.set("%s_first_req" % apply_id, int(time.time()))

        else:
            apply_id_2 = "Error%s" % int(time.time() * 1000)
            redis_status = {"status": "OK", "apply_id_2_0": apply_id_2}
            logger.error("ObtainCreditResultView apply_id_1:%s redis_status: %s " % (apply_id, redis_status))
        # 如果redis状态表示审核完成, 调用1.0获取结果接口, 透传返回信息
        if redis_status.get("status") == "OK":
            ret_data = rc1.do_request_1_result(request.query_params)
            logger.info("1.0 result go back, data is: %s" % ret_data)
            return JSONResponse(ret_data)

        # redis状态表示审核中(未完成), 直接返回审核中
        else:
            return JSONResponse(not_ok_data)


class AsyncCallbackView(CsrfExemptMixin, View):

    def post(self, request, *args, **kwargs):
        # 封装两个系统需要的数据
        post_data = json.loads(request.body)
        rc1 = RiskControl1()
        rc2 = RiskControl2()
        # 访问风控1.0, 得到相应的apply_id和返回数据
        ret_data = rc1.do_request_1_callback(json.dumps(post_data))
        apply_id_1 = post_data.get("apply_id")
        logger.info("apply_id_1:%s" % apply_id_1)

        red = RedisX()
        redis_status = red.get(apply_id_1)
        if redis_status:
            redis_status = json.loads(redis_status)
        else:
            apply_id_2 = "Error%s" % int(time.time() * 1000)
            redis_status = {"status": "RUNNING", "apply_id_2_0": apply_id_2}

        # 获取对应2.0的apply_id
        apply_id_2 = redis_status.get("apply_id_2_0")
        logger.info("apply_id_2:%s" % apply_id_2)

        if apply_id_2.startswith("Error"):
            redis_status["status"] = "OK"
            logger.error("AsyncCallbackView apply_id_2:%s skip! apply_id_1:%s post_data:%s" % (apply_id_2, apply_id_1, post_data))
        else:
            time.sleep(3)
            rc2.do_request_2(post_data, apply_id_2)

            # 准备redis数据 包含审核状态和 apply_id映射 状态改为RUNNING
            redis_status["status"] = "RUNNING"

        # 储存第一个redis数据, 以apply_id1做键 redis数据转json串做值
        red.set(apply_id_1, json.dumps(redis_status))

        return JSONResponse(ret_data)


class ReceiveResult(CsrfExemptMixin, View):

    def post(self, request, *args, **kwargs):

        # 接收2.0系统审核完成结果接口, 触发此接口代表2.0审核任务完成
        red = RedisX()
        req_data = json.loads(request.body)
        logger.info("2.0 callback data is: %s" % req_data)
        # 获取2.0的apply_id
        apply_id_2 = req_data.get("apply_id")
        logger.info("apply_id_2: %s"% apply_id_2)
        # 在redis中查得对应的1.0的apply_id
        apply_id_1 = red.get(apply_id_2)
        if not apply_id_1:
            apply_id_1 = "Error%s" % int(time.time() * 1000)
        logger.info("apply_id_1: %s" % apply_id_1)
        # 拿到redis中存储的审核状态
        redis_status_json = red.get(apply_id_1)
        logger.info("receive result redis data is: %s" % redis_status_json)
        if not redis_status_json:
            redis_status_json = json.dumps({"status": "RUNNING", "apply_id_2_0": apply_id_2})
        redis_status = json.loads(redis_status_json)
        redis_status.update({"status": "OK"})

        # 修改状态为OK
        red.set(apply_id_1, json.dumps(redis_status))
        res_data = {
            "status": 1,
            "message": "结果接收成功",
            "resData": req_data,
        }
        # 状态返回给2.0系统 代表审核结果接收成功
        return JSONResponse(res_data)
