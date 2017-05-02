# -*- coding: utf-8 -*-

config = dict(
    age_config={
        "feature_name": "age",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [("age", "$..content.age", "f_assert_not_null->f_assert_must_digit_or_float")],
        "f_map_and_filter_chain": "m_get_seq_index_value(0)",
        "reduce_chain": "",
        "l_map_and_filter_chain": ""
    },
        
    apply_register_duration_config={
        "feature_name": "apply_register_duration",
        "feature_data_type": "float",
        "default_value": "PositiveSignedFloatTypeDefault",
        "json_path_list": [
            ("application_on", "$.apply_data.data.application_on", "f_assert_not_null->f_assert_must_basestring"),
            ("registration_on", "$.portrait_data.data.registration_on", "f_assert_not_null->f_assert_must_basestring")
        ],
        "f_map_and_filter_chain": "m_to_slice(0,10)->f_assert_seq0_gte_seq1->m_get_mon_sub(2)->m_to_int",
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
        "f_map_and_filter_chain": "m_get_seq_index_value(0)->m_sex_to_code",
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
        "f_map_and_filter_chain": "m_get_seq_index_value(0)->m_get_city_name->f_assert_not_null->m_city_name_to_level2_0",
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
        
    mobile_area_city_level_config={
        "feature_name": "mobile_area_city_level",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [
            ("mobile_area", "$..content.mobile_area", "f_assert_not_null->f_assert_must_basestring"),
        ],
        "f_map_and_filter_chain": "m_get_seq_index_value(0)->m_get_city_name->f_assert_not_null->m_city_name_to_level2_0",
        "reduce_chain": "",
        "l_map_and_filter_chain": ""
    },
        
    online_time_config={
        "feature_name": "online_time",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [
            ("online_time", "$.yd_mobile_online_time_s.content.online_time", "m_yd_online_time2_0"),
            ("online_time", "$.unicome_mobile_online_time_s.content.online_time", "m_unicom_online_time2_0"),
            ("online_time", "$.telecom_mobile_online_time_s.content.online_time", "m_telecom_online_time2_0"),
        ],
        "f_map_and_filter_chain": "f_assert_not_null->m_get_seq_index_value(0)",
        "reduce_chain": "",
        "l_map_and_filter_chain": "",
    },
        
    college_type_config={
        "feature_name": "college_type",
        "feature_data_type": "string",
        "default_value": "StringTypeDefault",
        "json_path_list": [
            ("school_nature", "$..content.college.school_nature", "f_assert_not_null->f_assert_must_basestring"),
            ("degree", "$..content.degree.degree", "f_assert_not_null->f_assert_must_basestring")],
        "f_map_and_filter_chain": "m_college_type->m_to_code('college_type')",
        "reduce_chain": "",
        "l_map_and_filter_chain": ''
    },
        
    cur_employee_number_config={
        "feature_name": "cur_employee_number",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [("staff_count", "$..staff_count", "f_assert_not_null")],
        "f_map_and_filter_chain": "m_get_seq_index_value(0)->m_to_int",
        "reduce_chain": "",
        "l_map_and_filter_chain": "",
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
        
    company_addr_city_level_config={
        "feature_name": "company_addr_city_level",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [
            ("address", "$..content.address", "f_assert_not_null->f_assert_must_basestring"),
        ],
        "f_map_and_filter_chain": "m_get_seq_index_value(0)->m_get_city_name->f_assert_not_null->m_city_name_to_level2_0",
        "reduce_chain": "",
        "l_map_and_filter_chain": ""
    },
        
    is_cur_corp_shixin_config={
        "feature_name": "is_cur_corp_shixin",
        "feature_data_type": "int",
        "default_value": "BooleanTypeDefault",
        "json_path_list": [("result", "$..result", "f_assert_not_null")],
        "f_map_and_filter_chain": "m_get_seq_index_value(0)->m_to_bool2_0('00')",
        "reduce_chain": "",
        "l_map_and_filter_chain": "",
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
        "l_map_and_filter_chain": "m_industry_code_to_str"
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
        "l_map_and_filter_chain": "m_industry_code_to_str"
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
        
    is_recruitment_config={
        "feature_name": "is_recruitment",
        "feature_data_type": "int",
        "default_value": "BooleanTypeDefault",
        "json_path_list": [
            ("education_approach", "$..education_approach", "f_assert_not_null->f_assert_must_basestring")],
        "f_map_and_filter_chain": "m_get_seq_index_value(0)->m_to_recruitment",
        "reduce_chain": "",
        "l_map_and_filter_chain": ''
    },
        
    folk_config={
        "feature_name": "folk",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [
            ("nation", "$..content.nation", "f_assert_not_null->f_assert_must_basestring"),
        ],
        "f_map_and_filter_chain": "m_get_seq_index_value(0)->m_folk_x_in_y('汉')",
        "reduce_chain": "",
        "l_map_and_filter_chain": ""
    },
        
    graduate_college_config={
        "feature_name": "graduate_college",
        "feature_data_type": "string",
        "default_value": "StringTypeDefault",
        "json_path_list": [("school", "$..school", "f_assert_not_null->f_assert_must_basestring")],
        "f_map_and_filter_chain": "m_get_seq_index_value(0)",
        "reduce_chain": "",
        "l_map_and_filter_chain": 'm_code_to_collage_type'
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
        
    mobile_identity_config={
        "feature_name": "mobile_identity",
        "feature_data_type": "int",
        "default_value": "BooleanTypeDefault",
        "json_path_list": [
            ("mobile_identity", "$.unicom_mobile_identity_s.result", "m_mobile_id_judge"),
            ("mobile_identity", "$.yd_mobile_identity_s.result", "m_mobile_id_judge"),
            ("mobile_identity", "$.telecom_mobile_identity_s.result", "m_mobile_id_judge"),
        ],
        "f_map_and_filter_chain": "m_to_sum->m_to_bool2_0",
        "reduce_chain": "",
        "l_map_and_filter_chain": ""
    },
        
    cur_corp_years_config={
        "feature_name": "cur_corp_years",
        "feature_data_type": "int",
        "default_value": "PositiveSignedTypeDefault",
        "json_path_list": [("start_business_date", "$..start_business_date", "f_assert_not_null")],
        "f_map_and_filter_chain": "m_get_seq_index_value(0)->m_get_date_to_now_years(0)",
        "reduce_chain": "",
        "l_map_and_filter_chain": "",
    },
        
    education_degree_check_config={
        "feature_name": "education_degree_check",
        "feature_data_type": "string",
        "default_value": "StringTypeDefault",
        "json_path_list": [("degree", "$..content.degree.degree", "f_assert_not_null")],
        "f_map_and_filter_chain": "m_get_seq_index_value(0)->m_to_code('education_degree_check')",
        "reduce_chain": "",
        "l_map_and_filter_chain": ''
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
)
