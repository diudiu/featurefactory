# -*- coding:utf-8 -*-

from jsonparse_handle import JSONPathParser
from exec_chain_handle import func_exec_chain, func_exec_operator_chain
from vendor.errors.feature import FeatureProcessError
from studio.fecture_comment_handle.config import *
from vendor.utils.defaults import *

import logging

logger = logging.getLogger('apps.common')


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
                {
                    "feature_name": "特征名称",
                    "feature_data_type": "特征的数据类型",
                    "default_value": "缺省值",
                    "json_path_list": [
                    (
                        "path的key值",
                        "path的路径，如$..content.age",
                        "断言链，如f_assert_not_null->f_assert_must_int->f_assert_length_must(10)"
                    ),
                    (...)
                    ],
                    "map_and_filter_chain": "map和filter的调用链，如m_to_int->m_none_to_zero->f_del_lte(100)->m_all_add(10)",
                    "reduce_chain": "reduce的处理链，如r_add"
                }
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
        self.default_value = self.feature_conf['default_value']
        self.json_path_list = self.feature_conf['json_path_list']
        self.f_map_and_filter_chain = self.feature_conf['f_map_and_filter_chain']
        self.reduce_chain = self.feature_conf['reduce_chain']
        self.l_map_and_filter_chain = self.feature_conf['l_map_and_filter_chain']

    def run(self):
        """ 实际执行的方法，获取特征加工的结果

        Raises:
             FeatureProcessError  自定义的特征处理异常，在程序的外层可捕获该异常
        """
        try:
            self.feature_conf = eval(self.conf_str)
            self._load()
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
            logging.error(e.message)
            return None
        except Exception as e:
            logging.error(e.message)
            return {self.feature_name: eval(self.default_value)}
        return {self.feature_name: result}

    def load_feature_config(self):
        """从特征配置的文件中加载特征的配置，放入特征处理的上下文中

        Raises:
            FeatureConfigLoadError  自定义的特征配置加载异常，继承自FeatureProcessError
        """
        try:
            self.feature_conf = eval(self.conf_str)
        except (NameError, TypeError) as e:
            # TODO logger
            raise FeatureProcessError