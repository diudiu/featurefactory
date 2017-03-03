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
        logger.info('')
        self.feature_config = base_data['feature_conf']
        self.feature_list = self.feature_config.keys()
        self.feature_ret = {}
        self.error_list = []
        self.apply_id = base_data.get('apply_id', None)

    def get_feature_value(self):
        logger.info('feature list :\n%s' % self.feature_list)
        for feature_name in self.feature_list:
            logger.info('Get feature value, named %s' % feature_name)
            courier = Courier(feature_name, self.feature_config[feature_name], self.apply_id)
            ret = courier.get_feature()
            if ret:
                logger.info('Single feature value has been gotten, %s' % ret)
                self.feature_ret.update(ret)
            else:
                logger.error('Get single feature value field, result is None')
                self.error_list.append(courier.error_no)
