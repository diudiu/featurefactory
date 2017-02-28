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
    "f_map_and_filter_chain": "m_to_slice(0,10)->f_assert_seq0_gte_seq1->m_get_mon_sub(2)",
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
    "f_map_and_filter_chain": "m_get_new_list('work_end','comp_name')->m_seq_inx0_sort_in_list(True)"
                              "->m_get_seq_index_value(0)->m_get_seq_index_value(1)->f_assert_not_null",
    "reduce_chain": "",
    "l_map_and_filter_chain": ""
}


mobile_activeness_config = {
    "feature_name": "mobile_activeness",
    "feature_data_type": "float",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [
        ("tags", "$..tags", "f_assert_must_dict"),
        ("mobile", "$..apply_base.mobile", "f_assert_not_null"),
    ],
    "f_map_and_filter_chain": "f_mobile_m1_m5_sum_max_seq(['callTimes','calledTimes'])->m_get_mobile_stability",
    "reduce_chain": "",
    "l_map_and_filter_chain": ""
}

is_pingan_financial_shixin_config = {
    "feature_name": "is_pingan_financial_shixin",
    "feature_data_type": "bool",
    "default_value": "BooleanTypeDefault",
    "json_path_list": [
        ("others", "$..others", "f_assert_must_list"),
    ],
    "f_map_and_filter_chain": "m_to_bool",
    "reduce_chain": "",
    "l_map_and_filter_chain": ""
}

company_addr_city_level_config = {
    "feature_name": "company_addr_city_level",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [
        ("address", "$..content.address", "f_assert_not_null->f_assert_must_basestring"),
    ],
    "f_map_and_filter_chain": "m_get_seq_index_value(0)->m_get_company_addr_city_name->f_assert_not_null->m_city_name_to_code",
    "reduce_chain": "",
    "l_map_and_filter_chain": ""
}

folk_config = {
    "feature_name": "folk",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [
        ("nation", "$..content.nation", "f_assert_not_null->f_assert_must_basestring"),
    ],
    "f_map_and_filter_chain": "m_get_seq_index_value(0)->m_check_x_in_y('汉')",
    "reduce_chain": "",
    "l_map_and_filter_chain": ""
}

marital_status_config = {
    "feature_name": "marital_status",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [
        ("marital_status", "$..content.marital_status", "f_assert_not_null->f_assert_must_digit"),
    ],
    "f_map_and_filter_chain": "m_get_seq_index_value(0)->m_marital_status_to_code",
    "reduce_chain": "",
    "l_map_and_filter_chain": ""
}

gender_config = {
    "feature_name": "gender",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [
        ("sex", "$..content.sex", "f_assert_not_null->f_assert_must_basestring"),
    ],
    "f_map_and_filter_chain": "m_get_seq_index_value(0)->m_sex_to_code",
    "reduce_chain": "",
    "l_map_and_filter_chain": ""
}

mobile_area_city_level_config = {
    "feature_name": "mobile_area_city_level",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [
        ("mobile_area", "$..content.mobile_area", "f_assert_not_null->f_assert_must_basestring"),
    ],
    "f_map_and_filter_chain": "m_get_seq_index_value(0)->m_city_name->f_assert_not_null->m_city_name_to_code",
    "reduce_chain": "",
    "l_map_and_filter_chain": ""
}

register_city_level_config = {
    "feature_name": "register_city_level",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [
        ("home_address", "$..content.home_address", "f_assert_not_null->f_assert_must_basestring"),
    ],
    "f_map_and_filter_chain": "m_get_seq_index_value(0)->m_city_name->f_assert_not_null->m_city_name_to_code",
    "reduce_chain": "",
    "l_map_and_filter_chain": ""
}

max_flight_area_config = {
    "feature_name": "max_flight_area",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [
        ("flight_times", "$..content.flight_times", "f_assert_not_null->f_assert_must_digit_or_float"),
        ("inland_count", "$..content.inland_count", "f_assert_not_null->f_assert_must_digit_or_float"),
        ("international_count", "$..content.international_count", "f_assert_not_null->f_assert_must_digit_or_float"),
    ],
    "f_map_and_filter_chain": "m_max_flight_area",
    "reduce_chain": "",
    "l_map_and_filter_chain": ""
}