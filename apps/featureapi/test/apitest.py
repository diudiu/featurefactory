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
    data = {
        u'content': {
            u'callback': u'',
            # u'apply_id': u'APPLY201703081545051dxdinger',
            # u'apply_id': u'APPLY20170308154505179ydlisi',
            u'apply_id': u'APPLY2017030815450ltzhangsan',
            u'res_keys': [
                # 'age',
                # 'airfare_sum12',
                # 'application_on',
                # u'application_on_plus',
                # 'apply_register_duration',
                # 'car_count',
                # 'car_number',
                # 'card_id',
                # 'cc_bill_age',
                # 'college_type',#
                # 'company_addr_city_level',
                # 'contacts',
                # 'creditcard_count',
                # 'cur_company',
                # 'cur_corp_years', #
                # 'cur_employee_number',#
                # 'cur_work_status',#
                # 'dc_bill_age',
                # 'education_degree_check',#
                # 'education_degree_code',#
                # 'education_tz',
                # 'folk',
                # 'gender',#
                # 'gps_city_code',
                # 'graduate_college',
                # 'graduate_college_check',
                # 'has_negative_info',
                # 'income_expense_comparison',
                # 'income_level',
                # 'industry_change_count',
                # 'is_court_shixin',
                # 'is_court_zhixing',
                # 'is_cur_corp_shixin',
                # 'is_loan_agency',
                # 'is_mobile_black',
                # 'is_net_black',
                # 'is_netsky_black',
                # 'is_netsky_grey',
                # 'is_netsky_multi_loan',
                # 'is_organization_g_black',
                # 'is_recruitment',
                # 'is_skyeye_black',#
                # 'is_unclear_loan',#no
                # 'jiuyao_multi_loan_denied_count',
                # 'jiuyao_multi_loan_m2_count',
                # 'last_industry_code',
                # 'loan_infos',
                # 'marital_status',
                # 'max_flight_area',
                # 'max_flight_class',
                # 'mobile',
                # 'mobile_activeness',
                # 'mobile_area_city_level',
                # 'mobile_area_code',
                # 'mobile_identity',
                # 'mobile_mark',#no
                # 'mobile_stability',
                # 'now_industry_code',
                # 'now_work_time',
                # 'online_time',
                # u'overload_count',
                # 'overspeed_count',
                # 'register_city_level',
                'work_time',
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
