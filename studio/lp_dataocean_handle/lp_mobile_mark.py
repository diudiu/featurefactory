# -*- coding:utf-8 -*-

"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: ZL
    Date:  2017/01/20
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
import logging
from vendor.utils.defaults import StringTypeDefault

logger = logging.getLogger('apps.common')


class Handle(object):
    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口名称：
        'tags': 电话标记
        字段名称：
        'label': 用户标注标签 str

        输出:
        特征名称:
        'mobile_mark': 用户标注标签 str
        """
        result = {'mobile_mark': StringTypeDefault}
        try:
            base_data = self.data.get("tags", {}).get("contactMain_IMSI1_IMEI1", {}).get("label", '')
            if base_data and isinstance(base_data, basestring):
                result['mobile_mark'] = base_data

        except Exception as e:
            logging.error(e.message)
        return result
