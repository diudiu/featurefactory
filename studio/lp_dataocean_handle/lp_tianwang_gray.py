# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.Junpeng
    Date:  2017/01/20
    Change Activity:
"""
# TODO


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):
        """
        天网灰名单
        data_identity: tianwang_gray
        :return:
        """
        result = {
            'is_netsky_gray': False
        }
        tip = self.data.get('result', None)
        if not tip:
            return result

        if self.data['result'] == u'00':
            result['is_netsky_gray'] = True

        return result
