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
from studio.fecture_comment_handle.featrue_process import FeatureProcess

from vendor.utils.phone_operator_judge import PhoneOperator
from vendor.errors.contact_error import *
from vendor.utils.constant import cons

logger = logging.getLogger('apps.etl')


class Courier(object):

    def __init__(self, feature_name, feature_conf, apply_id):
        self.feature_conf = feature_conf
        self.feature_name = feature_name
        self.error_no = 0
        self.collect_type = ''
        self.apply_id = apply_id
        self.data_identity_list = []
        self.cache_base = CacheContext(self.apply_id)
        self.useful_data = {}
        self.is_relevance = False

    def get_feature(self):
        self.data_identity_list = self._get_di_from_conf(self.feature_conf)
        if self.collect_type == 'Courier':
            # 普通逻辑
            self.useful_data = self.get_general_data()

        elif len(self.data_identity_list) > 1 and self.collect_type == 'ShuntCourier':
            # 分流逻辑
            self.useful_data = self.get_shunt_data()

        elif self.collect_type == 'RelevanceCourier':
            # 依赖逻辑
            self.useful_data = self.get_relevance_data(self.data_identity_list[0])

        if not self.useful_data:
            # TODO 获取原始数据失败
            raise
        return self.data_analysis()

    def data_analysis(self):
        obj_string = cons.LP_BASE_HANDLE + cons.HANDLE_COMBINE \
                     + 'lp_' + self.feature_name + cons.HANDLE_COMBINE + cons.HANDLE_CLASS
        try:
            feature_obj = FeatureProcess(self.feature_name, self.useful_data)
            ret = feature_obj.run()
            if not ret:
                obj = import_string(obj_string)
                handler = obj(self.useful_data)
                logger.info('get handle --%s--' % obj_string)
                ret = handler.handle()
        except Exception as e:
            logger.error('%s \nhandle init error , massage is :\n %s' % (obj_string, e))
            raise HandleInitializeFailed

        logger.info('Handle completed, result is %s' % ret)
        if not ret:
            logger.error('handle work complete, nothing return: %s' % obj_string)
            raise HandleWorkError
        if self.feature_name not in ret.keys():
            # TODO 配置错误 返回的特征名和期待的不同
            raise
        return ret

    def get_useful_data(self, data_identity):
        dp = DataPrepare(data_identity, self.apply_id, self.feature_conf[data_identity])
        data = dp.get_original_data()
        return data

    def get_general_data(self):
        # 获取一般情况数据
        useful_data = {}
        for data_identity in self.data_identity_list:
            data = self.get_useful_data(data_identity)
            useful_data.update({
                data_identity: data
            })
        return useful_data

    def get_shunt_data(self):
        useful_data = {}
        data = self.get_shunt_rel_data()
        if not data:
            raise
        useful_data.update(data)
        return useful_data

    def get_shunt_rel_data(self):
        # 获取分流逻辑数据useful_data_identity = []
        feature_conf_list = FeatureShuntConf.objects.filter(
            feature_name=self.feature_name,
            is_delete=False
        ).order_by('id')
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
                    if not useful_data_identity:
                        raise
                    data = self.get_useful_data(data_identity)
                    if not data:
                        continue
                    return data

    def get_relevance_data(self, next_data_identity=None):
        # TODO 获取依赖逻辑数据
        useful_data = {}
        if next_data_identity:
            relevance_conf = FeatureRelevanceConf.objects.filter(
                data_identity=next_data_identity,
                is_delete=False
            )[0]
            if not relevance_conf:
                raise
            next_di = relevance_conf.depend_di
            if next_di:
                useful_data = self.get_relevance_data(next_di)
            else:
                data = self.get_useful_data(next_data_identity)
                useful_data.update({
                    next_data_identity: data
                })
        return useful_data

    def _get_di_from_conf(self, base_conf):
        data_identity_list = base_conf.keys()
        if 'collect_type' in data_identity_list:
            self.collect_type = base_conf['collect_type']
            data_identity_list.remove('collect_type')
        return data_identity_list
