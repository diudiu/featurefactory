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

from apps.etl.context import CacheContext, ApplyContext
from apps.etl.models import FeatureShuntConf, FeatureRelevanceConf
from apps.remote.call import DataPrepare

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
        self.useful_data = {}
        self.is_relevance = False

    def get_feature(self):
        di_feature_conf = FeatureFieldRel.objects.filter(
            feature_name=self.feature_name,
            is_delete=False
        )
        if not di_feature_conf:
            raise
        self.data_identity_list = self._get_di_from_conf(di_feature_conf)
        if di_feature_conf[0].collect_type == 'Courier':
            # TODO 普通逻辑
            self.useful_data = self.get_general_data()

        elif di_feature_conf.count() > 1 and di_feature_conf[0].collect_type == 'ShuntCourier':
            # TODO 分流逻辑
            self.useful_data = self.get_shunt_data()

        elif di_feature_conf[0].collect_type == 'RelevanceCourier' and len(self.data_identity_list) == 1:
            # TODO 依赖逻辑
            self.useful_data = self.get_relevance_data(self.data_identity_list[0])

        if not self.useful_data:
            # TODO 获取原始数据失败
            raise
        return self.data_analysis()

    def data_analysis(self):
        obj_string = cons.LP_BASE_HANDLE + cons.HANDLE_COMBINE\
                     + 'lp_' + self.feature_name + cons.HANDLE_COMBINE + cons.HANDLE_CLASS
        try:
            obj = import_string(obj_string)
            handler = obj(self.useful_data)
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
            dp = DataPrepare(data_identity, self.apply_id)
            data = dp.get_original_data()
            useful_data.update({
                data_identity: data
            })
        return useful_data

    def get_shunt_data(self):
        useful_data = {}
        data_identity = self.get_shunt_di()
        if not data_identity:
            raise
        dp = DataPrepare(data_identity, self.apply_id)
        data = dp.get_original_data()
        useful_data.update(data)
        return useful_data

    def get_shunt_di(self):
        # TODO 获取分流逻辑数据useful_data_identity = []
        useful_data_identity = ''
        feature_conf_list = FeatureShuntConf.objects.filter(
            feature_name=self.feature_name,
            is_delete=False
        )
        if not feature_conf_list:
            raise
        apply_base = ApplyContext(self.apply_id)
        apply_data = (apply_base.load())['data']
        for feature_conf in feature_conf_list:
            shunt_key = feature_conf.shunt_key
            data_identity = feature_conf.data_identity
            value = apply_data.get(shunt_key, None)
            if not value:
                raise
            oper = feature_conf.shunt_type
            if oper == 'PhoneOperator':
                po = PhoneOperator(value)
                shunt = po.distinguish()
                if shunt in eval(feature_conf.shunt_value):
                    useful_data_identity = data_identity
        return useful_data_identity

    def get_relevance_data(self, next_data_identity=None):
        # TODO 获取依赖逻辑数据
        useful_data = {}
        if next_data_identity:
            relevance_conf = FeatureRelevanceConf.objects.filter(
                feature_name=self.feature_name,
                is_delete=False
            )
            if not relevance_conf:
                raise
            next_di = relevance_conf.data_identity
            if next_di:
                self.get_relevance_data(next_di)
            else:
                dp = DataPrepare(next_data_identity, self.apply_id)
                data = dp.get_original_data()
                useful_data.update({
                    next_data_identity: data
                })
        return useful_data

    @staticmethod
    def _get_di_from_conf(di_feature_conf):
        data_identity_list = []
        for conf in di_feature_conf:
            data_identity_list.append(conf.data_identity)
        return data_identity_list
