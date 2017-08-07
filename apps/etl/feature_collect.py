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
import traceback
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
        self.feature_comment_type = {}
        self.feature_excomment_type = self.feature_config.copy()
        self.apply_id = base_data.get('apply_id', None)
        self.cache_base = CacheContext(self.apply_id)

    def delete_async_cache(self):
        for data_identity in self.cache_base.smembers_async():
            self.cache_base.delete_cache(data_identity)
        self.cache_base.delete_async()

    def get_feature_value(self):
        self.classify_feature()
        logger.info('Stream in feature_collect function name : get_feature_value\nFeature list :%s' %
                    self.feature_list)
        logger.info(self.feature_comment_type)
        # feature_list = tuple(self.feature_list)
        # 通用特征计算
        for data_identity, apiconfig_feature in self.feature_comment_type.iteritems():
            logger.info("*******get_comment_type*******")
            logger.info(data_identity, apiconfig_feature)
            try:
                logger.info('Get feature from data_identity:%s' % data_identity)
                courier = Courier(feature_name='',
                                  feature_conf={},
                                  data_identity=data_identity,
                                  data_identity_config=apiconfig_feature,
                                  apply_id=self.apply_id,
                                  classify_collect_type=cons.COMMON_TYPE
                                  )
                ret = courier.get_feature()
                if ret:
                    self.feature_ret.update(ret)
                    [self.feature_list.remove(feature_name) for feature_name in ret]

            except DoingAsyncCallInterface:
                logger.info("data_identity:%s doing asynchronous call" % data_identity)
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
                raise e

        # 分流和依赖特征计算
        for feature_name in self.feature_excomment_type:
            logger.info("*******get_excomment_type*******")
            try:
                logger.info('Get feature:%s value' % feature_name)
                courier = Courier(feature_name=feature_name,
                                  feature_conf=self.feature_config[feature_name],
                                  data_identity='',
                                  data_identity_config='',
                                  apply_id=self.apply_id,
                                  classify_collect_type=cons.SHUNT_TYPE+"_" + cons.RELEVANCE
                                  )

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
                raise e

        if self.feature_list:
            time.sleep(10)
            self.get_feature_value()

    def classify_feature(self):
        feature_dict = {}
        for feature_name, f_config in self.feature_config.iteritems():
            collect_type = f_config.get("collect_type")
            val_keys = f_config.keys()
            if collect_type == cons.COMMON_TYPE and len(val_keys)-1 == 1:

                if val_keys[0] == "collect_type":
                    data_identity = val_keys[1]
                else:
                    data_identity = val_keys[0]
                if data_identity not in feature_dict:
                    feature_dict.update(
                        {
                            data_identity: {
                                "args": f_config,
                                "feature_list": [feature_name]
                            }
                        }
                    )
                else:
                    feature_dict[data_identity]["feature_list"].append(feature_name)

                del self.feature_excomment_type[feature_name]

        self.feature_comment_type = feature_dict
