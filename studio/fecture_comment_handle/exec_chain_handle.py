# -*- coding:utf-8 -*-

import re
from vendor.func_lib.assert_handle import *
from vendor.func_lib.map_filter_reduce_handle import *
from vendor.errors.feature import FeatureProcessError


def func_exec_chain(data, chains):
    chain_list = chains.split('->') if chains else []
    args = ''
    for func in chain_list:
        try:
            f = re.search("(.*)\\((.*)\\)", func)
            if f:
                func = f.group(1)
                args = f.group(2).split(',')
            func = eval(func)
        except:
            raise FeatureProcessError()
        if args:
            data = func(data, args)
        else:
            data = func(data)

    return data

if __name__ == '__main__':
    data = [1, 5]
    chains = "f_assert_not_null->f_assert_must_digit->f_assert_must_between(0,100)"
    print func_exec_chain(data, chains)

    data = ['gyfgyfgyf']
    chains = 'map_to_slice(1,3)'
    print func_exec_chain(data, chains)


