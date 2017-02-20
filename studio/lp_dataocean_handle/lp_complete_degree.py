# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2013- DIGCREDIT, All Rights Reserved.
    -----------------------------------------------------------
    Author: Z.L
    Date:  2017/02/17
    Change Activity:
"""
from vendor.utils.defaults import UnsignedIntTypeDefault
import logging

logger = logging.getLogger('apps.common')


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        输入:
        接口名称：猎聘预授信接口
        字段名称：'complete_degree'  简历完成度 int

        计算逻辑: 从猎聘预授信接口提取简历完成度并输出,输出类型为int

        输出:
        特征名称: 'complete_degree'  简历完成度 int
        """

        result = {"complete_degree": UnsignedIntTypeDefault}
        try:
            base_data = self.data["complete_degree"]
            if str(base_data).isdigit():  # 检验简历完成度是否只由数字组成,是则转化为int类型
                base_data = int(base_data)
                result["complete_degree"] = base_data

        except Exception as e:
                logging.error(e.message)
        finally:
            return result

