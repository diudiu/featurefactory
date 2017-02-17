# -*- coding: utf-8 -*-

import operator
from collections import Iterable

from vendor.utils.constant import cons


class GenericUtils(object):
    """
    计算和分析使用到的通用工具类

    :Usage:
        ```
            from vendor.utils.analyzer import GenericUtils

            collection = [([0, 100], 1), ([100, 10000]， 2)]
            GenericUtils.get_mapped_value(collection, 10)
        ```
    """
    mapped_tuple_length = 2
    arithmetic_method_common_prefix = '_arithmetic_'

    @classmethod
    def get_mapped_value(cls, collection, original_val, arithmetic_type=cons.ARITHMETIC_LEFT_CLOSE_RIGHT_OPEN):
        """
        从指定的数据集合中，获取映射之后的值；
        运算类型支持左开右闭、左闭右开，默认是左闭右开；

        :param collection  要使用的映射的集合，数据结构需要满足如下格式：
            [("博士", 1), ("硕士"， 2)] 或者 [([0, 100], 1), ([100, 10000]， 2)]

        :param original_val  被映射的原始值
        :param arithmetic_type  运算类型，默认是左闭右开，映射只是一对一映射时，此参数无效

        :return: 被映射之后的值
        """
        if not isinstance(collection, Iterable):
            raise

        mapped_value = None

        for item in collection:
            if isinstance(item, tuple) and \
                    operator.ge(len(item), cls.mapped_tuple_length):
                mapped_option = item[0]
                if isinstance(mapped_option, basestring):
                    if mapped_option == original_val:
                        mapped_value = item[1]
                        break
                elif isinstance(mapped_option, list):
                    is_hit = cls._arithmetic_by_type(mapped_option, original_val, arithmetic_type=arithmetic_type)
                    if is_hit:
                        mapped_value = item[1]
                        break

        return mapped_value

    @classmethod
    def _arithmetic_by_type(cls, option_list, original_val, arithmetic_type=cons.ARITHMETIC_LEFT_CLOSE_RIGHT_OPEN):
        invoke_method_str = "%s%s" % (cls.arithmetic_method_common_prefix, arithmetic_type.lower())
        invoke_method = getattr(cls, invoke_method_str)
        if callable(invoke_method):
            return invoke_method(option_list, original_val)

        raise Exception("")

    @classmethod
    def _arithmetic_left_close_right_open(cls, option_list, original_val):
        if operator.le(option_list[0], original_val) and \
                operator.lt(original_val, option_list[1]):
            return True

        return False

    @classmethod
    def _arithmetic_left_open_right_close(cls, option_list, original_val):
        if operator.lt(option_list[0], original_val) and \
                operator.le(original_val, option_list[1]):
            return True

        return False
