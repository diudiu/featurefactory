# -*- coding:utf-8 -*-
"""
    Copyright (c) 2013-2016 SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/22
    Change Activity:

"""

import logging

from apps.etl.context import CacheContext
from apps.etl.courier import Courier
from vendor.errors.contact_error import *

logger = logging.getLogger("apps.etl")

n = 1000


class CollectFeature(object):

    def __init__(self, base_data):
        logger.info('Init CollectFeature')
        self.feature_config = base_data['feature_conf']
        self.feature_list = self.feature_config.keys()
        self.feature_ret = {}
        self.error_list = []
        self.apply_id = base_data.get('apply_id', None)
        self.counter = 0

    def get_feature_value(self):
        logger.info('Stream in feature_collect function name : get_feature_value\nFeature list :%s' %
                    self.feature_list)
        feature_list = tuple(self.feature_list)
        for feature_name in feature_list:
            try:
                logger.info('*******Get feature:%s value*******' % feature_name)
                courier = Courier(feature_name, self.feature_config[feature_name], self.apply_id)
                ret = courier.get_feature()
                if ret:
                    self.feature_ret.update(ret)
                    self.feature_list.remove(feature_name)
                else:
                    logger.error('Get single feature value field, result is None')
                    self.error_list.append(courier.error_no)
            except DoingAsyncCallInterface:
                logger.info("Feature:%s doing asynchronous call" % feature_name)
                continue
            except Exception as e:
                import traceback
                traceback.print_exc()
                cache_base = CacheContext(self.apply_id)
                logger.info(cache_base.smembers_async())
                for data_identity in cache_base.smembers_async():
                    cache_base.delete(data_identity)
                cache_base.delete_async()
                raise Exception(e.message)

        if self.feature_list:
            if self.counter > 100:
                raise AsyncCallInterfaceTimeout
            logger.info(" Get async feature value, feature_list:%s " % self.feature_list)
            self.get_feature_value()
            self.counter += 1
