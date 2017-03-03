# -*- coding:utf-8 -*-


is_netsky_multi_loan_config = {
    "feature_name": "is_netsky_multi_loan",
    "feature_data_type": "int",
    "default_value": "BooleanTypeDefault",
    "json_path_list": [("is_netsky_multi_loan", "$.result", "f_assert_not_null->f_assert_must_basestring")],
    "f_map_and_filter_chain": "m_to_bool(['00'])",
    "reduce_chain": "",
    "l_map_and_filter_chain": ''
}

is_skyeye_black_config = {
    "feature_name": "is_skyeye_black",
    "feature_data_type": "int",
    "default_value": "BooleanTypeDefault",
    "json_path_list": [("is_skyeye_black", "$.result", "f_assert_not_null->f_assert_must_basestring")],
    "f_map_and_filter_chain": "m_to_bool(['00'])",
    "reduce_chain": "",
    "l_map_and_filter_chain": ''
}

is_court_shixin_config = {
    "feature_name": "is_court_shixin",
    "feature_data_type": "int",
    "default_value": "BooleanTypeDefault",
    "json_path_list": [("is_court_shixin", "$.result", "f_assert_not_null->f_assert_must_basestring")],
    "f_map_and_filter_chain": "m_to_bool(['00'])",
    "reduce_chain": "",
    "l_map_and_filter_chain": ''
}

is_net_black_config = {
    "feature_name": "is_net_black",
    "feature_data_type": "int",
    "default_value": "BooleanTypeDefault",
    "json_path_list": [("is_net_black", "$.result", "f_assert_not_null->f_assert_must_basestring")],
    "f_map_and_filter_chain": "m_to_bool(['00'])",
    "reduce_chain": "",
    "l_map_and_filter_chain": ''
}

has_negative_info_config = {
    "feature_name": "has_negative_info",
    "feature_data_type": "int",
    "default_value": "BooleanTypeDefault",
    "json_path_list": [("has_negative_infok", "$.result", "f_assert_not_null->f_assert_must_basestring")],
    "f_map_and_filter_chain": "m_to_bool(['00'])",
    "reduce_chain": "",
    "l_map_and_filter_chain": ''
}

has_negative_info_config = {
    "feature_name": "has_negative_info",
    "feature_data_type": "int",
    "default_value": "BooleanTypeDefault",
    "json_path_list": [("has_negative_infok", "$.result", "f_assert_not_null->f_assert_must_basestring")],
    "f_map_and_filter_chain": "m_to_bool(['00'])",
    "reduce_chain": "",
    "l_map_and_filter_chain": ''
}

is_netsky_grey_config = {
    "feature_name": "is_netsky_grey",
    "feature_data_type": "int",
    "default_value": "BooleanTypeDefault",
    "json_path_list": [("is_netsky_grey", "$.result", "f_assert_not_null->f_assert_must_basestring")],
    "f_map_and_filter_chain": "m_to_bool(['00'])",
    "reduce_chain": "",
    "l_map_and_filter_chain": ''
}

is_court_zhixing_config = {
    "feature_name": "is_court_zhixing",
    "feature_data_type": "int",
    "default_value": "BooleanTypeDefault",
    "json_path_list": [("is_court_zhixing", "$.result", "f_assert_not_null->f_assert_must_basestring")],
    "f_map_and_filter_chain": "m_to_bool(['00'])",
    "reduce_chain": "",
    "l_map_and_filter_chain": ''
}

is_recruitment_config = {
    "feature_name": "is_recruitment",
    "feature_data_type": "int",
    "default_value": "BooleanTypeDefault",
    "json_path_list": [("is_recruitment", "$..education_approach", "f_assert_not_null->f_assert_must_basestring")],
    "f_map_and_filter_chain": "m_to_bool(['普通全日制'])",
    "reduce_chain": "",
    "l_map_and_filter_chain": ''
}

graduate_college_config = {
    "feature_name": "graduate_college",
    "feature_data_type": "str",
    "default_value": "StringTypeDefault",
    "json_path_list": [("graduate_college", "$..school", "f_assert_not_null->f_assert_must_basestring")],
    "f_map_and_filter_chain": "",
    "reduce_chain": "",
    "l_map_and_filter_chain": ''
}

car_number_config = {
    "feature_name": "car_number",
    "feature_data_type": "list",
    "default_value": "ListTypeDefault",
    "json_path_list": [("license_no", "$..license_no", "f_assert_not_null->f_plate_number")],
    "f_map_and_filter_chain": "",
    "reduce_chain": "",
    "l_map_and_filter_chain": ""
}

college_type_config = {
    "feature_name": "college_type",
    "feature_data_type": "str",
    "default_value": "StringTypeDefault",
    "json_path_list": [("college_type", "$.content.college.school_nature", "f_assert_not_null->f_assert_must_basestring"),
                       ("college_type", "$.content.degree.degree", "f_assert_not_null->f_assert_must_basestring")],
    "f_map_and_filter_chain": "m_college_type",
    "reduce_chain": "",
    "l_map_and_filter_chain": ''
}

graduate_college_check_config = {
    "feature_name": "graduate_college_check",
    "feature_data_type": "str",
    "default_value": "StringTypeDefault",
    "json_path_list": [("college_type", "$.content.degree.college", "f_assert_not_null")],
    "f_map_and_filter_chain": "",
    "reduce_chain": "",
    "l_map_and_filter_chain": ''
}

education_degree_check_config = {
    "feature_name": "education_degree_check",
    "feature_data_type": "str",
    "default_value": "StringTypeDefault",
    "json_path_list": [("college_type", "$.content.degree.degree", "f_assert_not_null")],
    "f_map_and_filter_chain": "m_to_int",
    "reduce_chain": "",
    "l_map_and_filter_chain": ''
}

pingan_multi_loan_infos_config = {
    "feature_name": "pingan_multi_loan_infos",
    "feature_data_type": "str",
    "default_value": "StringTypeDefault",
    "json_path_list": [("pingan_multi_loan_infos", "$..classification", "f_assert_not_null")],
    "f_map_and_filter_chain": "m_del_invalid_value()",
    "reduce_chain": "",
    "l_map_and_filter_chain": ''
}
