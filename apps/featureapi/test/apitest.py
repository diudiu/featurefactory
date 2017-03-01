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
        'client_code': 'lp_test',
        'content': {
            'apply_id': 'APPLY20170213143121831017716',
            'callback_url': '',
            'res_keys': [
                'age',
                'airfare_sum_12',
                'application_on',
                'application_on_plus',
                'apply_register_duration',
                'car_count',
                'car_number',
                'card_id',
                'cc_bill_age',
                'company_addr_city_level',
                'complete_degree',
                'contacts',
                'creditcard_count',
                'cur_company',
                'cur_corp_years',
                'cur_employee_number',
                'cur_work_status',
                'dc_bill_age',
                'education_degree_code',
                'education_tz',
                'folk',
                'gender',
                'gps_city_code',
                'graduate_college',
                'has_negative_info',
                'income_level',
                'industry_change_count',
                'is_court_shixin',
                'is_court_zhixing',
                'is_cur_corp_shixin',
                'is_jiuyao_multi_loan',
                'is_loan_agency',
                'is_mobile_black',
                'is_netsky_black',
                'is_netsky_multi_loan',
                'is_organization_g_black',
                'is_pingan_financial_shixin',
                'is_pingan_multi_loan',
                'is_pingan_overdue_loan',
                'is_skyeye_black',
                'jiuyao_multi_loan_denied_count',
                'jiuyao_multi_loan_m2_count',
                'last_industry_code',
                'loan_infos',
                'marital_status',
                'max_flight_area',
                'max_flight_class',
                'mobile',
                'mobile_area_city_level',
                'mobile_area_code',
                'mobile_identity',
                'mobile_mark',
                'name',
                'now_industry_code',
                'now_work_time',
                'now_workplace_code',
                'online_time',
                'pingan_max_overdue_days',
                'pingan_multi_loan_count',
                'pingan_multi_loan_infos',
                'pingan_overdue_corp_count',
                'work_time',
                'pingan_other_loan_count',
                'mobile_stability',
                'is_pingan_other_loan',
                'graduate_college_check',
                'register_city_level',
                'pingan_overdue_count',
                'pingan_other_loan_infos',
                'is_netsky_grey',
                'mobile_activeness',
                'pingan_overdue_loan_infos',
                'education_degree_check',
                'college_type',
                'income_expense_comparison',
                'is_recruitment',
                'is_unclear_loan',
                'overload_count',
                'overspeed_count',
            ],
        },
    }
    a = time.time()
    response = requests.post(url, headers=headers, data=json.dumps(data))
    content = json.loads(response.content)
    print content
    print time.time() - a

if __name__ == '__main__':
    feature_post()
