# -*- coding: utf-8 -*-

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
        for item in collection:
            pass

        return None
