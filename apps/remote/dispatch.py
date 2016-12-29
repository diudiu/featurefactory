# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH(Shaohan Niu), All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/26
    Change Activity:
"""
from apps.remote.courier import Courier


def dispatch(useful_common_data, useful_args):
    """
    Save the original data and calculate the features
    :param useful_common_data:dict
    :param useful_args:dict
    :return:dict
    """

    courier = Courier(useful_common_data, useful_args)

    # TODO step 1: get data
    temp_data = courier.get_data_by_keys()
    # TODO step 2: save original data
    cache_data = temp_data['cache']
    fresh_data = temp_data['fresh']
    # TODO step 3: dispose the original data

    # TODO step 4: save the process data

    # TODO step 5: return the useful data
    return {}
