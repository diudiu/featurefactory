# -*- coding:utf-8 -*-

age_config = {
    "feature_name": "age",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [("age", "$..content.age", "f_assert_not_null->f_assert_must_digit_or_float")],
    "map_and_filter_chain": "",
    "reduce": "reduce_singo_value",
    "operator_chain": ''
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
    "reduce": "reduce_sub",
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
    "reduce": "",
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
    "reduce": "",
    "operator_chain": ""
}