# -*- coding:utf-8 -*-

from vendor.errors.feature import FeatureProcessError


def f_assert_not_null(value_list):
    for value in value_list:
        if value in (None, ''):
            raise FeatureProcessError()
    return value_list


def f_assert_must_digit(value_list):
    for value in value_list:
        if not str(value).isdigit():
            raise FeatureProcessError()
    return value_list
