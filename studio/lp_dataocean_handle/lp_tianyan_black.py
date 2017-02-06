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
        网贷黑名单
        data_identity: net_black_a_s
        :return:
        """
        result = {
            'is_net_black': False
        }
        tip = self.data.get('result', None)
        if not tip:
            return result

        if self.data['result'] == u'00':
            result['is_net_black'] = True

        return result
