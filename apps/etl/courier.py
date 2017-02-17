# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/26
    Change Activity:
"""
import logging
from django.utils.module_loading import import_string

from apps.etl.context import CacheContext
from apps.etl.models import FeatureShuntConf, FeatureRelevanceConf
from apps.remote.models import FeatureFieldRel
from apps.remote.call import call_interface

from vendor.utils.phone_operator_judge import PhoneOperator
from vendor.errors.contact_error import *
from vendor.utils.constant import cons

logger = logging.getLogger('apps.etl')


class Courier(object):

    def __init__(self, feature_name, apply_id):
        self.feature_name = feature_name
        self.error_no = 0
        self.apply_id = apply_id
        self.data_identity_list = []
        self.cache_base = CacheContext(self.apply_id)

    def get_feature(self):
        useful_data = {}
        di_feature_conf = FeatureFieldRel.objects.filter(
            feature_name=self.feature_name,
            is_delete=False
        )
        if not di_feature_conf:
            raise
        self.data_identity_list = self._get_di_from_conf(di_feature_conf)
        if di_feature_conf[0].collect_type == 'Courier':
            # TODO 普通逻辑
            useful_data = self.get_general_data()
            pass

        elif di_feature_conf.count() > 1 and di_feature_conf[0].collect_type == 'ShuntCourier':
            # TODO 分流逻辑
            useful_data = self.get_shunt_data()
            pass

        elif di_feature_conf[0].collect_type == 'RelevanceCourier':
            # TODO 依赖逻辑
            useful_data = self.get_relevance_data()
            pass

        if not useful_data:
            # TODO 获取原始数据失败
            raise

        obj_string = cons.LP_BASE_HANDLE + cons.HANDLE_COMBINE\
                     + 'lp_' + self.feature_name + cons.HANDLE_COMBINE + cons.HANDLE_CLASS
        try:
            obj = import_string(obj_string)
            handler = obj(useful_data)
        except Exception as e:
            logger.error('%s \nhandle init error , massage is :\n %s' % (obj_string, e))
            raise HandleInitializeFailed
        logger.info('get handle --%s--' % obj_string)
        ret = handler.handle()
        logger.info('Handle completed, result is %s' % ret)
        if not ret:
            logger.error('handle work complete, nothing return: %s' % obj_string)
            raise HandleWorkError
        if self.feature_name not in ret.keys():
            # TODO 配置错误 返回的特征名和期待的不同
            raise
        return ret

    def get_general_data(self):
        # TODO 获取一般情况数据
        useful_data = {}
        for data_identity in self.data_identity_list:
            data = call_interface(data_identity)
            useful_data.update({
                data_identity: data
            })
        return useful_data

    def get_shunt_data(self):
        # TODO 获取分流逻辑数据
        return {}

    def get_relevance_data(self):
        # TODO 获取依赖逻辑数据
        return {}

    @staticmethod
    def _get_di_from_conf(di_feature_conf):
        data_identity_list = []
        for conf in di_feature_conf:
            data_identity_list.append(conf.data_identity)
        return data_identity_list
