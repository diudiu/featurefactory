# -*- coding:utf-8 -*-
from apps.common.dispatcher import process_dispatch, data_get_dispatch
from braces.views import CsrfExemptMixin
from django.views.generic import View
import json
import logging
import requests
from apps.featureapi.response import JSONResponse
from vendor.utils.encrypt import Cryption
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

logger = logging.getLogger('apps.featureapi')
# dataocean_url = "http://127.0.0.1:8001"
dataocean_url = "http://apitest.digcredit.com"
dataocean_url_data = dataocean_url + "/source/queryinfo/"
dataocean_url_grant = dataocean_url + "/oauth2/token/"
client_id = "jpWstKTB3bqPLWNoocVncCVVHniytPn6ROHy82Ze"
client_secret = "kXXNuP6IOMYr5WxhZihef4Ub6QbOFRPglX0WPPZ5D2sAydh3vDZTCvuMGRFAwlJcu3LoqlQuzs60XE72mxlisrZfhW2DGGCjUHJojkPhiouYrjKrkBj357ThuC61qupk"
des_key = 'sjdguhcphysghcih'


def do_request(url, data, des_key):
    json_data = json.dumps(data, encoding="UTF-8", ensure_ascii=False)
    # print "gyf---------", json_data
    req_data = Cryption.aes_base64_encrypt(json_data, des_key)
    content = requests.post(url, json.dumps({"req_data": req_data,
                                             "client": client_id},
                                            encoding="UTF-8", ensure_ascii=False)).content
    content = json.loads(content)
    if content.get('res_data', None):
        content['res_data'] = Cryption.aes_base64_decrypt(content['res_data'], des_key)
    return content


def get_token(url, client_secret):
    grant_type = "client_credentials"
    datas = dict(grant_type=grant_type,
                 client_secret=client_secret,
                 )
    content = do_request(url, datas, des_key)
    # print content
    token = json.loads(content['res_data'])
    return token


class ProcessDispatch(CsrfExemptMixin, View):
    @staticmethod
    def post(request):
        data = json.loads(request.body)
        data = process_dispatch(data)
        return JSONResponse(data)


class DataGetDispatch(CsrfExemptMixin, View):
    @staticmethod
    def post(request):
        data = json.loads(request.body)
        data = data_get_dispatch(data)
        return JSONResponse(data)


class DataOceanTest(CsrfExemptMixin, View):
    # @staticmethod
    def post(self, request, data_identity):
        data = {
            "status": 1,
            "message": "操作成功"
        }

        try:
            logger.info(request.body)
            json_data = request.body
            if isinstance(json_data, basestring):
                req_data = json.loads(json_data)["req_data"]
                req_data.update({'data_identity': data_identity})

            token = get_token(dataocean_url_grant, client_secret)
            req_data.update({"access_token": token["access_token"]})
            print req_data
            content = do_request(dataocean_url_data, req_data, des_key)
            # print content
            data.update({"res_data": content})

        except Exception, e:
            print e.message

            data.update({
                'status': 0,
                'message': 'error'
            })
        print data
        return JSONResponse(data=data)
