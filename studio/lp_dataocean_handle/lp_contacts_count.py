# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: LJY
    Date:  2017/01/18
    Change Activity:
"""

class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口名称：个人基本信息查询
        字段名称：
        contacts 联系人数量

        输出:
        特征名称: 联系人数量
        字段名称:
        'contacts_count': 联系人数量
        """

        result = {
            'contacts_count': 999999,
        }
        try:
            base_data = self.data['contacts']
        except Exception as e:
            # TODO log this error
            return result
        if not base_data or not isinstance(base_data, int):
            return result

        result['contacts_count'] = base_data

        return result