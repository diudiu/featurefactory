# -*- coding:utf-8 -*-
"""
    Copyright (c) 2013-2016 SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/22
    Change Activity:

"""

import logging

from apps.etl.courier import Courier

logger = logging.getLogger("apps.etl")


class CollectFeature(object):

    def __init__(self, base_data):
        self.feature_config = base_data['feature_conf']
        self.feature_list = self.feature_config.keys()
        self.feature_ret = {}
        self.error_list = []
        self.apply_id = base_data.get('apply_id', None)

    def get_feature_value(self):
        for feature_name in self.feature_list:
            courier = Courier(feature_name, self.feature_config[feature_name], self.apply_id)
            ret = courier.get_feature()
            if ret:
                self.feature_ret.update(ret)
            else:
                self.error_list.append(courier.error_no)
