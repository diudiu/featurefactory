# -*- coding:utf-8 -*-

import os
from django.utils.module_loading import import_string
from jsonparse_handle import JSONPathParser
from exec_chain_handle import func_exec_chain
from apps.etl.models import FeatureProcess as FeatureProcessTable
from vendor.utils.defaults import *

import logging

logger = logging.getLogger('apps.common')


def load_feature_config():
    path = os.path.dirname(__file__)
    file_list = os.listdir(path)
    config = {}
    for file in file_list:
        if file.endswith('_config.py'):
            title = 'studio.feature_comment_handle.%s.config' % file[:-3]
            configs = import_string(title)
            config.update(configs)
    return config


config = load_feature_config()


class FeatureProcess(object):
    def __init__(self, feature_name, data):
        """ 初始化

        Args:
            :param feature_name  特征名称
            :param data  从接口获取到的数据

        Attributes:
            :attr feature_name  特征名称
            :attr data  从接口获取到的数据
            :attr feature_config_context  特征配置的上下文，配置上下文的数据结构如下：
                "feature_name": 特征名称
                "feature_data_type": 特征数据类型
                "default_value": 特征缺省值
                "json_path_list": [
                    (
                        "application_on",   特征名
                        "$.apply_data.application_on",      jsonpath
                        "f_assert_not_null->f_assert_must_basestring"     断言链
                    ),
                    (...)       数据二
                ],
                "f_map_and_filter_chain": "",   前置map
                "reduce_chain": "",             reduce链
                "l_map_and_filter_chain": ""    后置map
            :attr function_context  函数库上下文
            :attr json_path_parser  JSONPath的解析对象
        """
        self.feature_name = feature_name
        self.conf_str = self.feature_name + '_config'
        self.feature_conf = None
        self.data = data
        self.default_value = None
        self.json_path_list = None
        self.f_map_and_filter_chain = None
        self.reduce_chain = None
        self.l_map_and_filter_chain = None

    def _load(self):
        try:
            self.feature_conf = config[self.conf_str]
            self.default_value = self.feature_conf['default_value']
            self.json_path_list = self.feature_conf['json_path_list']
            if not self.json_path_list:
                raise Exception("json_path_list cannot be empty!")
            self.f_map_and_filter_chain = self.feature_conf['f_map_and_filter_chain']
            self.reduce_chain = self.feature_conf['reduce_chain']
            self.l_map_and_filter_chain = self.feature_conf['l_map_and_filter_chain']
        except:
            raise NameError("%s config not find or config error!!! " % self.feature_name)

    def _load_config(self):
        feature_conf = FeatureProcessTable.objects.filter(feature_name=self.feature_name)
        if not feature_conf.count():
            raise NameError("%s config not find or config error!!! " % self.feature_name)
        self.feature_conf = feature_conf[0]
        self.default_value = self.feature_conf.default_value
        self.json_path_list = self.feature_conf.json_path_list
        if not self.json_path_list:
            raise Exception("json_path_list cannot be empty!")
        self.json_path_list = eval(self.json_path_list)
        self.f_map_and_filter_chain = self.feature_conf.f_map_and_filter_chain
        self.reduce_chain = self.feature_conf.reduce_chain
        self.l_map_and_filter_chain = self.feature_conf.l_map_and_filter_chain

    def run(self):
        """ 实际执行的方法，获取特征加工的结果

        Raises:
             FeatureProcessError  自定义的特征处理异常，在程序的外层可捕获该异常
        """
        try:
            # self._load()
            self._load_config()
            json_path_parser = JSONPathParser()
            value_list = json_path_parser.parsex(self.data, self.json_path_list)
            result = []
            for i in value_list:
                result = result + i[3]
            if len(result) == 1 and isinstance(result[0], list):
                result = result[0]
            if self.f_map_and_filter_chain:
                result = func_exec_chain(result, self.f_map_and_filter_chain)

            if self.reduce_chain:
                result = func_exec_chain(result, self.reduce_chain)
            if self.l_map_and_filter_chain:
                result = func_exec_chain(result, self.l_map_and_filter_chain)

        except NameError as e:
            logger.error(e.message)
            return None
        except Exception as e:
            logger.error(e.message)
            return {self.feature_name: eval(self.default_value)}
        return {self.feature_name: result}
