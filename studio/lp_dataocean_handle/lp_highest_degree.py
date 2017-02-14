# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2017- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.G
    Date: 2017/02/10
    Change Activity:
"""


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口：猎聘预授信接口
        输出:简历最高学历
        """

        result = {"highest_degree": 9999}

        try:
            edu_exp_form = self.data['edu_exp_form']
            degree_list = []
            for a in range(len(edu_exp_form)):
                degree_list.append(edu_exp_form[a].get('degree'))
            if "5" in degree_list:
                highest_degree = "5"
            elif "10" in degree_list:
                highest_degree = "10"
            elif "20" in degree_list:
                highest_degree = "20"
            elif "30" in degree_list:
                highest_degree = "30"
            elif "40" in degree_list:
                highest_degree = "40"
            elif "50" in degree_list:
                highest_degree = "50"
            elif "60" in degree_list:
                highest_degree = "60"
            elif "70" in degree_list:
                highest_degree = "70"
            elif "80" in degree_list:
                highest_degree = "80"
            elif "90" in degree_list:
                highest_degree = "90"
            else:
                highest_degree = "999"
            result['highest_degree'] = highest_degree
        except Exception:
            # TODO log this error
            return result

        return result



