# -*- coding:utf-8 -*-

from vendor.func_lib.assert_handle import *
from vendor.func_lib.map_filter_reduce_handle import *
from vendor.errors.feature import FeatureProcessError


def func_exec_chain(data, chains):
    chain_list = chains.split('->') if chains else []
    for func in chain_list:
        try:
            func = eval(func)
        except:
            raise FeatureProcessError()
        data = func(data)

    return data

