# -*- coding:utf-8 -*-

from vendor.errors.feature import FeatureProcessError


def f_assert_not_null(value_list):
    for value in value_list:
        if value in (None, '', {}, [], ()):
            raise FeatureProcessError()
    return value_list


def f_assert_must_int(value_list):
    for value in value_list:
        if not isinstance(value, int):
            raise FeatureProcessError()
    return value_list


def f_assert_must_list(value_list):
    for value in value_list:
        if not isinstance(value, list):
            raise FeatureProcessError()
    return value_list


def f_assert_must_dict(value_list):
    for value in value_list:
        if not isinstance(value, dict):
            raise FeatureProcessError()
    return value_list


# def f_assert_must_digit(value_list):
#     for value in value_list:
#         if not str(value).isdigit():
#             raise FeatureProcessError()
#     return value_list


def f_assert_must_basestring(value_list):
    for value in value_list:
        if not isinstance(value, basestring):
            raise FeatureProcessError()
    return value_list


def f_assert_must_digit_or_float(value_list):
    for value in value_list:
        if not (str(value).count('.') <= 1 and str(value).replace('.', '').isdigit()):
            raise FeatureProcessError()
    return value_list


def f_assert_must_between(value_list, args):
    assert len(args) == 2
    for value in value_list:
        if not (str(value).isdigit() and int(args[0]) <= int(value) <= int(args[1])):
            raise FeatureProcessError()
    return value_list


if __name__ == '__main__':
    print f_assert_must_digit_or_float([1, '1.0'])
