# -*- coding:utf-8 -*-
"""
    Copyright (c) 2013-2016 SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/22
    Change Activity:

"""
import time
import logging

from apps.etl.context import CacheContext
from apps.etl.courier import Courier
from vendor.errors.contact_error import *
from vendor.utils.constant import cons

logger = logging.getLogger("apps.etl")


class CollectFeature(object):
    def __init__(self, base_data):
        logger.info('Init CollectFeature')
        self.feature_config = base_data['feature_conf']
        self.feature_list = self.feature_config.keys()
        self.feature_ret = {}
        self.error_list = []
        self.use_time = {}
        self.apply_id = base_data.get('apply_id', None)
        self.cache_base = CacheContext(self.apply_id)

    def delete_async_cache(self):
        for data_identity in self.cache_base.smembers_async():
            self.cache_base.delete_cache(data_identity)
        self.cache_base.delete_async()

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
                calling_interface = DoingAsyncCallInterface.data_identify
                self.use_time['%s:start_time' % calling_interface] = self.use_time.get(
                    '%s:start_time' % calling_interface, int(time.time()))
                self.use_time['%s:use_time' % calling_interface] = int(time.time()) - self.use_time[
                    '%s:start_time' % calling_interface]
                logger.info("feature call use_time:\n%s" % self.use_time)
                if self.use_time['%s:use_time' % calling_interface] > cons.ASYNC_CALL_OVERTIME:
                    self.delete_async_cache()
                    raise AsyncCallInterfaceTimeout
                continue
            except Exception as e:
                import traceback
                traceback.print_exc()
                self.delete_async_cache()
                raise Exception(e.message)

        if self.feature_list:
            time.sleep(10)
            self.get_feature_value()
