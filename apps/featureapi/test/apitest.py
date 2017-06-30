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
    url = 'http://127.0.0.1:9999/syph-ff/feature/extract/'
    # url = 'http://192.168.1.199:9900/syph-ff/feature/extract/'
    # data = {
    #     u'content': {
    #         u'callback': '',
    #         u'apply_id': u'APPLY20170622144300255261193',
    #         u'res_keys':
    #         [
    #             # 'age',                            # 测试通过
    #             # 'gender',                         # 测试通过
    #             # 'home_address',                   # 测试通过  返回籍贯具体字符串  未加处理
    #             # 'is_skyeye_black',                # 测试通过
    #             # 'is_loan_agency',                 # 测试通过
    #             # 'is_netsky_longloan',             # 测试通过
    #             # 'is_court_shixin',                # 测试通过
    #             # 'is_organization_g_black',        # 测试通过
    #             # 'is_netsky_black',                # 测试通过
    #             # 'is_owner_mobile',                # 测试通过
    #             # 'card_id_two_elem',               # 测试通过
    #             # 'is_netsky_grey',                 # 测试通过
    #             # 'is_court_zhixing',               # 测试通过
    #             # 'c_d_c_a003',                     # 测试通过
    #             # 'c_s_w_c002',                     # 测试通过
    #             # 'c_s_r_l003',                     # 测试通过
    #             # 'c_d_t_t106',                     # 测试通过
    #             # 'c_d_t_b292',                     # 测试通过
    #             # 'c_d_t_b296',                     # 测试通过
    #             # 'c_d_t_t094',                     # 测试通过
    #             # 'c_d_t_t097',                     # 测试通过
    #             # 'c_d_t_b260',                     # 测试通过
    #             # 'c_d_t_t027',                     # 测试通过
    #             # 'c_d_t_t040',                     # 测试通过
    #             # 'c_d_m_c133',                     # 测试通过
    #             # 'c_d_m_c136',                     # 测试通过
    #             # 'c_d_t_t079',                     # 测试通过
    #             # 'c_d_t_t092',                     # 测试通过
    #             # 'c_d_t_b065',                     # 测试通过
    #             # 'c_d_t_b066',                     # 测试通过
    #             # 'c_d_t_b061',                     # 测试通过
    #             # 'c_d_t_b064',                     # 测试通过
    #             # 'c_d_m_c260',                     # 测试通过
    #             # 'c_d_t_c035',                     # 测试通过
    #             # 'c_d_t_c050',                     # 测试通过
    #             # 'c_d_m_c113',                     # 测试通过
    #             # 'c_d_t_b004',                     # 测试通过
    #             # 'c_d_t_b019',                     # 测试通过
    #             # 'c_d_t_b230',                     # 测试通过
    #             # 'c_d_t_b122',                     # 测试通过
    #             # 'c_s_r_l001',                     # 测试通过
    #             # 'c_d_t_b268',                     # 测试通过
    #             # 'name',                           # 测试通过
    #             # 'card_id',                        # 测试通过
    #             # 'san_code_time',                  # 测试通过
    #             'loan_cnt',                       # 借款信用历史接口
    #             'arrears_limit',                  # 借款信用历史接口
    #             'apply_limit',                    # 借款信用历史接口
    #             'acc_overdue_cnt',                # 借款信用历史接口
    #             # 'is_credit_card',
    #             # 'credit_card_iden',
    #             # 'has_children',
    #             # 'is_on_job',
    #             # 'is_married',
    #             # 'amount',
    #             # 'monthly_consume_amount_rank',
    #             # 'call_pay_average',
    #             # 'has_night_consume',
    #             # 'credit_times',
    #             # 'm3_credit_consume_amount',
    #             # 'repayment_ability',
    #             # 'address_and_scan_address',
    #             # 'sex_age',
    #             # 'is_mobile_local_scan_same',
    #             # 'is_gps_location_scan_same',
    #             # 'phone_remain',
    #             # 'credit_limit',
    #             # 'available_balance',
    #             # 'mobile_online_time',             尝试联通电信,  无数据尝试移动, 号码不对会报数据格式错误
    #
    #         ]
    #     },
    #     u'client_code': u'bfm_test'
    # }
    test_data = {
        u'content': {
            u'callback': '',
            u'apply_id': u'APPLY20170622144300255261193',
            u'res_keys':
                [
                    # "c_d_c_a003",
                    # "c_d_m_c113",
                    # "c_d_m_c133",
                    # "c_d_m_c136",
                    # "c_d_m_c260",
                    # "c_d_t_b004",
                    # "c_d_t_b019",
                    # "c_d_t_b045",
                    # "c_d_t_b046",
                    # "c_d_t_b061",
                    # "c_d_t_b064",
                    # "c_d_t_b065",
                    # "c_d_t_b066",
                    # "c_d_t_b122",
                    # "c_d_t_b230",
                    # "c_d_t_b260",
                    # "c_d_t_b268",
                    # "c_d_t_b292",
                    # "c_d_t_b296",
                    # "c_d_t_c035",
                    # "c_d_t_c048",
                    # "c_d_t_c050",
                    # "c_d_t_t027",
                    # "c_d_t_t040",
                    # "c_d_t_t079",
                    # "c_d_t_t092",
                    # "c_d_t_t094",
                    # "c_d_t_t097",
                    # "c_d_t_t106",
                    # "c_s_r_l001",
                    # "c_s_r_l003",
                    # "c_s_w_c002",
                    # u"is_owner_mobile",
                    # u"age",
                    # u"card_id_two_elem",
                    # u"mobile_online_time",
                    # u"is_loan_agency",
                    # u"is_court_shixin",
                    # u"is_organization_g_black",
                    # u"is_netsky_black",
                    # u"is_netsky_longloan",
                    # u"is_skyeye_black",
                    "isEqual61",
                    "creditCardIden",
                    "isCreditCard",
                    "callPayAverage",
                    "phoneRemain",
                    "creditLimit",
                    "availableBalance",
                    "age",
                    "gender",
                    "mobileOnlineTime",
                    "sanCodeTime",
                    "loanCnt",
                    "arrearsLimit",
                    "applyLimit",
                    "accOverdueCnt",
                    "disposablePersonalIncome",
                    "creditCardCnt",
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
