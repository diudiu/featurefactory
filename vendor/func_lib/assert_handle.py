# -*- coding:utf-8 -*-

from vendor.errors.feature import FeatureProcessError

"""
    此目录下所有功能函数均为:

        按一定条件检查传入参数合法性
        **若不合法, 将抛出异常**
"""


def f_assert_not_null(seq):
    """检测值是否非空或值得列表是否存在非空元素"""
    if seq in (None, '', [], {}, ()):
        raise FeatureProcessError("value: %s f_assert_not_null Error" % seq)

    if isinstance(seq, list):
        for value in seq:
            if value in (None, '', {}, [], ()):
                raise FeatureProcessError("value: %s f_assert_not_null Error" % seq)
    return seq


def f_assert_jsonpath_true(seq):
    """假设jsonpath查询到的为true seq为[]空列表时代表没查到字段"""
    if seq in ([],):
        raise FeatureProcessError("jsonpath not find field")
    return seq


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


def f_assert_must_digit(value_list, args=False):
    """
        检测列表中的元素是否为数字
        :param value_list: 待检测列表
        :param args:        负数是否通过 false 不通过报异常 True 负数通过
        :return:            异常或原值

        example：
                    :value_list  [-2,'-2', 3]
                    :args  false
                    ：return 异常

                    :value_list  [-2,'-2', 3]
                    :args  True
                    ：return [-2,'-2', 3]

    """

    for value in value_list:
        if args:
            if not str(value).lstrip('-').isdigit():
                raise FeatureProcessError('%s negative number=%s f_assert_must_digit Error' % (value_list, args))
        else:
            if not str(value).isdigit():
                raise FeatureProcessError('%s negative number=%s f_assert_must_digit Error' % (value_list, args))
    return value_list


def f_assert_must_basestring(value_list):
    """检测列表中的元素是否为字符串"""
    for value in value_list:
        if not isinstance(value, basestring):
            raise FeatureProcessError('%s f_assert_must_basestring Error' % value_list)
    return value_list


def f_assert_must_digit_or_float(value_list, args=False):
    """
        检测列表中的元素是否为数字或float, args=false 负数报异常 True 负数通过

        :param value_list: 待检测列表
        :param args:        负数是否通过 false 不通过报异常 True 负数通过
        :return:            异常或原值

        example：
                    :value_list  [-2.0,'-2', 3]
                    :args  false
                    ：return 异常

                    :value_list  [-2.0,'-2', 3]
                    :args  True
                    ：return [-2.0,'-2', 3]
    """

    for value in value_list:
        if args:
            if not (str(value).count('.') <= 1 and str(value).replace('.', '').lstrip('-').isdigit()):
                raise FeatureProcessError(
                    '%s  negative number=%s f_assert_must_digit_or_float Error' % (value_list, args))
        else:
            if not (str(value).count('.') <= 1 and str(value).replace('.', '').isdigit()):
                raise FeatureProcessError(
                    '%s negative number=%s f_assert_must_digit_or_float Error' % (value_list, args))
    return value_list


def f_assert_must_percent(value_list):
    """
        检测是否是百分数
    """

    for value in value_list:
        if not (str(value)[-1] == '%' and (str(value[:-1]).count('.') <= 1 and str(value[:-1]).replace('.', '').isdigit())):
                raise FeatureProcessError(
                    '%s f_assert_must_percent Error' % value_list)
    return value_list


def f_assert_must_between(value_list, args):
    """
    检测列表中的元素是否为数字或浮点数且在args的范围内

    :param value_list: 待检测列表
    :param args:        范围列表
    :return:            异常或原值

    example：
                :value_list  [2, 2, 3]
                :args  [1,3]

                :value_list  ['-2', '-3', 3]
                :args  ['-5',3]
    """

    assert len(args) == 2
    for value in value_list:
        if not (str(value).count('.') <= 1 and str(value).replace('.', '').lstrip('-').isdigit()
                and float(args[0]) <= float(value) <= float(args[1])):
            raise FeatureProcessError('%s f_assert_must_between %s Error' % (value_list, args))
    return value_list


def f_assert_seq0_gte_seq1(value_list):
    """检测列表中的第一个元素是否大于等于第二个元素"""
    if not value_list[0] >= value_list[1]:
        raise FeatureProcessError('%s f_assert_seq0_gte_seq1 Error' % value_list)
    return value_list


if __name__ == '__main__':
    print f_assert_must_percent(['7.0%'])
