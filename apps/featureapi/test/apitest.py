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
    # url = 'http://192.168.1.196:8071/syph-ff/feature/extract/'
    url = 'http://127.0.0.1:10012/syph-ff/feature/extract/'
    # url = 'http://192.168.1.100:8071/syph-ff/feature/extract/'
    # url = 'http://de.digcredit.com:8071/syph-ff/feature/extract/'
    # url = 'http://139.129.220.118:10012/syph-ff/feature/extract/'
    test_data = {
        u'content': {
            u'callback': '',
            u'apply_id': u'APPLY20170725104516684093829',
            u'res_keys':
                [
                    "c_d_c_a003",
                    "c_d_m_c113",
                    "c_d_m_c133",
                    "c_d_m_c136",
                    "c_d_m_c260",
                    "c_d_t_b004",
                    "c_d_t_b019",
                    "c_d_t_b045",
                    "c_d_t_b046",
                    "c_d_t_b061",
                    "c_d_t_b064",
                    "c_d_t_b065",
                    "c_d_t_b066",
                    "c_d_t_b122",
                    "c_d_t_b230",
                    "c_d_t_b260",
                    "c_d_t_b268",
                    "c_d_t_b292",
                    "c_d_t_b296",
                    "c_d_t_c035",
                    "c_d_t_c048",
                    "c_d_t_c050",
                    "c_d_t_t027",
                    "c_d_t_t040",
                    "c_d_t_t079",
                    "c_d_t_t092",
                    "c_d_t_t094",
                    "c_d_t_t097",
                    "c_d_t_t106",
                    "c_s_r_l001",
                    "c_s_r_l003",
                    "c_s_w_c002",
                    # "is_owner_mobile",
                    "age",
                    # "card_id_two_elem",
                    # "mobile_online_time",
                    # "is_loan_agency",
                    # "is_court_shixin",
                    # "is_organization_g_black",
                    # "is_netsky_black",
                    # "is_netsky_longloan",
                    # "is_skyeye_black",
                    "gender",
                    "credit_card_iden",
                    # "is_credit_card",
                    "call_pay_average",
                    "phone_remain",
                    "credit_limit",
                    "available_balance",
                    #
                    "loan_cnt",
                    "arrears_limit",
                    "apply_limit",
                    "acc_overdue_cnt",
                    "disposable_personal_income",
                    "credit_card_cnt",
                    "san_code_time",
                    # "is_equal61",
                    # "is_gps_location_scan_same",
                ]
        },
        u'client_code': u'bfm_test'
    }
    a = time.time()
    response = requests.post(url, headers=headers, data=json.dumps(test_data))
    content = json.loads(response.content)
    print content
    print time.time() - a


def rule_engine_post():
    url = 'http://192.168.1.25:8080/syph-re/api/credit/apply/async/'
    data = {
        "product_code": "cf5b6d062260f643d123ae61a37fe416",
        "call_back": "aaaaa",
        "data_identity": "aaaaa",
        "apply_id": "aaaaaa",
        "mobile": "13333333333",
        "name": "文儿哥",
        "card_id": "130202199108101423",
        "scan_code_city": u"北京",
        "scan_code_time": time.time(),
        "gps_longitude": "108.85492143460727",
        "gps_latitude": "34.198012456599415",
        "select_address": u"北京",
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    content = json.loads(response.content)
    print content


if __name__ == '__main__':
    # rule_engine_post()
    feature_post()
