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

from apps.etl.context import CacheContext, ApplyContext, ArgsContext
from apps.etl.models import FeatureShuntConf, FeatureRelevanceConf
from apps.remote.call import DataPrepare
from studio.feature_comment_handle.featrue_process import FeatureProcess

from vendor.utils.shunt_operator_judge import *
from vendor.errors.remote_error import *
from vendor.errors.contact_error import *
from vendor.errors.api_errors import *
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
        self.argument_base = ArgsContext(self.apply_id)
        self.useful_data = {}
        self.is_relevance = False
        self.relevance_feature_list = []
        self.relevance_data_identity_list = []

    def get_feature(self):
        logger.info('Stream in courier function name : get_feature Feature name :%s' %
                    self.feature_name)
        self.data_identity_list = self._get_di_from_conf(self.feature_conf)
        if self.collect_type == 'Courier':
            logger.info('Stream in courier function name : get_feature collect_type is Courier')
            self.get_general_data()

        elif len(self.data_identity_list) > 1 and self.collect_type == 'ShuntCourier':
            logger.info('Stream in courier function name : get_feature collect_type is ShuntCourier')
            self.get_shunt_data()

        elif self.collect_type == 'RelevanceCourier':
            logger.info('Stream in courier function name : get_feature collect_type is RelevanceCourier')
            self.get_relevance_data()

        if not self.useful_data:
            logger.error('Get feature value error : useful data is empty  feature_name is %s' % self.feature_name)
            raise FeatureProcessError
        return self.data_analysis(self.feature_name, self.useful_data)

    @staticmethod
    def data_analysis(feature_name, useful_data):

        feature_obj = FeatureProcess(feature_name, useful_data)
        ret = feature_obj.run()
        if not ret:
            logger.error('Feature:%s return is None' % feature_name)
            raise HandleWorkError
        if feature_name not in ret.keys():
            logger.error(
                'Wrong config of the feature, not the expect feature_name, feature_name: %s' % feature_name)
            raise FeatureConfigError
        logger.info('Feature Handle completed, result is \n%s' % ret)
        return ret

    def get_useful_data(self, data_identity):
        args_config = self.feature_conf.get(data_identity)
        if not args_config:
            logger.error("feature_name:%s config error in common feature table miss data_identity:%s"
                         % (self.feature_name, data_identity))
            raise CommonFeatureConfigError
        dp = DataPrepare(data_identity, self.apply_id, self.feature_conf[data_identity], self.collect_type)
        data = dp.get_original_data()
        return data

    def get_general_data(self):
        logger.info('Stream in courier function name : get_general_data')
        for data_identity in self.data_identity_list:
            data = self.get_useful_data(data_identity)
            if not data:
                logger.error('Get origin data error, data_identity is : %s' %data_identity)

                raise OriginDataGetError
            self.useful_data.update({data_identity: data})
        logger.info('Stream get_general_data complete\nUseful_data : %s' % self.useful_data)

    def get_shunt_data(self):
        logger.info('Stream in courier function name : get_shunt_data')
        feature_conf_list = FeatureShuntConf.objects.filter(
            feature_name=self.feature_name,
            is_delete=False
        ).order_by('id')
        if not feature_conf_list:
            logger.error("feature_name:%s miss config  in shunt feature table" % self.feature_name)
            raise ShuntFeatureConfigError
        apply_base = ApplyContext(self.apply_id)
        apply_data = (apply_base.load())['data']
        has_value = False
        for feature_conf in feature_conf_list:
            shunt_key = feature_conf.shunt_key
            data_identity = feature_conf.data_identity
            value = apply_data.get(shunt_key, None)
            if not value:
                logger.error("feature_name:%s shunt_key:%s get value error  in shunt feature table"
                             % (self.feature_name, shunt_key))
                raise GetArgumentsError
            oper = feature_conf.shunt_type
            oper = eval(oper)
            po = oper(value)
            shunt = po.distinguish()
            if shunt in eval(feature_conf.shunt_value):
                useful_data_identity = data_identity
                if not useful_data_identity:
                    logger.error("feature_name:%s  miss  data_identity in shunt feature table" % self.feature_name)
                    raise ShuntFeatureConfigError
                data = self.get_useful_data(data_identity)
                if data:
                    has_value = True
                    data = {data_identity: data}
                    logger.info('Find shunt_data,stream get_shunt_data complete\nUseful_data : %s' % data)
                    self.useful_data.update(data)
                    break

        if not has_value:
            logger.error('Get origin data error, feature_name is : %s' %
                         self.feature_name)
            raise OriginDataGetError

    def get_relevance_data(self):
        self._get_relevance_feature_list(self.feature_name)
        if len(self.relevance_feature_list) != len(self.relevance_data_identity_list):
            logger.error("feature_name:%s config error in relevance feature table " % self.feature_name)
            raise RelevanceFeatureConfigError
        self._get_relevance_feature_userful_data(self.relevance_feature_list, self.relevance_data_identity_list)

    def _get_relevance_feature_list(self, feature_name):
        relevance_conf = FeatureRelevanceConf.objects.filter(
            feature_name=feature_name,
            is_delete=False
        )[0]
        if not relevance_conf:
            logger.error("Don't find feature_name:%s config in relevance feature table " % feature_name)
            raise RelevanceFeatureConfigError
        self.relevance_data_identity_list.append(relevance_conf.data_identity)
        self.relevance_feature_list.append(feature_name)
        next_feature = relevance_conf.depend_feature
        if next_feature:
            next_feature_list = next_feature.split(',')
            for feature in next_feature_list:
                self._get_relevance_feature_list(feature)

    def _get_relevance_feature_userful_data(self, relevance_feature_list, relevance_data_identity):

        feature_data_identity_list = zip(relevance_feature_list, relevance_data_identity)
        feature_data_identity_list.reverse()
        logger.info("Relevance feature:%s config order:\n%s" % (self.feature_name, feature_data_identity_list))
        for feature_name, data_identity in feature_data_identity_list:
            if isinstance(data_identity, list):
                self._get_relevance_feature_userful_data(feature_name, data_identity)

            data = self.get_useful_data(data_identity)
            if not data:
                logger.error('Get origin data error,feature_name is:%s data_identity:%s'
                             % (self.feature_name, data_identity))
                raise OriginDataGetError
            self.useful_data.update({data_identity: data})
            if feature_name != feature_data_identity_list[-1][0]:
                feature_value = self.data_analysis(feature_name, data)
                self.argument_base.kwargs.update(feature_value)
                self.argument_base.save()
        logger.info('Stream get_relevance_data complete\nUseful_data : %s' % self.useful_data)

    def _get_di_from_conf(self, base_conf):
        logger.info('Stream in courier function name : _get_di_from_conf\nBase_conf :%s' %
                    base_conf)
        data_identity_list = base_conf.keys()
        if 'collect_type' in data_identity_list:
            self.collect_type = base_conf['collect_type']
            data_identity_list.remove('collect_type')
        logger.info('Data_identity_list : %s' % data_identity_list)
        return data_identity_list
