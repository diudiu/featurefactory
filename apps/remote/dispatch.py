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

    courier = Courier(useful_common_data, useful_args)

    # TODO step 1: get data
    ret_data = courier.get_keys()
    # TODO step 2: save original data

    # TODO step 3: dispose the original data

    # TODO step 4: save the process data

    # TODO step 5: return the useful data
    return ret_data
