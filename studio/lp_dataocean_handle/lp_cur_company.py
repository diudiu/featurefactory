# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: S.G
    Date:  2017/2/17
    Change Activity:
"""

import logging
logger = logging.getLogger('apps.common')
from vendor.utils.defaults import StringTypeDefault

class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口：猎聘预授信

        字段：work_exp_form       工作信息
              comp_name           公司名称
              work_end            工作经历结束时间

        计算逻辑：如果不存在工作信息，返回异常；否则遍历work_exp_form的所有记录，get所有word_end（如果不存在word_end，返回异常）
                  并转化为整形组成work_end_list。取work_end_list中最大值对应的comp_name作为当前工作单位

        输出：cur_company    当前工作单位
        """

        result = {'cur_company': StringTypeDefault}
        work_end_list = []

        try:
            work_exp_form = self.data['work_exp_form']

            if not isinstance(work_exp_form, list):   # 如果不存在工作信息，返回异常
                pass
            for work_exp in work_exp_form:   # 遍历work_exp_form的所有记录
                work_end = work_exp.get('work_end', None)
                if not isinstance(work_end, (str, int)):   # 如果不存在word_end，返回异常
                    pass
                else:
                    work_end_list.append(int(work_end))   # get所有word_end并转化为整形组成work_end_list
            result['cur_company'] = work_exp_form[max(work_end_list)].get('comp_name', None)   # 取work_end_list中最大值对应的comp_name作为当前工作单位
        except Exception as e:
            logging.error(e.message)
        finally:
            return result