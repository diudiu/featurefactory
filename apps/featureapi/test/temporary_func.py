# -*- coding:utf-8 -*-

import time


def temporary_func(content):
    data = {
        "age": 20,
        "gender": "男",
        "is_skyeye_black": "否",
        "is_net_black": "否",
        "is_loan_agency": "否",
        "is_netsky_longloan": "否",
        "is_court_shixin": "否",
        "has_negative_info": "否",
        "is_organization_g_black": "否",
        "is_netsky_black": "否",
        "is_owner_mobile": "是",
        "card_id_two_elem": "是",
        "mobile_online_time": "[6_12)",
        "is_mobile_local_scan_same": "是",
        "home_address": "是",
        "is_gps_location_scan_same": "是",
        "is_netsky_grey": "否",
        "is_court_zhixing": "否",
        "san_code_time": "11:31 - 14:00",
        "loan_cnt": 5,
        "arrears_limit": 6000,
        "apply_limit": 6000,
        "acc_overdue_cnt": 5,
        "disposable_personal_income": 6000,
        "credit_card_cnt": 4,
        "call_pay_average": 80,
        "phone_remain": 50,
        "credit_limit": 50000,
        "available_balance": 4000,
        "c_d_c_a003": "贷记卡",
        "c_s_w_c002": 50,
        "c_s_r_l003": 50000,
        "c_d_t_t106": 40,
        "c_d_t_b292": 40000,
        "c_d_t_b296": "2",
        "c_d_t_t094": "是",
        "c_d_t_t097": 5,
        "c_d_t_b260": 60000,
        "c_d_t_t027": 6,
        "c_d_t_t040": 5000,
        "c_d_m_c133": 8,
        "c_d_m_c136": 60000,
        "c_d_t_t079": 20,
        "c_d_t_t092": 40,
        "c_d_t_b065": 60000,
        "c_d_t_b066": 8,
        "c_d_t_b061": 8000,
        "c_d_t_b064": 40000,
        "c_d_m_c260": 6000,
        "c_d_t_c035": 600,
        "c_d_t_c050": 400,
        "c_d_m_c113": 300,
        "c_d_t_b004": 40,
        "c_d_t_b019": 100000,
        "c_d_t_b230": 30,
        "c_d_t_b122": 800000,
        "c_s_r_l001": 30000,
        "c_d_t_b268": 8000,
        "is_credit_card": "是",
        "credit_card_iden": "是",
    }
    keys = content.get("res_keys")
    res_data = {}
    for k in keys:
        res_data.update({
            k: data[k]
        })
    time.sleep(1.5)

    return res_data
