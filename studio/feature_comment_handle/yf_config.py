# -*- coding:utf-8 -*-
config = dict(
    mobile_activeness_config={
        "feature_name": "mobile_activeness",
        "feature_data_type": "float",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [
            ("tags", "$..tags", "f_assert_not_null->f_assert_must_dict"),
            ("mobile", "$..apply_data.data.mobile", "f_assert_not_null"),
        ],
        "f_map_and_filter_chain": "f_mobile_m1_m5_sum_max_seq(['contactAmount'])->m_seq_to_agv(2)",
        "reduce_chain": "",
        "l_map_and_filter_chain": ""
    },

    mobile_stability_config={
        "feature_name": "mobile_stability",
        "feature_data_type": "float",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [
            ("tags", "$..tags", "f_assert_not_null->f_assert_must_dict"),
            ("mobile", "$..apply_data.data.mobile", "f_assert_not_null"),
        ],
        "f_map_and_filter_chain": "f_mobile_m1_m5_sum_max_seq(['callTimes','calledTimes'])->m_get_mobile_stability",
        "reduce_chain": "",
        "l_map_and_filter_chain": ""
    },

    is_pingan_financial_shixin_config={
        "feature_name": "is_pingan_financial_shixin",
        "feature_data_type": "bool",
        "default_value": "BooleanTypeDefault",
        "json_path_list": [
            ("others", "$..others", "f_assert_jsonpath_true->f_assert_must_list"),
        ],
        "f_map_and_filter_chain": "m_to_bool",
        "reduce_chain": "",
        "l_map_and_filter_chain": ""
    },

    company_addr_city_level_config={
        "feature_name": "company_addr_city_level",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [
            ("address", "$..content.address", "f_assert_not_null->f_assert_must_basestring"),
        ],
        "f_map_and_filter_chain": "m_get_seq_index_value(0)->m_get_city_name->f_assert_not_null->m_city_name_to_level",
        "reduce_chain": "",
        "l_map_and_filter_chain": ""
    },

    folk_config={
        "feature_name": "folk",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [
            ("nation", "$..content.nation", "f_assert_not_null->f_assert_must_basestring"),
        ],
        "f_map_and_filter_chain": "m_get_seq_index_value(0)->m_check_x_in_y('汉')",
        "reduce_chain": "",
        "l_map_and_filter_chain": ""
    },

    home_address_config={
        "feature_name": "home_address",
        "feature_data_type": "string",
        "default_value": "StringTypeDefault",
        "json_path_list": [("nation", "$..content.home_address", "f_assert_not_null->f_assert_must_basestring")],
        "f_map_and_filter_chain": "",
        "reduce_chain": "",
        "l_map_and_filter_chain": ""
    },

    marital_status_config={
        "feature_name": "marital_status",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [
            ("marital_status", "$..content.marital_status", "f_assert_not_null->f_assert_must_digit"),
        ],
        "f_map_and_filter_chain": "m_get_seq_index_value(0)->m_marital_status->m_to_code('marital_status')",
        "reduce_chain": "",
        "l_map_and_filter_chain": ""
    },

    gender_config={
        "feature_name": "gender",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [
            ("sex", "$..content.sex", "f_assert_not_null->f_assert_must_basestring"),
        ],
        "f_map_and_filter_chain": "m_get_seq_index_value(0)->m_sex_to_code->m_to_code('gender')",
        "reduce_chain": "",
        "l_map_and_filter_chain": ""
    },

    mobile_area_city_level_config={
        "feature_name": "mobile_area_city_level",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [
            ("mobile_area", "$..content.mobile_area", "f_assert_not_null->f_assert_must_basestring"),
        ],
        "f_map_and_filter_chain": "m_get_seq_index_value(0)->m_get_city_name->f_assert_not_null->m_city_name_to_level",
        "reduce_chain": "",
        "l_map_and_filter_chain": ""
    },

    register_city_level_config={
        "feature_name": "register_city_level",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [
            ("home_address", "$..content.home_address", "f_assert_not_null->f_assert_must_basestring"),
        ],
        "f_map_and_filter_chain": "m_get_seq_index_value(0)->m_get_city_name->f_assert_not_null->m_city_name_to_level",
        "reduce_chain": "",
        "l_map_and_filter_chain": ""
    },

    max_flight_area_config={
        "feature_name": "max_flight_area",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [
            ("flight_times", "$..content.flight_times", "f_assert_not_null->f_assert_must_digit_or_float"),
            ("inland_count", "$..content.inland_count", "f_assert_not_null->f_assert_must_digit_or_float"),
            (
                "international_count", "$..content.international_count",
                "f_assert_not_null->f_assert_must_digit_or_float"),
        ],
        "f_map_and_filter_chain": "m_max_flight_area->f_assert_not_null->m_to_code('max_flight_area')",
        "reduce_chain": "",
        "l_map_and_filter_chain": ""
    },

    max_flight_class_config={
        "feature_name": "max_flight_class",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [
            ("business_class_count", "$..content.business_class_count", "f_assert_not_null->f_assert_must_digit"),
            ("executive_class_count", "$..content.executive_class_count", "f_assert_not_null->f_assert_must_digit"),
            ("tourist_class_count", "$..content.tourist_class_count", "f_assert_not_null->f_assert_must_digit"),
        ],
        "f_map_and_filter_chain": "m_to_int->m_max_flight_class->m_to_code('max_flight_class')",
        "reduce_chain": "",
        "l_map_and_filter_chain": ""
    },

    airfare_sum12_config={
        "feature_name": "airfare_sum12",
        "feature_data_type": "float",
        "default_value": "PositiveSignedFloatTypeDefault",
        "json_path_list": [
            ("average_price", "$..content.average_price", "f_assert_not_null->f_assert_must_digit_or_float"),
            ("flight_times", "$..content.flight_times", "f_assert_not_null->f_assert_must_digit"),
        ],
        "f_map_and_filter_chain": "m_str_to_int_float_in_list",
        "reduce_chain": "r_mul",
        "l_map_and_filter_chain": ""
    },

    contacts_config={
        "feature_name": "contacts",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [
            ("contacts", "$..contacts", "f_assert_not_null->f_assert_must_digit"),
        ],
        "f_map_and_filter_chain": "m_to_int->m_get_seq_index_value(0)",
        "reduce_chain": "",
        "l_map_and_filter_chain": ""
    },

    is_jiuyao_multi_loan_config={
        "feature_name": "is_jiuyao_multi_loan",
        "feature_data_type": "bool",
        "default_value": "BooleanTypeDefault",
        "json_path_list": [
            ("loanInfos", "$..loanInfos", "f_assert_jsonpath_true->f_assert_must_list"),
        ],
        "f_map_and_filter_chain": "m_to_bool",
        "reduce_chain": "",
        "l_map_and_filter_chain": ""
    },

    loan_infos_config={
        "feature_name": "loan_infos",
        "feature_data_type": "list",
        "default_value": "ListTypeDefault",
        "json_path_list": [
            ("loanInfos", "$..loanInfos", "f_assert_not_null->f_assert_must_list"),
        ],
        "f_map_and_filter_chain": "",
        "reduce_chain": "",
        "l_map_and_filter_chain": ""
    },

    is_mobile_black_config={
        "feature_name": "is_mobile_black",
        "feature_data_type": "bool",
        "default_value": "BooleanTypeDefault",
        "json_path_list": [
            ("grayscale", "$..trustutn_loan_phone.data.grayscale", "f_assert_jsonpath_true->f_assert_must_dict"),
        ],
        "f_map_and_filter_chain": "m_get_seq_index_value(0)->m_to_bool",
        "reduce_chain": "",
        "l_map_and_filter_chain": ""
    },

    education_tz_config={
        "feature_name": "education_tz",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [
            ("edu_exp_form", "$..edu_exp_form[*]", "f_assert_not_null->f_assert_must_dict"),
        ],
        "f_map_and_filter_chain": "m_get_new_list('degree','tz')->m_seq_inx_to_int"
                                  "->m_seq_inx0_sort_in_list->m_get_seq_index_value(0)"
                                  "->m_get_seq_index_value(1)->f_assert_not_null",
        "reduce_chain": "",
        "l_map_and_filter_chain": ""
    },

    now_industry_code_config={
        "feature_name": "now_industry_code",
        "feature_data_type": "string",
        "default_value": "StringTypeDefault",
        "json_path_list": [
            ("work_exp_form", "$..work_exp_form[*]", "f_assert_not_null->f_assert_must_dict"),
        ],
        "f_map_and_filter_chain": "m_get_new_list('work_end','industry')->f_assert_not_null->m_now_industry_code",

        "reduce_chain": "",
        "l_map_and_filter_chain": ""
    },

    last_industry_code_config={
        "feature_name": "last_industry_code",
        "feature_data_type": "string",
        "default_value": "StringTypeDefault",
        "json_path_list": [
            ("work_exp_form", "$..work_exp_form[*]", "f_assert_not_null->f_assert_must_dict"),

        ],
        "f_map_and_filter_chain": "m_get_new_list('work_end','industry')->f_assert_not_null->m_seq_inx_to_int"
                                  "->m_seq_inx0_sort_in_list(True)->m_get_seq_index_value(0)->m_get_seq_index_value(1)",
        "reduce_chain": "",
        "l_map_and_filter_chain": ""
    },
    now_work_time_config={
        "feature_name": "now_work_time",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [
            ("work_exp_form", "$..work_exp_form[*]", "f_assert_not_null->f_assert_must_dict"),

        ],
        "f_map_and_filter_chain": "m_get_new_list('work_end','work_start')->f_assert_not_null"
                                  "->m_seq_inx0_sort_in_list(True)->m_get_seq_index_value(0)->m_r_to_now_work_time",
        "reduce_chain": "",
        "l_map_and_filter_chain": ""
    },

    industry_change_count_config={
        "feature_name": "industry_change_count",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [
            ("industry", "$..work_exp_form[*].industry", "f_assert_not_null"),

        ],
        "f_map_and_filter_chain": "m_list_to_distinct->m_to_len(1)",
        "reduce_chain": "",
        "l_map_and_filter_chain": ""
    },

    jiuyao_multi_loan_denied_count_config={
        "feature_name": "jiuyao_multi_loan_denied_count",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [
            ("contract_date", "$..loanInfos[*].contractDate", ""),
        ],
        "f_map_and_filter_chain": "f_digit_or_float->f_days_greater_than_args(180)->f_assert_not_null",
        "reduce_chain": "m_to_len",
        "l_map_and_filter_chain": ""
    },

    jiuyao_multi_loan_m2_count_config={
        "feature_name": "jiuyao_multi_loan_m2_count",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [
            ("repay_state", "$..loanInfos[*].repayState", "f_assert_not_null->f_digit_or_float"),
        ],
        "f_map_and_filter_chain": "f_inside_stipulate_scope([3, 4, 5, 6, 7, 8])",
        "reduce_chain": "m_to_len",
        "l_map_and_filter_chain": ""
    },

    is_unclear_loan_config={
        "feature_name": "is_unclear_loan",
        "feature_data_type": "int",
        "default_value": "BooleanTypeDefault",
        "json_path_list": [
            ("is_unclear_loan", "$..res_data.is_unclear_loan", "f_assert_not_null->f_assert_must_digit"),
        ],
        "f_map_and_filter_chain": "m_to_int->m_get_seq_index_value(0)->m_to_bool",
        "reduce_chain": "",
        "l_map_and_filter_chain": "m_to_bool(1)"
    },

    mobile_area_city_code_config={
        "feature_name": "mobile_area_city_code",
        "feature_data_type": "string",
        "default_value": "StringTypeDefault",
        "json_path_list": [
            ("mobile_area", "$..content.mobile_area", "f_assert_not_null->f_assert_must_basestring"),
        ],
        "f_map_and_filter_chain": "m_get_seq_index_value(0)->m_get_city_name->f_assert_not_null->m_city_name_to_code",
        "reduce_chain": "",
        "l_map_and_filter_chain": ""
    },

    gps_city_code_config={
        "feature_name": "gps_city_code",
        "feature_data_type": "string",
        "default_value": "StringTypeDefault",
        "json_path_list": [
            ("mobile_area", "$..addressComponent.city", "f_assert_not_null->f_assert_must_basestring"),
        ],
        "f_map_and_filter_chain": "m_get_seq_index_value(0)->m_get_city_name->f_assert_not_null->m_city_name_to_code",
        "reduce_chain": "",
        "l_map_and_filter_chain": ""
    },

    cur_work_status_config={
        "feature_name": "cur_work_status",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [
            ("cur_work_status", "$..cur_work_status", "f_assert_not_null->f_assert_must_basestring"),
        ],
        "f_map_and_filter_chain": "m_get_seq_index_value(0)->m_to_code('cur_work_status')",
        "reduce_chain": "",
        "l_map_and_filter_chain": ""
    },

    now_workplace_code_config={
        "feature_name": "now_workplace_code",
        "feature_data_type": "string",
        "default_value": "StringTypeDefault",
        "json_path_list": [
            ("work_exp_form", "$..work_exp_form[*]", "f_assert_not_null->f_assert_must_dict"),
        ],
        "f_map_and_filter_chain": "m_get_new_list('work_end','dq')->f_assert_not_null"
                                  "->m_seq_inx0_sort_in_list(True)->m_get_seq_index_value(0)->m_get_seq_index_value(1)",

        "reduce_chain": "",
        "l_map_and_filter_chain": ""
    },

    work_time_config={
        "feature_name": "work_time",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [
            ("work_start", "$..work_exp_form[*].work_start", "f_assert_must_basestring"),
        ],
        "f_map_and_filter_chain": "f_not_null->f_assert_not_null->m_get_max_month_to_now",
        "reduce_chain": "",
        "l_map_and_filter_chain": ""
    },

    mobile_identity_config={
        "feature_name": "mobile_identity",
        "feature_data_type": "int",
        "default_value": "BooleanTypeDefault",
        "json_path_list": [
            ("mobile_identity", "$.unicom_mobile_identity_s.result", "m_mobile_id_judge"),
            ("mobile_identity", "$.yd_mobile_identity_s.result", "m_mobile_id_judge"),
            ("mobile_identity", "$.telecom_mobile_identity_s.result", "m_mobile_id_judge"),
        ],
        "f_map_and_filter_chain": "m_to_sum->m_to_bool",
        "reduce_chain": "",
        "l_map_and_filter_chain": ""
    },
    income_expense_comparison_config={
        "feature_name": "income_expense_comparison",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [
            ("debit", "$.unicom_finance_portrait_s.content.last12.debit", "m_get_income_expense_comparison('unicome')"),
            ("rrx_inc_12m", "$.cc_credit.result.rrx_inc_12m", "m_get_income_expense_comparison('cc_credit')"),
        ],
        "f_map_and_filter_chain": "f_not_null->f_assert_not_null->m_get_seq_index_value(0)"
                                  "->m_to_code('income_expense_comparison')",
        "reduce_chain": "",
        "l_map_and_filter_chain": ""
    },

    mobile_area_code_config={
        "feature_name": "mobile_area_code",
        "feature_data_type": "string",
        "default_value": "StringTypeDefault",
        "json_path_list": [
            ("mobile_area", "$..mobile_area", "f_assert_not_null->f_assert_must_basestring"),
        ],
        "f_map_and_filter_chain": "m_get_seq_index_value(0)",
        "reduce_chain": "",
        "l_map_and_filter_chain": ""
    },

)
