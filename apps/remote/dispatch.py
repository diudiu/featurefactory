# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/26
    Change Activity:
"""
import logging

from apps.remote.courier import Courier
from apps.etl.fabrication import Fabricate
from vendor.utils.constant import cons

logger = logging.getLogger('apps.remote')


def dispatch(useful_common_data, useful_args):
    """
    Save the original data and calculate the features
    :param useful_common_data:dict
    :param useful_args:dict
    :return:dict
    """
    courier = Courier(useful_common_data, useful_args)
    # TODO step 1: get and save original data
    temp_data = courier.get_data_by_keys()
    # TODO step 3: dispose and save the process data used original data
    apply_id = useful_common_data[cons.APPLY_ID]
    fabrica = Fabricate(temp_data, useful_args, apply_id)
    res_data = fabrica.fabricate()
    return res_data
