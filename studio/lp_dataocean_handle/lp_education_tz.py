# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: S,G
    Date:  2017/02/10
    Change Activity:
"""

import numpy as np

import logging

from vendor.utils.defaults import *

logger = logging.getLogger('apps.common')


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):
        """
        接口名称：猎聘
        字段名称：edu_exp_form      教育信息
                 degree            学历code
                 tz                统招code

        输出：
        特征名称：education_tz      学历类型
        """

        result = {'education_tz': PositiveSignedTypeDefault}

        try:
            edu_exp_form = self.data['edu_exp_form']
            degree_list = []
            for edu_exp in edu_exp_form:
                degree = edu_exp.get('degree', None)
                if str(degree).isdigit():
                    degree_list.append(int(degree))
            tz = edu_exp_form[np.argmin(degree_list)]['tz']
            if str(tz).isdigit():
                result['education_tz'] = edu_exp_form[np.argmin(degree_list)]['tz']
        except Exception as e:
            logging.error(e.message)

        return result
