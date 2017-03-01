# -*- coding:utf-8 -*-

jiuyao_multi_loan_denied_count_config = {
    "feature_name": "jiuyao_multi_loan_denied_count",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [
        ("contract_date", "$..loanInfos[*].contractDate", "f_assert_not_null"),
    ],
    "f_map_and_filter_chain": "f_digit_or_float",
    "reduce_chain": "",
    "l_map_and_filter_chain": ""
}
