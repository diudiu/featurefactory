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
from vendor.utils.defaults import PositiveSignedTypeDefault
import logging
logger = logging.getLogger('apps.common')


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):
        """
        接口名称：猎聘
        字段名称： work_exp_form   工作信息
                  work_start      工作经历开始时间

        输出：
        特征名称： work_time       工作时间
        """
        work_time_dic = {'work_time': PositiveSignedTypeDefault}
        try:
            work_exp_form = self.data['work_exp_form']
            assert type(work_exp_form) == list
            work_start_list = []
            for work_exp in work_exp_form:
                work_start = work_exp.get('work_start', None)
                if not isinstance(work_start, (basestring, int)):
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
        except Exception as e:
                logging.error(e.message)
        return work_time_dic
