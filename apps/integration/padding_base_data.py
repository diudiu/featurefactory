# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/3/10
    Change Activity:
"""
import xlrd
import pymongo


def read_file():
    data_base_list = []
    file_name = "pro_data.xlsx"
    file_handle = xlrd.open_workbook(file_name)
    sheet = file_handle.sheets()[0]
    title_list = sheet.row_values(0)

    for row_num in range(sheet.nrows):
        data = {
            "product_code": "",
            "proposer_id": "",
            "name": "",
            "card_id": "",
            "mobile": "",
            "email": "",
            "registration_on": "",
            "city_code": "",
            "city_name": "",
            "now_indust_code": "",
            "now_indust_name": "",
            "work_age": 0,
            "complete_degree": 0,
            "cur_work_status": "",
            "upload_contact": 0,
            "sns_friends_cnt": 0,
            "sns_sd_friend_cnt": 0,
            "sns_h_fans_cn": 0,
            'sns_skill_tag_list': [],
            'work_exp_form': [],
            'edu_exp_form': [],
        }
        sns_skill_tag_list = {
            "skill_tag": "",
            "certified_num": 0
        }
        work_exp_form = {
            "title": "",
            "has_certified": "",
            "certified_num": 0,
            "comp_name": "",
            "months": 0,
            "salary": 0,
            "work_start": "",
            "work_end": "",
            "industry": "",
            "industry_name": "",
            "dq": "",
            "dq_name": ""
        }
        edu_exp_form = {
            "school": "",
            "start": "",
            "end": "",
            "degree": "",
            "degree_name": "",
            "tz": 0
        }
        if row_num == 0:
            continue
        row = sheet.row_values(row_num)
        for i in range(len(title_list)):
            data_base = data
            skill_tag = sns_skill_tag_list
            work_form = work_exp_form
            edu_form = edu_exp_form

            base_key = data_base.keys()
            skill_key = skill_tag.keys()
            work_key = work_form.keys()
            edu_key = edu_form.keys()
            if not title_list[i]:
                continue
            if title_list[i] in base_key:
                data_base[title_list[i]] = row[i]
            if title_list[i] in skill_key:
                skill_tag[title_list[i]] = row[i]
            if title_list[i] in work_key:
                work_form[title_list[i]] = row[i]
            if title_list[i] in edu_key:
                edu_form[title_list[i]] = row[i]
        data_base['sns_skill_tag_list'].append(skill_tag)
        data_base['work_exp_form'].append(work_form)
        data_base['edu_exp_form'].append(edu_form)
        data_base_list.append(data_base)
    return data_base_list


if __name__ == "__main__":
    data_list = read_file()
    # num = 0
    # conn = pymongo.MongoClient('192.168.1.198', 27017)
    # coll = conn['feature_storage']['portrait_base']
    # for data in data_list:
    #     num += 1
    #     print num
    #     coll.insert_one(data)

    print "Completed"