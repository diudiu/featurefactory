# -*- coding: utf-8 -*-

pingan_overdue_count_config = {
    "feature_name": "pingan_overdue_count",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [("recordNums", "$..recordNums", "f_not_null->f_digit_or_float")],
    "f_map_and_filter_chain": "m_to_sum",
    "reduce_chain": "",
    "l_map_and_filter_chain": "",
}


pingan_max_overdue_days_config = {
    "feature_name": "pingan_max_overdue_days",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [("longestDays", "$..longestDays", "f_not_null")],
    "f_map_and_filter_chain": "m_to_int->m_to_sum",
    "reduce_chain": "",
    "l_map_and_filter_chain": "",
}


pingan_overdue_corp_count_config = {
    "feature_name": "pingan_overdue_corp_count",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [("orgNums", "$..orgNums", "f_not_null->f_digit_or_float")],
    "f_map_and_filter_chain": "m_to_sum",
    "reduce_chain": "",
    "l_map_and_filter_chain": "",
}


pingan_other_loan_count_config = {
    "feature_name": "pingan_other_loan_count",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [("orgNums", "$..orgNums", "f_not_null")],
    "f_map_and_filter_chain": "m_to_int->m_to_sum",
    "reduce_chain": "",
    "l_map_and_filter_chain": "",
}


is_pingan_overdue_loan_config = {
    "feature_name": "is_pingan_overdue_loan",
    "feature_data_type": "int",
    "default_value": "BooleanTypeDefault",
    "json_path_list": [("result", "$..result", "f_assert_not_null->f_digit_or_float")],
    "f_map_and_filter_chain": "m_to_bool(0)",
    "reduce_chain": "",
    "l_map_and_filter_chain": "",
}


is_pingan_other_loan_config = {
    "feature_name": "is_pingan_other_loan",
    "feature_data_type": "int",
    "default_value": "BooleanTypeDefault",
    "json_path_list": [("result", "$..result", "f_assert_not_null->f_digit_or_float")],
    "f_map_and_filter_chain": "m_to_bool(0)",
    "reduce_chain": "",
    "l_map_and_filter_chain": "",
}


pingan_overdue_loan_infos_config = {
    "feature_name": "pingan_overdue_loan_infos",
    "feature_data_type": "list",
    "default_value": "ListTypeDefault",
    "json_path_list": [("trustutn_loan_overdue", "$.trustutn_loan_overdue", "f_not_null")],
    "f_map_and_filter_chain": "m_del_invalid_value(1)",
    "reduce_chain": "",
    "l_map_and_filter_chain": "",
}


pingan_other_loan_infos_config = {
    "feature_name": "pingan_other_loan_infos",
    "feature_data_type": "list",
    "default_value": "ListTypeDefault",
    "json_path_list": [("trustutn_loan_otheragent", "$.trustutn_loan_otheragent", "f_not_null")],
    "f_map_and_filter_chain": "m_del_invalid_value(1)",
    "reduce_chain": "",
    "l_map_and_filter_chain": "",
}


cur_company_config = {
    "feature_name": "cur_company",
    "feature_data_type": "str",
    "default_value": "StringTypeDefault",
    "json_path_list": [("work_exp_form", "$..work_exp_form", "f_assert_not_null->f_assert_must_list")],
    "f_map_and_filter_chain": "m_get_new_list('work_end','comp_name')->m_seq_inx0_sort_in_list(True)->m_get_seq_index_value(0)->m_get_seq_index_value(1)->f_assert_not_null",
    "reduce_chain": "",
    "l_map_and_filter_chain": "",
}


cur_corp_years_config = {
    "feature_name": "cur_corp_years",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [("start_business_date", "$..start_business_date", "f_assert_not_null")],
    "f_map_and_filter_chain": "m_get_seq_index_value(0)->m_get_date_to_now_years(2)->m_check_code()",
    "reduce_chain": "",
    "l_map_and_filter_chain": "",
}


cur_employee_number_config = {
    "feature_name": "cur_employee_number",
    "feature_data_type": "int",
    "default_value": "PositiveSignedTypeDefault",
    "json_path_list": [("staff_count", "$..staff_count", "f_assert_not_null")],
    "f_map_and_filter_chain": "m_get_seq_index_value(0)->m_to_int->m_check_code()",
    "reduce_chain": "",
    "l_map_and_filter_chain": "",
}


is_cur_corp_shixin_config = {
    "feature_name": "is_cur_corp_shixin",
    "feature_data_type": "int",
    "default_value": "BooleanTypeDefault",
    "json_path_list": [("result", "$..result", "f_assert_not_null")],
    "f_map_and_filter_chain": "m_to_bool('00')",
    "reduce_chain": "",
    "l_map_and_filter_chain": "",
}




name_config = {
    "feature_name": "name",
    "feature_data_type": "string",
    "default_value": "StringTypeDefault",
    "json_path_list": [("name", "$..apply_data.name","f_assert_not_null")],
    "f_map_and_filter_chain": "",
    "reduce_chain": "",
    "l_map_and_filter_chain": "",
}


card_id_config = {
    "feature_name": "card_id",
    "feature_data_type": "string",
    "default_value": "StringTypeDefault",
    "json_path_list": [("card_id", "$..card_id", "f_assert_not_null")],
    "f_map_and_filter_chain": "",
    "reduce_chain": "",
    "l_map_and_filter_chain": "",
}


mobile_config = {
    "feature_name": "mobile",
    "feature_data_type": "string",
    "default_value": "StringTypeDefault",
    "json_path_list": [("mobile", "$..mobile", "f_assert_not_null")],
    "f_map_and_filter_chain": "",
    "reduce_chain": "",
    "l_map_and_filter_chain": "",
}


