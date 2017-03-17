# -*- coding:utf-8 -*-
import re

from vendor.errors.feature import FeatureProcessError
from vendor.func_lib.map_handle import *
from vendor.func_lib.assert_handle import *
from vendor.func_lib.filter_handle import *
from vendor.func_lib.reduce_handle import *


def do_assert_list(data, func_list_str):
    if not data:
        raise
    data = data[0]
    func_list = func_list_str.split('->')

    for func in func_list:
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

