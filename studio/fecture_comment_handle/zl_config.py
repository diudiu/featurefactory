# -*- coding: utf-8 -*-

application_on_config = {
    "feature_name": "application_on",
    "feature_data_type": "string",
    "default_value": "StringTypeDefault",
    "json_path_list": [("application_on", "$.application_on", "f_assert_not_null->f_assert_must_basestring")],
    "f_map_and_filter_chain": "m_get_seq_index_value(0)",
    "reduce_chain": "",
    "l_map_and_filter_chain": "",
}


application_on_plus_config = {
    "feature_name": "application_on_plus",
    "feature_data_type": "string",
    "default_value": "StringTypeDefault",
    "json_path_list": [("application_on", "$.application_on", "f_assert_not_null->f_assert_must_basestring")],
    "f_map_and_filter_chain": "m_get_seq_index_value(0)->m_datetime_only_hour_minute",
    "reduce_chain": "",
    "l_map_and_filter_chain": "",
}


cc_bill_age_config = {
    "feature_name": "cc_bill_age",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [("cc_bill_age", "$..result.rrx_once_all.credit_card_account_age", "f_assert_not_null->f_assert_must_digit")],
    "f_map_and_filter_chain": "m_get_seq_index_value(0)",
    "reduce_chain": "",
    "l_map_and_filter_chain": "",
}


complete_degree_config = {
    "feature_name": "complete_degree",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [("complete_degree", "$..complete_degree", "f_assert_not_null->f_assert_must_int")],
    "f_map_and_filter_chain": "m_get_seq_index_value(0)",
    "reduce_chain": "",
    "l_map_and_filter_chain": "",
}


creditcard_count_config = {
    "feature_name": "creditcard_count",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [("creditcard_count", "$..result.rrx_once_all.credit_cards_num", "f_assert_not_null->f_assert_must_digit")],
    "f_map_and_filter_chain": "m_get_seq_index_value(0)",
    "reduce_chain": "",
    "l_map_and_filter_chain": "",
}


dc_bill_age_config = {
    "feature_name": "dc_bill_age",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [("dc_bill_age", "$..result.rrx_once_all.debit_card_account_age", "f_assert_not_null->f_assert_must_digit")],
    "f_map_and_filter_chain": "m_get_seq_index_value(0)",
    "reduce_chain": "",
    "l_map_and_filter_chain": "",
}


education_degree_code_config = {
    "feature_name": "education_degree_code",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [("education_degree_code", "$..degree", "f_assert_not_null->f_assert_must_digit")],
    "f_map_and_filter_chain": "",
    "reduce_chain": "",
    "l_map_and_filter_chain": "",
}


income_level_config = {
    "feature_name": "income_level",
    "feature_data_type": "",
    "default_value": "",
    "json_path_list": [],
    "f_map_and_filter_chain": "",
    "reduce_chain": "",
    "l_map_and_filter_chain": "",
}


is_loan_agency_config = {
    "feature_name": "is_loan_agency",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [("is_loan_agency", "$.result", "f_assert_not_null->f_assert_must_basestring")],
    "f_map_and_filter_chain": "m_to_bool(['00'])",
    "reduce_chain": "",
    "l_map_and_filter_chain": "",
}


is_netsky_black_config = {
    "feature_name": "is_netsky_black",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [("is_netsky_black", "$.result", "f_assert_not_null->f_assert_must_basestring")],
    "f_map_and_filter_chain": "m_to_bool(['00'])",
    "reduce_chain": "",
    "l_map_and_filter_chain": "",
}


is_organization_g_black_config = {
    "feature_name": "is_organization_g_black",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [("is_organization_g_black", "$.result", "f_assert_not_null->f_assert_must_basestring")],
    "f_map_and_filter_chain": "m_to_bool(['00'])",
    "reduce_chain": "",
    "l_map_and_filter_chain": "",
}


is_pingan_multi_loan_config = {
    "feature_name": "is_pingan_multi_loan",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [("is_pingan_multi_loan", "$.result", "f_assert_not_null->f_assert_must_int")],
    "f_map_and_filter_chain": "m_to_bool([0])",
    "reduce_chain": "",
    "l_map_and_filter_chain": "",
}


mobile_mark_config = {
    "feature_name": "mobile_mark",
    "feature_data_type": "string",
    "default_value": "StringTypeDefault",
    "json_path_list": [("mobile_mark", "$.tags.contactMain_IMSI1_IMEI1.label", "f_assert_not_null->f_assert_must_basestring")],
    "f_map_and_filter_chain": "m_get_seq_index_value(0)",
    "reduce_chain": "",
    "l_map_and_filter_chain": "",
}


online_time_config = {
    "feature_name": "online_time",
    "feature_data_type": "",
    "default_value": "",
    "json_path_list": [],
    "f_map_and_filter_chain": "",
    "reduce_chain": "",
    "l_map_and_filter_chain": "",
}


pingan_multi_loan_count_config = {
    "feature_name": "pingan_multi_loan_count",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [("pingan_multi_loan_count", "$..orgNums", "f_not_null->f_assert_must_digit")],
    "f_map_and_filter_chain": "m_to_int->m_to_sum",
    "reduce_chain": "",
    "l_map_and_filter_chain": "",
}


overspeed_count_config = {
    "feature_name": "overspeed_count",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [("overspeed_count", "$..month_times", "f_not_null->f_assert_must_digit")],
    "f_map_and_filter_chain": "m_to_int->m_to_sum",
    "reduce_chain": "",
    "l_map_and_filter_chain": "",
}


overload_count_config = {
    "feature_name": "overload_count",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [("overload_count", "$..month_times", "f_not_null->f_assert_must_digit")],
    "f_map_and_filter_chain": "m_to_int->m_to_sum",
    "reduce_chain": "",
    "l_map_and_filter_chain": "",
}


