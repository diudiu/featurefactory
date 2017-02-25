# -*- coding:utf-8 -*-

age_config = {
    "feature_name": "age",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [("age", "$..content.age", "f_assert_not_null->f_assert_must_digit_or_float")],
    "f_map_and_filter_chain": "m_get_seq_index_value(0)",
    "reduce_chain": "",
    "l_map_and_filter_chain": ''
}

apply_register_duration_config = {
    "feature_name": "apply_register_duration",
    "feature_data_type": "float",
    "default_value": "PositiveSignedFloatTypeDefault",
    "json_path_list": [
        ("application_on", "$.apply_data.application_on", "f_assert_not_null->f_assert_must_basestring"),
        ("registration_on", "$.portrait_data.registration_on", "f_assert_not_null->f_assert_must_basestring")
    ],
    "f_map_and_filter_chain": "m_to_slice(0,10)->f_assert_seq0_gte_seq1->m_get_mon_sub",
    "reduce_chain": "",
    "l_map_and_filter_chain": ''
}

car_count_config = {
    "feature_name": "car_count",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [
        ("application_on", "$.result", "f_assert_must_list"),
    ],
    "f_map_and_filter_chain": "f_not_null->m_to_len",
    "reduce_chain": "",
    "l_map_and_filter_chain": ""
}

car_number_config = {
    "feature_name": "car_number",
    "feature_data_type": "list",
    "default_value": "ListTypeDefault",
    "json_path_list": [
        ("license_no", "$..license_no", ""),
    ],
    "f_map_and_filter_chain": "f_not_null",
    "reduce_chain": "",
    "l_map_and_filter_chain": ""
}

cur_company_config = {
    "feature_name": "cur_company",
    "feature_data_type": "string",
    "default_value": "StringTypeDefault",
    "json_path_list": [
        ("work_exp_form", "$..work_exp_form", "f_assert_must_list"),
    ],
    "f_map_and_filter_chain": "m_get_new_list(work_end,comp_name)->m_seq_inx0_sort_in_list(True)"
                              "->m_get_seq_index_value(0)->m_get_seq_index_value(1)->f_assert_not_null",
    "reduce_chain": "",
    "l_map_and_filter_chain": ""
}
