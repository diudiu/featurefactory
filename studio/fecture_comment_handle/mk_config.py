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
