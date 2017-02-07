# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: Sun Fei
    Date:  2017/1/18
    Change Activity:
"""


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):
        """
        接口名称：猎聘
        字段名称：work_exp_form    工作信息
                  cur_status       当前工作状态

        输出：
        特征名称：cur_work_status  当前工作状态
        """

        result = {'cur_work_status': 9999}  # 9999：异常

        # TODO 计算维度
        cur_work_status = self.data.get('cur_status', None)
        if cur_work_status == '在职，看看新机会':
            result['cur_work_status'] = 0
        elif cur_work_status == '离职，正在找工作':
            result['cur_work_status'] = 1
        elif cur_work_status == '在职，急寻新工作':
            result['cur_work_status'] = 2
        elif cur_work_status == '在职，暂无跳槽打算':
            result['cur_work_status'] = 3

        return result
