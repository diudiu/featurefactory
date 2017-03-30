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
# import os
# import sys
# import django
#
# home_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# sys.path.append(home_path)
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'featurefactory.settings')
# django.setup()

import json
import pymongo
import logging

from braces.views import CsrfExemptMixin
from django.views.generic import View

from apps.featureapi.response import JSONResponse
from apps.integration.tools import do_request, get_token


logger = logging.getLogger('apps.integration')

dataocean_url = "http://apitest.digcredit.com"
dataocean_url_data = dataocean_url + "/source/queryinfo/"
dataocean_url_grant = dataocean_url + "/oauth2/token/"
client_id = "jpWstKTB3bqPLWNoocVncCVVHniytPn6ROHy82Ze"
client_secret = "kXXNuP6IOMYr5WxhZihef4Ub6QbOFRPglX0WPPZ5D2sAydh3vDZTCvuMGRFAwlJcu3LoqlQuzs60XE72mxlisrZfhW2DGGCjUHJojkPhiouYrjKrkBj357ThuC61qupk"
des_key = "sjdguhcphysghcih"


class Simulation(CsrfExemptMixin, View):

    def post(self, request, data_identity):
        data = {
            'status': 1,
            'message': u'操作成功',
        }
        data_identity = data_identity
        req_data = json.loads(request.body)
        try:
            if data_identity in ['personal_info', 'geo_location']:
                content = remote_test(req_data, data_identity)
            else:
                content = local_test(req_data, data_identity)
            # print content
            data.update({"res_data": content})
        except Exception, e:
            logger.error(e.message)
            data.update({
                'status': 0,
                'message': 'error'
            })
        print data
        return JSONResponse(data=data)


def local_test(req_data, data_identity):
    query = {
        'data_identity': data_identity
    }
    query.update(req_data)

    conn = pymongo.MongoClient('192.168.1.198', 27017)
    coll = conn['feature_storage']['test_data']
    data = coll.find_one({'args': query})
    return data.get('data', None)


def remote_test(req_data, data_identity):
    req_data.update({'data_identity': data_identity})
    token = get_token(dataocean_url_grant, client_secret)
    req_data.update({'access_token': token['access_token']})
    content = do_request(dataocean_url_data, req_data, des_key)
    content['res_data'] = json.loads(content['res_data'])
    return content
