# -*- coding:utf-8 -*-

import re

from vendor.errors.feature import FeatureProcessError
from vendor.func_lib.map_handle import *
from vendor.func_lib.assert_handle import *
from vendor.func_lib.filter_handle import *
from vendor.func_lib.reduce_handle import *


def func_exec_chain(data, chains):
    chain_list = chains.split('->') if chains else []
    for func in chain_list:
        args = ''
        try:
            f = re.search("(.*)\\((.*)\\)", func)
            if f:
                func = f.group(1)
                args = f.group(2)

            func = eval(func)
        except:
            raise FeatureProcessError("exec_chain Error: don't find function %s" % func)
        if args:
            if args.startswith("[") or args.startswith("{"):
                args = eval(args)
            else:
                args = args.split(',')
                args_tmp = []
                for i in args:
                    if i.startswith("\'"):
                        arg = i.strip("\'")
                    elif i.startswith("""\""""):
                        arg = i.strip("\"")
                    else:
                        arg = eval(i)
                    args_tmp.append(arg)
                args = args_tmp
                if len(args) == 1:
                    args = args[0]
            # print args
            data = func(data, args)
        else:
            data = func(data)
    return data


def func_exec_operator_chain(value, chains):
    chain_list = chains.split('->') if chains else []
    for operator in chain_list:
        if '#' in operator:
            judge = eval(operator[1:])
            if judge:
                continue
            else:
                raise FeatureProcessError('exec_operator_chain Error value: %s assert: %s' % (value, operator[1:]))
        try:
            value = eval(operator)
        except:
            raise FeatureProcessError('exec_operator_chain Error value: %s operator: %s' % (value, operator))
    return value


if __name__ == '__main__':
    data = [1, 5]
    chains = "f_assert_not_null->f_assert_must_digit->f_assert_must_between(0,100)"
    print func_exec_chain(data, chains)

