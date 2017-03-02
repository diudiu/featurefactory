# -*- coding:utf-8 -*-

jiuyao_multi_loan_denied_count_config = {
    "feature_name": "jiuyao_multi_loan_denied_count",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [
        ("contract_date", "$..loanInfos[*].contractDate", "f_assert_not_null"),
    ],
    "f_map_and_filter_chain": "f_digit_or_float->f_days_greater_than_args(180)",
    "reduce_chain": "m_to_len",
    "l_map_and_filter_chain": ""
}

jiuyao_multi_loan_m2_count_config = {
    "feature_name": "jiuyao_multi_loan_m2_count",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [
        ("repay_state", "$..loanInfos[*].repayState", "f_assert_not_null->f_digit_or_float"),
    ],
    "f_map_and_filter_chain": "f_inside_stipulate_scope([3, 4, 5, 6, 7, 8])",
    "reduce_chain": "m_to_len",
    "l_map_and_filter_chain": ""
}

is_unclear_loan_config = {
    "feature_name": "is_unclear_loan",
    "feature_data_type": "int",
    "default_value": "BooleanTypeDefault",
    "json_path_list": [
        ("is_unclear_loan", "$..res_data.is_unclear_loan", "f_assert_not_null->f_assert_must_digit"),
    ],
    "f_map_and_filter_chain": "m_to_int->m_to_sum",
    "reduce_chain": "",
    "l_map_and_filter_chain": "m_to_bool(1)"
}

mobile_area_city_code_config = {
    "feature_name": "mobile_area_city_code",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [
        ("mobile_area", "$..content.mobile_area", "f_assert_not_null->f_assert_must_basestring"),
    ],
    "f_map_and_filter_chain": "m_get_seq_index_value(0)->m_get_city_name->f_assert_not_null->m_city_name_to_code",
    "reduce_chain": "",
    "l_map_and_filter_chain": ""
}

gps_city_code_config = {
    "feature_name": "mobile_area_city_code",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [
        ("mobile_area", "$..addressComponent.city", "f_assert_not_null->f_assert_must_basestring"),
    ],
    "f_map_and_filter_chain": "m_get_seq_index_value(0)->m_get_city_name->f_assert_not_null->m_city_name_to_code",
    "reduce_chain": "",
    "l_map_and_filter_chain": ""
}

cur_work_status_config = {
    "feature_name": "cur_work_status",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [
        ("mobile_area", "$..cur_work_status", "f_assert_not_null->f_assert_must_basestring"),
    ],
    "f_map_and_filter_chain": "m_get_work_status_map('cur_work_status')",
    "reduce_chain": "",
    "l_map_and_filter_chain": ""
}

now_workplace_code_config = {
    "feature_name": "now_workplace_code",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [
        ("industry", "$..work_exp_form[*].industry", "f_assert_not_null->f_assert_must_basestring"),
        ("work_end", "$..work_exp_form[*].work_end", "f_assert_not_null->f_assert_must_basestring"),
    ],
    "f_map_and_filter_chain": "f_get_workplace_now",
    "reduce_chain": "",
    "l_map_and_filter_chain": ""
}

work_time_config = {
    "feature_name": "work_time",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [
        ("industry", "$..work_exp_form[*].work_start", "f_not_null->f_assert_must_basestring"),
        ("work_end", "$..work_exp_form[*].work_end", "f_not_null->f_assert_must_basestring"),
    ],
    "f_map_and_filter_chain": "",
    "reduce_chain": "m_get_month_from_now",
    "l_map_and_filter_chain": ""
}


mobile_identity_config = {
    "feature_name": "mobile_identity",
    "feature_data_type": "int",
    "default_value": "BooleanTypeDefault",
    "json_path_list": [
        ("mobile_identity", "$.unicom_mobile_identity_s.result", "m_mobile_id_judge"),
        ("mobile_identity", "$.yd_mobile_identity_s.result", "m_mobile_id_judge"),
        ("mobile_identity", "$.telecom_mobile_identity_s.result", "m_mobile_id_judge"),
    ],
    "f_map_and_filter_chain": "m_to_sum",
    "reduce_chain": "",
    "l_map_and_filter_chain": ""
}
