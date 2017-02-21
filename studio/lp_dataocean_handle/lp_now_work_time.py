# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: Sun Fei
    Date:  2017/1/19
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
        字段名称：work_exp_form       工作信息
                  work_start          工作经历开始时间
                  work_end            工作经历结束时间

        输出：
        特征名称：now_work_time       本份工作工作时间
        """
        now_work_time_dic = {'now_work_time': PositiveSignedTypeDefault}
        try:
            work_exp_form = self.data['work_exp_form']
            # TODO 计算维度
            # 计算最近一份工作的结束时间
            work_end_list = []
            for work_exp in work_exp_form:
                work_end = work_exp.get('work_end', None)
                if isinstance(work_end, (str, int)):
                    work_end_list.append(int(work_end))
            cur_status = self.data.get('cur_status', '9999')
            if '离职' in cur_status:
                now_work_start_str = work_exp_form[
                    np.argmax(work_end_list)].get('work_start', None)
                now_work_start = datetime.strptime(now_work_start_str, '%Y%m')
                now_work_end_str = work_exp_form[
                    np.argmax(work_end_list)].get('work_end', None)
                now_work_end = datetime.strptime(now_work_end_str, '%Y%m')
                now_work_time = now_work_end - now_work_start
                now_work_time_dic['now_work_time'] = now_work_time.days / 30

            elif '在职' in cur_status:
                now_work_start_str = work_exp_form[
                    np.argmax(work_end_list)].get('work_start', None)
                now_work_start = datetime.strptime(now_work_start_str, '%Y%m')
                now_work_time = datetime.now() - now_work_start
                now_work_time_dic['now_work_time'] = now_work_time.days / 30

        except Exception as e:
            logging.error(e.message)
        return now_work_time_dic
