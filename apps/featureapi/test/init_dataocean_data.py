# -*- coding:utf-8 -*-

import hashlib
import copy
import os
import string
import random
from importlib import import_module
from datetime import datetime
from pymongo import MongoClient

# MONGO_HOST = '192.168.1.198'
# MONGO_NAME = 'dataocean'
# MONGO_USERNAME = 'dataocean'
# MONGO_PASSWORD = 'Syph@0918'
MONGO_HOST = '120.27.124.31'
MONGO_NAME = 'dataocean_debug'
MONGO_USERNAME = 'dataocean_debug'
MONGO_PASSWORD = 'Syph@dataocean_debug'
MONGO_PORT = 27017


def hash_str(s):
    """Generate hexadecimal string for string:s """
    _hash = ''
    if s:
        _hash = hashlib.md5(s).hexdigest()

    return _hash


def get_mongo_db():
    client = MongoClient(MONGO_HOST, MONGO_PORT)
    client[MONGO_NAME].authenticate(MONGO_USERNAME, MONGO_PASSWORD)
    db = client[MONGO_NAME]
    return db


def random_str(count=6, is_only_digit=False):
    if is_only_digit:
        choice_str = string.digits
    else:
        choice_str = (string.letters + string.digits) * 4
    return ''.join(random.sample(choice_str, count))


def get_deal_identifying():
    datetime_str = datetime.now().strftime('%Y%m%d%H%M%S')
    rand_str = random_str(count=6, is_only_digit=True)

    return 'syph' + datetime_str + rand_str


def insert_mongo(data_identity, req_data, res_data):
    db = get_mongo_db()
    hash_data = copy.deepcopy(req_data)
    if hash_data.get("access_token"):
        del hash_data['access_token']
    if hash_data.get("timestamp"):
        del hash_data['timestamp']
    # print hash_data
    sorted_data = sorted(hash_data.items(), key=lambda d: d[0])
    hstr = hash_str(str(sorted_data))
    # print hstr
    data = dict(data_identity=data_identity,
                request_data=dict(
                    data_identity=data_identity,
                    req_param=req_data,
                    status=1,
                    hstr=hstr,
                    deal_identifying=get_deal_identifying()),
                response_data=res_data)

    assert data['data_identity'] and data['request_data'] and db
    req_col_str = "do_" + data['data_identity'] + "_request"
    res_col_str = "do_" + data['data_identity'] + "_response"
    req_col = getattr(db, req_col_str)
    res_col = getattr(db, res_col_str)

    created_time = datetime.now()
    data['request_data']['created_time'] = created_time
    req_id = req_col.insert(data['request_data'])
    response = dict(response=data['response_data'],
                    request=req_id,
                    created_time=created_time)
    res_id = res_col.insert(response)
    print "do_%s_request--%s do_%s_response--%s" % (req_data['data_identity'], req_id, req_data['data_identity'], res_id)


if __name__ == '__main__':
    path = os.path.dirname(__file__)
    files = os.listdir(path)
    for i in files:
        if i.startswith('dataocean_test_data'):
            f = import_module(i.split('.')[0])
            data = f.data
            print data
            for fecture, v in data.items():
                data_identify = v['data_identify']
                lists = v['req_res']
                for req_res in lists:
                    req_data = req_res['req_data']
                    res_data = req_res['res_data']
                    tmp_req_data = {}
                    for k in req_data:
                        tmp_req_data[u'%s' % k] = u'%s' % req_data[k]
                    insert_mongo(data_identify, tmp_req_data, res_data)
