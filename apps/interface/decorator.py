# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/26
    Change Activity:

"""
from functools import wraps


def data_check(view_func):
    """

    :param view_func:
    :return:
    """
    @wraps(view_func)
    def _wrapped_view_func(request, *args, **kwargs):
        pass

    return _wrapped_view_func


def json_load(view_func):
    """

    :param view_func:
    :return:
    """
    @wraps(view_func)
    def _wrapped_view_func(request, *args, **kwargs):
        pass

    return _wrapped_view_func


def data_send(view_func):
    """

    :param view_func:
    :return:
    """
    @wraps(view_func)
    def _wrapped_view_func(request, *args, **kwargs):
        pass

    return _wrapped_view_func
