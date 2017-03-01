# -*- coding:utf-8 -*-

from vendor.errors.feature import FeatureProcessError


def f_assert_not_null(value_list):
    """检测值是否非空或值得列表是否存在非空元素"""
    tmp = value_list
    if not isinstance(tmp, list):
        tmp = [tmp]
    for value in tmp:
        if value in (None, '', {}, [], ()):
            raise FeatureProcessError("value: %s f_assert_not_null Error" % value_list)
    return value_list


def f_assert_must_int(value_list):
    """检测列表中的元素是否为int类型"""
    for value in value_list:
        if not isinstance(value, int):
            raise FeatureProcessError('%s f_assert_must_int Error' % value_list)
    return value_list


def f_assert_must_list(value_list):
    """检测列表中的元素是否为list类型"""
    for value in value_list:
        if not isinstance(value, list):
            raise FeatureProcessError('%s f_assert_must_list Error' % value_list)
    return value_list


def f_assert_must_dict(value_list):
    """检测列表中的元素是否为dict类型"""
    for value in value_list:
        if not isinstance(value, dict):
            raise FeatureProcessError('%s f_assert_must_dict Error' % value_list)
    return value_list


def f_assert_must_digit(value_list):
    """检测列表中的元素是否为数字"""
    for value in value_list:
        if not str(value).isdigit():
            raise FeatureProcessError('%s f_assert_must_digit Error' % value_list)
    return value_list


def f_assert_must_basestring(value_list):
    """检测列表中的元素是否为字符串"""
    for value in value_list:
        if not isinstance(value, basestring):
            raise FeatureProcessError('%s f_assert_must_basestring Error' % value_list)
    return value_list


def f_assert_must_digit_or_float(value_list):
    """检测列表中的元素是否为数字或float"""
    for value in value_list:
        if not (str(value).count('.') <= 1 and str(value).replace('.', '').lstrip('-').isdigit()):
            raise FeatureProcessError('%s f_assert_must_digit_or_float Error' % value_list)
    return value_list


def f_assert_must_between(value_list, args):
    """
    检测列表中的元素是否为数字且在args的范围内

    :param value_list: 待检测列表
    :param args:        范围列表
    :return:            异常或原值

    example：
                :value_list  [2, 2, 3]
                :args  [1,3]
    """

    assert len(args) == 2
    for value in value_list:
        if not (str(value).isdigit() and int(args[0]) <= int(value) <= int(args[1])):
            raise FeatureProcessError('%s f_assert_must_between %s Error' % (value_list, args))
    return value_list


def f_assert_seq0_gte_seq1(value_list):
    """检测列表中的第一个元素是否大于等于第二个元素"""
    if not value_list[0] >= value_list[1]:
        raise FeatureProcessError('%s f_assert_seq0_gte_seq1 Error' % value_list)
    return value_list


if __name__ == '__main__':
    print f_assert_must_digit_or_float([1, '1.0'])
