# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: Sun Fei
    Date:  2017/1/18
    Change Activity:
"""

import numpy as np
from datetime import datetime


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):
        """
        接口名称：猎聘
        字段名称：work_exp_form   工作信息
                  work_start      工作经历开始时间

        输出：
        特征名称：work_time       工作时间
        """

        work_time_dic = {'work_time': 9999}  # 9999：异常

        try:
            work_exp_form = self.data['work_exp_form']
        except Exception:
            # TODO log this error
            return work_time_dic

        if not isinstance(work_exp_form, list):
            return work_time_dic

        # TODO 计算维度
        work_start_list = []
        for work_exp in work_exp_form:
            work_start = work_exp.get('work_start', None)
            if not isinstance(work_start, (str, int)):
                return work_time_dic
            else:
                work_start_list.append(int(work_start))

        # 计算第一份工作的起始时间
        work_start_str = work_exp_form[
            np.argmin(work_start_list)].get('work_start')
        work_start = datetime.strptime(work_start_str, '%Y%m')
        worktime = datetime.now() - work_start
        worktime_month = worktime.days / 30
        work_time_dic['work_time'] = worktime_month

        return work_time_dic
