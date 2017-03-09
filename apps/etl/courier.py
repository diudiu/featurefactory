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
from studio.feature_comment_handle.featrue_process import FeatureProcess

from vendor.utils.phone_operator_judge import PhoneOperator
from vendor.errors.contact_error import *
from vendor.utils.constant import cons

logger = logging.getLogger('apps.etl')


class Courier(object):
    def __init__(self, feature_name, feature_conf, apply_id):
        logger.info('Init Courier')
        self.feature_conf = feature_conf
        self.feature_name = feature_name
        self.error_no = 0
        self.collect_type = ''
        self.apply_id = apply_id
        self.data_identity_list = []
        self.cache_base = CacheContext(self.apply_id)
        self.useful_data = {}
        self.is_relevance = False
        self.relevance_feature_list = [feature_name]

    def get_feature(self):
        logger.info('Stream in courier function name : get_feature\nFeature name :\n%s' %
                    self.feature_name)
        self.data_identity_list = self._get_di_from_conf(self.feature_conf)
        if self.collect_type == 'Courier':
            logger.info('Stream in courier function name : get_feature\ncollect_type is Courier')
            self.get_general_data()

        elif len(self.data_identity_list) > 1 and self.collect_type == 'ShuntCourier':
            logger.info('Stream in courier function name : get_feature\ncollect_type is ShuntCourier')
            self.get_shunt_data()

        elif self.collect_type == 'RelevanceCourier':
            logger.info('Stream in courier function name : get_feature\ncollect_type is RelevanceCourier')
            self.get_relevance_data(self.data_identity_list[0])

        if not self.useful_data:
            logger.error('Get feature value error : useful data is empty  feature_name is %s' % self.feature_name)
            raise FeatureProcessError
        return self.data_analysis(self.feature_name, self.useful_data)

    @staticmethod
    def data_analysis(feature_name, useful_data):
        obj_string = cons.LP_BASE_HANDLE + cons.HANDLE_COMBINE \
                     + 'lp_' + feature_name + cons.HANDLE_COMBINE + cons.HANDLE_CLASS
        try:
            feature_obj = FeatureProcess(feature_name, useful_data)
            ret = feature_obj.run()
            logger.info('New Feature process complete, value : %s' % ret)
            if not ret:
                obj = import_string(obj_string)
                handler = obj(useful_data)
                logger.info('get handle --%s--' % obj_string)
                ret = handler.handle()
                logger.info('No value with New Feature process, use the classic process, value : %s' % ret)
        except Exception as e:
            logger.error('%s \nhandle init error , massage is :\n %s' % (obj_string, e))
            raise HandleInitializeFailed

        logger.info('Handle completed, result is %s' % ret)
        if not ret:
            logger.error('handle work complete, nothing return: %s' % obj_string)
            raise HandleWorkError
        if feature_name not in ret.keys():
            logger.error(
                'Wrong config of the feature, not the expect feature_name, feature_name: %s' % feature_name)
            raise FeatureConfigError
        return ret

    def get_useful_data(self, data_identity):
        dp = DataPrepare(data_identity, self.apply_id, self.feature_conf[data_identity])
        data = dp.get_original_data()
        return data

    def get_general_data(self):
        logger.info('Stream in courier function name : get_general_data')
        # useful_data = {}
        for data_identity in self.data_identity_list:
            data = self.get_useful_data(data_identity)
            # useful_data.update({
            #     data_identity: data
            # })
            self.useful_data.update({
                data_identity: data
            })
        logger.info('Stream get_general_data complete\nUseful_data : %s' % self.useful_data)

    def get_shunt_data(self):
        logger.info('Stream in courier function name : get_shunt_data')
        # useful_data = {}
        data = self.get_shunt_rel_data()
        if not data:
            raise
        # useful_data.update(data)
        logger.info('Stream get_shunt_data complete\nUseful_data : %s' % data)
        self.useful_data.update(data)

    def get_shunt_rel_data(self):
        logger.info('Stream in courier function name : get_shunt_rel_data')
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
                    logger.info('Stream get_shunt_rel_data complete\nUseful_data : %s' % data)
                    return data

    def _get_relevance_feature_list(self, next_data_identity=None):

        # useful_data = {}
        if next_data_identity:
            relevance_conf = FeatureRelevanceConf.objects.filter(
                data_identity=next_data_identity,
                is_delete=False
            )[0]
            if not relevance_conf:
                raise
            next_di = relevance_conf.depend_di
            next_feature = relevance_conf.depend_feature
            if next_di:
                self.relevance_feature_list.append(next_feature)
                self.get_relevance_data(next_di)

    def get_relevance_data(self, data_identity):
        # TODO 获取依赖逻辑数据
        self._get_relevance_feature_list(data_identity)
        relevance_feature_list = self.relevance_feature_list.reverse()
        relevance_data_identity = self.data_identity_list.reverse()

        for feature_name, data_identity in zip(relevance_feature_list, relevance_data_identity):
            if feature_name != relevance_feature_list[-1]:
                data = self.get_useful_data(data_identity)
                feature_value = self.data_analysis(feature_name, data)

                self.useful_data.update({
                    feature_name: feature_value
                })

        # return useful_data

    def _get_di_from_conf(self, base_conf):
        logger.info('Stream in courier function name : _get_di_from_conf\nBase_conf :\n%s' %
                    base_conf)
        data_identity_list = base_conf.keys()
        if 'collect_type' in data_identity_list:
            self.collect_type = base_conf['collect_type']
            data_identity_list.remove('collect_type')
        logger.info('Data_identity_list : %s' % data_identity_list)
        return data_identity_list
