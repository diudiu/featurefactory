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
            u'callback': u'http://192.168.1.199:8085/syph-re/api/credit/result/features/',
            u'apply_id': u'APPLY20170308154505179519058',
            u'res_keys': [
                u'cur_work_status',
                u'now_workplace_code',
                u'gps_city_code', u'mobile_area_code',
                u'mobile_activeness',
                u'pingan_multi_loan_count', u'pingan_other_loan_count', u'pingan_overdue_corp_count',
                u'jiuyao_multi_loan_denied_count', u'mobile_mark', u'work_time', u'education_degree_check',
                u'education_degree_code', u'contacts', u'mobile_stability'    , u'last_industry_code',
                u'now_industry_code', u'industry_change_count', u'education_tz'
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
