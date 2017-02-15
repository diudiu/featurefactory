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
import logging

logger = logging.getLogger('apps.common')


class Handle(object):
    def __init__(self, data):
        self.data = data

    def handle(self):
        """
        接口名称：猎聘
        字段名称：work_exp_form       工作信息
                  work_end            工作经历结束时间
                  dq                  工作地点code

        输出：
        特征名称：now_workplace_code  现在工作地点code
        """

        # TODO 抽取DataOcean返回的源数据
        try:
            now_workplace_code_dic = {'now_workplace_code': 9999}  # 9999：异常
            work_exp_form = self.data['work_exp_form']
            # TODO 计算维度
            # 计算最近一份工作的工作地点
            work_end_list = []
            for work_exp in work_exp_form:
                work_end = work_exp.get('work_end', None)
                if not isinstance(work_end, (str, int)):
                    return now_workplace_code_dic
                else:
                    work_end_list.append(int(work_end))

            now_workplace_code = work_exp_form[
                np.argmax(work_end_list)].get('dq', None)
            if now_workplace_code[0:3] in ['010', '020', '030', '040', '320', '330', '340']:
                now_workplace_code = now_workplace_code[0:3]
            elif len(now_workplace_code) > 6:
                now_workplace_code = now_workplace_code[0:6]
            now_workplace_code_dic['now_workplace_code'] = now_workplace_code

        except Exception as e:
            logging.error(e.message)
        finally:
            return now_workplace_code_dic
