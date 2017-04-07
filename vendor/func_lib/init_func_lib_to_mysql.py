# -*- coding:utf-8 -*-
import os, sys

home_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(home_path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'featurefactory.settings')

from django.utils.module_loading import import_string
from apps.etl.models import FuncLibSource
import assert_handle, filter_handle, map_handle, reduce_handle

assert_handle_dir = dir(assert_handle)
filter_handle_dir = dir(filter_handle)
map_handle_dir = dir(map_handle)
reduce_handle_dir = dir(reduce_handle)
func_type = lambda x: x


def get_func(x, types, func_flag):
    for i in eval('%s_dir' % x):
        m = import_string('vendor.func_lib.%s.%s' % (x, i))
        if type(m) == type(func_type) and i.startswith(func_flag):
            function_name = m.__name__
            function_doc = m.__doc__
            deault = 'deault'
            f_args_name = m.__code__.co_varnames[0]
            s_args_name = ''
            if m.__code__.co_argcount == 2:
                s_args_name = m.__code__.co_varnames[1]
                if m.__defaults__:
                    deault = m.__defaults__[0]
            if s_args_name != '':
                if deault != 'deault':
                    function_name_all = '%s(%s, %s=%s)' % (function_name, f_args_name, s_args_name, deault)
                else:
                    function_name_all = '%s(%s, %s)' % (function_name, f_args_name, s_args_name)
            else:
                function_name_all = '%s(%s)' % (function_name, f_args_name)
            # print function_name_all
            # print function_doc
            if FuncLibSource.objects.filter(func_name=function_name_all).count():
                FuncLibSource.objects.filter(func_name=function_name_all).update(
                    func_desc=function_doc,
                    func_type=types
                )
            else:
                FuncLibSource(
                    func_name=function_name_all,
                    func_desc=function_doc,
                    func_type=types
                ).save()


if __name__ == '__main__':
    get_func('assert_handle', 'A', 'f_')
    get_func('filter_handle', 'F', 'f_')
    get_func('map_handle', 'M', 'm_')
    get_func('reduce_handle', "R", 'r_')
