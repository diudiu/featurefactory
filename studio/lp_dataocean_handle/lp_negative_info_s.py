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
        个人不良信息
        data_identity: negative_info_s
        :return:
        """
        result = {
            'has_negative_info': False
        }
        tip = self.data.get('result', None)
        if not tip:
            return result

        if self.data['result'] == u'00':
            result['has_negative_info'] = True

        return result
