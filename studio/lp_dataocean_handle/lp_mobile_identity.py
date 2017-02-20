# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2017- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.G
    Date: 2017/02/10
    Change Activity:
"""
from vendor.utils.defaults import BooleanTypeDefault
import logging


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):
        if 'telecom_mobile_identity_s' in self.data.keys():
            self.data = self.data['telecom_mobile_identity_s']
            return self._telecom_handle()
        if 'yd_mobile_identity_s' in self.data.keys():
            self.data = self.data['yd_mobile_identity_s']
            return self._yd_handle()
        if 'unicom_mobile_identity_s' in self.data.keys():
            self.data = self.data['unicom_mobile_identity_s']
            return self._unicome_handle()

    def _telecom_handle(self):
        """
            接口名称：电信号码三元素认证
            字段名称：result          返回结果

            输出：
            特征名称：mobile_identity 电信查询返回结果
            """
        mobile_identity_dic = {'mobile_identity': BooleanTypeDefault}
        try:
            mobile_identity = self.data.get('result', None)
            if mobile_identity == '00':
                mobile_identity_dic['mobile_identity'] = 1
            else:
                mobile_identity_dic['mobile_identity'] = 0

        except Exception as e:
            logging.error(e.message)
        return mobile_identity_dic

    def _yd_handle(self):
        """
            接口名称：移动号码三元素认证
            字段名称：result            返回结果

            输出：
            特征名称：mobile_identity   移动查询返回结果
            """
        mobile_identity_dic = {'mobile_identity': BooleanTypeDefault}
        try:
            mobile_identity = self.data['result']
            if mobile_identity == '00':
                mobile_identity_dic['mobile_identity'] = 1
            else:
                mobile_identity_dic['mobile_identity'] = 0
        except Exception as e:
            logging.error(e.message)
        return mobile_identity_dic

    def _unicome_handle(self):
        """
            接口名称：联通号码三元素认证
            字段名称：result          返回结果

            输出：
            特征名称：mobile_identity 联通查询返回结果
            """
        mobile_identity_dic = {'mobile_identity': BooleanTypeDefault}
        try:
            mobile_identity = self.data['result']
            if mobile_identity == '00':
                mobile_identity_dic['mobile_identity'] = 1
            else:
                mobile_identity_dic['mobile_identity'] = 0
        except Exception as e:
            logging.error(e.message)
        return mobile_identity_dic
