# -*- coding:utf-8 -*-

"""
    License DIGCREDIT-L.
    Copyright (c) 2013- DIGCREDIT, All Rights Reserved.
    -----------------------------------------------------------
    Author: Z.L
    Date:  2017/02/17
    Change Activity:

    data = {
    "tags": {
        "contactMain_IMSI1_IMEI1":
            {
                "city": "上海市上海市",
                "label": "未被标记",
                "operator": "上海移动",
            },
    },
}
"""
from vendor.utils.defaults import StringTypeDefault
import logging

logger = logging.getLogger('apps.common')


class Handle(object):
    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        输入:
        接口名称：'tags': 电话标记
        字段名称：'label': 用户标注标签 str

        计算逻辑:从电话标记接口提取电话标记信息并输出,输出类型为string

        输出:
        特征名称: 'mobile_mark': 用户标注标签 str
        """
        result = {'mobile_mark': StringTypeDefault}

        try:
            base_data = self.data.get("tags", {}).get("contactMain_IMSI1_IMEI1", {}).get("label", '')
            if base_data and isinstance(base_data, basestring):  # 判断电话标记信息是否为非空字符串
                result['mobile_mark'] = base_data

        except Exception as e:
            logging.error(e.message)
        finally:
            return result
