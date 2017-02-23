# -*- coding:utf-8 -*-

age_config = {
    "feature_name": "age",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [("age", "$..content.age", "f_assert_not_null->f_assert_must_digit")],
    "map_and_filter_chain": "",
    "reduce_chain": "reduce_singo_value"
}
