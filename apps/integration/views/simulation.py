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
# import logging
import requests

from braces.views import CsrfExemptMixin
from django.views.generic import View

from apps.featureapi.response import JSONResponse
from apps.integration.tools import do_request, get_token


# logger = logging.getLogger('apps.featureapi')

dataocean_url = "http://apitest.digcredit.com"
dataocean_url_data = dataocean_url + "/source/queryinfo/"
dataocean_url_grant = dataocean_url + "/oauth2/token/"
client_id = "jpWstKTB3bqPLWNoocVncCVVHniytPn6ROHy82Ze"
client_secret = "kXXNuP6IOMYr5WxhZihef4Ub6QbOFRPglX0WPPZ5D2sAydh3vDZTCvuMGRFAwlJcu3LoqlQuzs60XE72mxlisrZfhW2DGGCjUHJojkPhiouYrjKrkBj357ThuC61qupk"
des_key = 'sjdguhcphysghcih'


class Simulation(CsrfExemptMixin, View):

    def post(self, request, data_identity):
        data = {
            'status': 1,
            'message': u'操作成功',
        }
        data_identity = data_identity
        req_data = json.loads(request.body)
        try:
            content = remote_test(req_data, data_identity)
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


def remote_test(req_data, data_identity):
    req_data.update({'data_identity': data_identity})
    token = get_token(dataocean_url_grant, client_secret)
    req_data.update({"access_token": token["access_token"]})
    content = do_request(dataocean_url_data, req_data, des_key)
    content['res_data'] = json.loads(content['res_data'])
    return content
