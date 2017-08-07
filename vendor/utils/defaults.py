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

# 特征取值如果是字符串类型的，将此类型作为缺省值
StringTypeDefault = "UNKNOWN"

# 特征取值如果是布尔类型的，将此类型作为缺省值
BooleanTypeDefault = -1

# 特征取值如果是正数类型的，将此类型作为缺省值
PositiveSignedTypeDefault = -1

# 特征取值如果是负数类型的，将此类型作为缺省值
NegativeSignedTypeDefault = 1

# 特征取值如果是负数类型的，将此类型作为缺省值
UnsignedIntTypeDefault = 2 ** 31 - 1

# 特征取值如果是负数类型的，将此类型作为缺省值
UnsignedLongTypeDefault = UnsignedIntTypeDefault

# 特征取值如果是正的浮点类型的，将此类型作为缺省值
PositiveSignedFloatTypeDefault = float(PositiveSignedTypeDefault)

# 特征取值如果是正的浮点类型的，将此类型作为缺省值
NegativeSignedFloatTypeDefault = float(NegativeSignedTypeDefault)

# 特征取值如果是无符号浮点类型的，将此类型作为缺省值
UnsignedFloatTypeDefault = float(UnsignedIntTypeDefault)

# 特征取值如果是列表类型的，将此类型作为缺省值
ListTypeDefault = None

# 特征取值如果是字典类型的，将此类型作为缺省值
DictTypeDefault = None
