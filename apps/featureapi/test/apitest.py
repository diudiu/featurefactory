# -*- coding:utf-8 -*-

import requests
import json
import time

# from vendor.utils.encrypt import Cryption

headers = {
    "Content-type": "application/json; charset=utf-8",
}
des_key = 'yyyyyyuuuuoooooo'
no_disease_list = [

]


def feature_post():
    url = 'http://127.0.0.1:9999/syph-ff/feature/extract/'
    # url = 'http://192.168.1.199:9900/syph-ff/feature/extract/'
    data = {
        u'content': {
            u'callback': u'',
            u'apply_id': u'APPLY201703081545051dxdinger',
            # u'apply_id': u'APPLY20170308154505179ydlisi',
            # u'apply_id': u'APPLY2017030815450ltzhangsan',
            u'res_keys': [
                # u'is_court_zhixing',
                u'is_net_black',
                # u'income_level',
                # u'overload_count'
            ]
        },
        u'client_code': u'lp_test'
    }
    a = time.time()
    response = requests.post(url, headers=headers, data=json.dumps(data))
    content = json.loads(response.content)
    print content
    print time.time() - a


if __name__ == '__main__':
    feature_post()
