# -*- coding:utf-8 -*-

age_config = {
    "feature_name": "age",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [("age", "$..content.age", "f_assert_not_null->f_assert_must_digit_or_float")],
    "map_and_filter_chain": "",
    "reduce_chain": "",
    "operator_chain": 'value[0]'
}

apply_register_duration_config = {
    "feature_name": "apply_register_duration",
    "feature_data_type": "float",
    "default_value": "PositiveSignedFloatTypeDefault",
    "json_path_list": [
        ("application_on", "$.apply_data.application_on", "f_assert_not_null->f_assert_must_basestring"),
        ("registration_on", "$.portrait_data.registration_on", "f_assert_not_null->f_assert_must_basestring")
    ],
    "map_and_filter_chain": "map_to_slice(0,10)->map_string_to_datetime",
    "reduce_chain": "reduce_sub",
    "operator_chain": "value.days->value/30.0->round(value, 2)->#value>=0"
}

car_count_config = {
    "feature_name": "car_count",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [
        ("application_on", "$.result", "f_assert_must_list"),
    ],
    "map_and_filter_chain": "filter_not_null",
    "reduce_chain": "",
    "operator_chain": "len(value)"
}

car_number_config = {
    "feature_name": "car_number",
    "feature_data_type": "list",
    "default_value": "ListTypeDefault",
    "json_path_list": [
        ("license_no", "$..license_no", ""),
    ],
    "map_and_filter_chain": "filter_not_null",
    "reduce_chain": "",
    "operator_chain": ""
}

cur_company_config = {
    "feature_name": "cur_company",
    "feature_data_type": "string",
    "default_value": "StringTypeDefault",
    "json_path_list": [
        ("work_exp_form", "$..work_exp_form", "f_assert_must_list"),
    ],
    "map_and_filter_chain": "map_get_new_list(work_end,comp_name)",
    "reduce_chain": "",
    "operator_chain": "sorted(value, key=lambda x: x[0], reverse=True)[0][1]->#value != ''"
}
