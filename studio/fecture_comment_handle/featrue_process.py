# -*- coding:utf-8 -*-

from jsonparse_handle import JSONPathParser
from exec_chain_handle import func_exec_chain, func_exec_operator_chain
from vendor.errors.feature import FeatureProcessError
from vendor.utils.defaults import *

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
                    "json_path_list": [("path的key值", "path的路径，如$..content.age", "断言链，如f_assert_not_null->f_assert_must_int->f_assert_length_must(10)"), (...)],
                    "map_and_filter_chain": "map和filter的调用链，如m_to_int->m_none_to_zero->f_del_lte(100)->m_all_add(10)",
                    "reduce_chain": "reduce的处理链，如r_add"
                }
            :attr function_context  函数库上下文
            :attr json_path_parser  JSONPath的解析对象
        """
        self.feature_name = feature_name
        self.data = data
        self.default_value = self.load_feature_config()['default_value']
        self.json_path_list = self.load_feature_config()['json_path_list']
        self.map_and_filter_chain = self.load_feature_config()['map_and_filter_chain']
        self.reduce = self.load_feature_config()['reduce']
        self.operator_chain = self.load_feature_config()['operator_chain']

    def run(self):
        """ 实际执行的方法，获取特征加工的结果

        Raises:
             FeatureProcessError  自定义的特征处理异常，在程序的外层可捕获该异常
        """
        result = {self.feature_name: eval(self.default_value)}
        try:
            json_path_parser = JSONPathParser()
            value_list = json_path_parser.parse(self.data, self.json_path_list)
            seq = []
            for i in value_list:
                seq = seq + i[3]
            if self.map_and_filter_chain:
                seq = func_exec_chain(seq, self.map_and_filter_chain)
            if not self.reduce:
                raise FeatureProcessError
            value = func_exec_chain(seq, self.reduce)
            if self.operator_chain:
                value = func_exec_operator_chain(value, self.operator_chain)
        except FeatureProcessError as e:
            print e.message
            return {self.feature_name: eval(self.default_value)}
        return {self.feature_name: value}

    def load_feature_config(self):
        """从特征配置的文件中加载特征的配置，放入特征处理的上下文中

        Raises:
            FeatureConfigLoadError  自定义的特征配置加载异常，继承自FeatureProcessError
        """
        # feature_config = {
        #     "feature_name": "age",
        #     "feature_data_type": "int",
        #     "default_value": "PositiveSignedTypeDefault",
        #     "json_path_list": [("age", "$..content.age", "f_assert_not_null->f_assert_must_digit")],
        #     "map_and_filter_chain": "",
        #     "reduce": "reduce_singo_value",
        #     "operator_chain": ""
        # }
        feature_config = {
            "feature_name": "apply_register_duration",
            "feature_data_type": "float",
            "default_value": "PositiveSignedFloatTypeDefault",
            "json_path_list": [("application_on", "$.apply_data.application_on", "f_assert_not_null->f_assert_must_basestring"),
                               ("registration_on", "$.portrait_data.registration_on","f_assert_not_null->f_assert_must_basestring")],
            "map_and_filter_chain": "map_to_slice(0,10)->map_string_to_datetime",
            "reduce": "reduce_sub",
            "operator_chain": "value.days->value/30.0->round(value, 2)->#value>=0"
        }
        return feature_config
