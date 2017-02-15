# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: LJY
    Date:  2017/02/08
    Change Activity:

    data = {
        "status": 1,
        "message": "操作成功",
        "res_data": {
            "is_unclear_loan": 0,
        },
    }
"""
import logging

logger = logging.getLogger('apps.common')


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口名称：猎聘金融
        字段名称：


        输出:
        特征名称: 是否有未结清贷款
        字段名称:
        'is_unclear_loan': 是否有未结清贷款
        """
        try:
            result = {
                "is_unclear_loan": 9999,
            }
            base_data = self.data.get("res_data", {}).get("is_unclear_loan", '')
            if str(base_data).isdigit():
                result['is_unclear_loan'] = base_data
        except Exception as e:
            logging.info(e.message)
        return result
