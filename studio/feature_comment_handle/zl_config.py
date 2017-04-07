# -*- coding: utf-8 -*-
config = dict(
    age_config={
        "feature_name": "age",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [("age", "$..content.age", "f_assert_not_null->f_assert_must_digit_or_float")],
        "f_map_and_filter_chain": "m_get_seq_index_value(0)",
        "reduce_chain": "",
        "l_map_and_filter_chain": ''
    },

    apply_register_duration_config={
        "feature_name": "apply_register_duration",
        "feature_data_type": "float",
        "default_value": "PositiveSignedFloatTypeDefault",
        "json_path_list": [
            ("application_on", "$.apply_data.data.application_on", "f_assert_not_null->f_assert_must_basestring"),
            ("registration_on", "$.portrait_data.data.registration_on", "f_assert_not_null->f_assert_must_basestring")
        ],
        "f_map_and_filter_chain": "m_to_slice(0,10)->f_assert_seq0_gte_seq1->m_get_mon_sub(2)",
        "reduce_chain": "",
        "l_map_and_filter_chain": ''
    },

    application_on_config={
        "feature_name": "application_on",
        "feature_data_type": "string",
        "default_value": "StringTypeDefault",
        "json_path_list": [("application_on", "$..application_on", "f_assert_not_null->f_assert_must_basestring")],
        "f_map_and_filter_chain": "m_get_seq_index_value(0)",
        "reduce_chain": "",
        "l_map_and_filter_chain": "",
    },

    application_on_plus_config={
        "feature_name": "application_on_plus",
        "feature_data_type": "string",
        "default_value": "StringTypeDefault",
        "json_path_list": [("application_on", "$..application_on", "f_assert_not_null->f_assert_must_basestring")],
        "f_map_and_filter_chain": "m_get_seq_index_value(0)->m_datetime_only_hour_minute",
        "reduce_chain": "",
        "l_map_and_filter_chain": "",
    },

    car_count_config={
        "feature_name": "car_count",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [
            ("result", "$..result", "f_assert_jsonpath_true->f_assert_must_list"),
        ],
        "f_map_and_filter_chain": "f_not_null->m_to_len",
        "reduce_chain": "",
        "l_map_and_filter_chain": ""
    },

    cc_bill_age_config={
        "feature_name": "cc_bill_age",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [("cc_bill_age", "$..result.rrx_once_all.credit_card_account_age",
                            "f_assert_not_null->f_assert_must_digit")],
        "f_map_and_filter_chain": "m_get_seq_index_value(0)",
        "reduce_chain": "",
        "l_map_and_filter_chain": "",
    },

    complete_degree_config={
        "feature_name": "complete_degree",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [("complete_degree", "$..complete_degree", "f_assert_not_null->f_assert_must_int")],
        "f_map_and_filter_chain": "m_get_seq_index_value(0)",
        "reduce_chain": "",
        "l_map_and_filter_chain": "",
    },

    creditcard_count_config={
        "feature_name": "creditcard_count",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [
            ("creditcard_count", "$..result.rrx_once_all.credit_cards_num", "f_assert_not_null->f_assert_must_digit")],
        "f_map_and_filter_chain": "m_get_seq_index_value(0)",
        "reduce_chain": "",
        "l_map_and_filter_chain": "",
    },

    dc_bill_age_config={
        "feature_name": "dc_bill_age",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [
            ("dc_bill_age", "$..result.rrx_once_all.debit_card_account_age", "f_assert_not_null->f_assert_must_digit")],
        "f_map_and_filter_chain": "m_get_seq_index_value(0)",
        "reduce_chain": "",
        "l_map_and_filter_chain": "",
    },

    education_degree_code_config={
        "feature_name": "education_degree_code",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [("education_degree_code", "$..edu_exp_form[*].degree", "f_not_null->f_assert_must_digit")],
        "f_map_and_filter_chain": "m_to_int->r_min->m_to_str->m_to_code('education_degree_code')",
        "reduce_chain": "",
        "l_map_and_filter_chain": "",
    },

    is_loan_agency_config={
        "feature_name": "is_loan_agency",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [("is_loan_agency", "$..result", "f_assert_not_null->f_assert_must_basestring")],
        "f_map_and_filter_chain": "m_get_seq_index_value(0)->m_to_bool('00')",
        "reduce_chain": "",
        "l_map_and_filter_chain": "",
    },

    is_netsky_black_config={
        "feature_name": "is_netsky_black",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [
            ("is_netsky_black", "$..result", "f_assert_not_null->f_assert_must_basestring")],
        "f_map_and_filter_chain": "m_get_seq_index_value(0)->m_to_bool('00')",
        "reduce_chain": "",
        "l_map_and_filter_chain": "",
    },

    is_organization_g_black_config={
        "feature_name": "is_organization_g_black",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [("is_organization_g_black", "$..result", "f_assert_not_null->f_assert_must_basestring")],
        "f_map_and_filter_chain": "m_get_seq_index_value(0)->m_to_bool('00')",
        "reduce_chain": "",
        "l_map_and_filter_chain": "",
    },

    is_pingan_multi_loan_config={
        "feature_name": "is_pingan_multi_loan",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [("is_pingan_multi_loan", "$..result", "f_assert_not_null->f_assert_must_int")],
        "f_map_and_filter_chain": "m_get_seq_index_value(0)->m_to_bool(0)",
        "reduce_chain": "",
        "l_map_and_filter_chain": "",
    },

    mobile_mark_config={
        "feature_name": "mobile_mark",
        "feature_data_type": "string",
        "default_value": "StringTypeDefault",
        "json_path_list": [("mobile_mark", "$..tags.contactMain_IMSI1_IMEI1.label",
                            "f_assert_not_null->f_assert_must_basestring")],
        "f_map_and_filter_chain": "m_get_seq_index_value(0)",
        "reduce_chain": "",
        "l_map_and_filter_chain": "",
    },

    online_time_config={
        "feature_name": "online_time",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [
            ("online_time", "$.yd_mobile_online_time_s.content.online_time", "m_yd_online_time"),
            ("online_time", "$.unicome_mobile_online_time_s.content.online_time", "m_unicom_online_time"),
            ("online_time", "$.telecom_mobile_online_time_s.content.online_time", "m_telecom_online_time"),
        ],
        "f_map_and_filter_chain": "f_assert_not_null->m_to_sum",
        "reduce_chain": "",
        "l_map_and_filter_chain": "",
    },

    income_level_config={
        "feature_name": "income_level",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [
            ("portrait_data", "$.portrait_data.data.work_exp_form",
             "m_lp_income(0.56)->m_to_code('income_level')"),
            ("cc_credit", "$..debit_card_12m_passentry_amount",
             "m_to_code('income_level_yd')->m_single_to_list"),
            ("unicom_finance_portrait_s", "$..last12.debit.income_range",
             "m_to_code('income_level_lt')->m_single_to_list"),
        ],
        "f_map_and_filter_chain": "m_to_sum",
        "reduce_chain": "",
        "l_map_and_filter_chain": "",
    },

    pingan_multi_loan_count_config={
        "feature_name": "pingan_multi_loan_count",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [("pingan_multi_loan_count", "$..orgNums", "f_not_null->f_assert_must_digit")],
        "f_map_and_filter_chain": "m_to_int->m_to_sum",
        "reduce_chain": "",
        "l_map_and_filter_chain": "",
    },

    overspeed_count_config={
        "feature_name": "overspeed_count",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [("overspeed_count", "$..content.over_speed_list[*].month_times", "f_not_null->f_assert_not_null->f_assert_must_digit")],
        "f_map_and_filter_chain": "m_to_int->m_to_sum",
        "reduce_chain": "",
        "l_map_and_filter_chain": "",
    },

    overload_count_config={
        "feature_name": "overload_count",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [("overload_count", "$..content.over_load_list[*].month_times", "f_not_null->f_assert_not_null->f_assert_must_digit")],
        "f_map_and_filter_chain": "m_to_int->m_to_sum",
        "reduce_chain": "",
        "l_map_and_filter_chain": "",
    },
)
