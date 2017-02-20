# -*- coding: utf-8 -*-
"""
Usage:
   - 特征取值是字符串的场景
   from vendor.utils.defaults import StringTypeDefault

   result = {
       "city_name": StringTypeDefault
   }

   - 特征取值是布尔类型的场景
   from vendor.utils.defaults import BooleanTypeDefault
   result = {
       "is_net_black": BooleanTypeDefault
   }

   - 特征取值是正整数类型的场景
   from vendor.utils.defaults import PositiveSignedTypeDefault
   result = {
       "is_net_black": PositiveSignedTypeDefault
   }

"""


class Default(object):
    """ 所有缺省值的顶级父类 """
    value = None


class StringTypeDefault(Default):
    """ 特征取值如果是字符串类型的，将此类型作为缺省值 """
    value = "**UNKNOWN**"


class BooleanTypeDefault(Default):
    """ 特征取值如果是布尔类型的，将此类型作为缺省值 """
    value = -1


class PositiveSignedTypeDefault(Default):
    """ 特征取值如果是正数类型的，将此类型作为缺省值 """
    value = -1


class NegativeSignedTypeDefault(Default):
    """ 特征取值如果是负数类型的，将此类型作为缺省值 """
    value = 1


class UnsignedIntTypeDefault(Default):
    """ 特征取值如果是无符号整数类型的，将此类型作为缺省值 """
    # 32位的系统最大值是2的32次方，64位系统最大值是2的64次方
    # value = sys.maxint
    value = 2 ** 31 - 1


class UnsignedLongTypeDefault(Default):
    """ 特征取值如果是无符号长整数类型的，将此类型作为缺省值 """
    # 为了考虑32位系统的兼容性问题，考虑使用16字节的最大值进行表示
    # long_sizeof_bit = sys.getsizeof(1L) * 8
    # long_sizeof_bit = 16 * 8
    value = UnsignedIntTypeDefault.value


class PositiveSignedFloatTypeDefault(Default):
    """ 特征取值如果是正的浮点类型的，将此类型作为缺省值 """
    value = float(PositiveSignedTypeDefault.value)


class NegativeSignedFloatTypeDefault(Default):
    """ 特征取值如果是负的浮点类型的，将此类型作为缺省值 """
    value = float(NegativeSignedTypeDefault.value)


class UnsignedFloatTypeDefault(Default):
    """ 特征取值如果是无符号浮点类型的，将此类型作为缺省值 """

    # 为了考虑32位系统的兼容性问题，考虑使用16字节的最大值进行表示
    # float_sizeof_bit = sys.getsizeof(1.0) * 8
    # float_sizeof_bit = 16 * 8
    value = float(UnsignedIntTypeDefault.value)


class ListTypeDefault(Default):
    """ 特征取值如果是列表类型的，将此类型作为缺省值 """
    value = None


class DictTypeDefault(Default):
    """ 特征取值如果是字典类型的，将此类型作为缺省值 """
    value = None
