# -*- coding:utf-8 -*-
"""
    Copyright (c) 2013-2016 SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/22
    Change Activity:

"""
from studio import do_nothing
from django.utils.module_loading import import_string


# 抽象处理方法
class Machine(object):

    def __init__(self, key=None, data=None):
        self.key = key
        self.data = data.get('content', None)
        self.data_identity = data.get('data_identity', None)
        self.result = data.get('result', None)

    def dispose_data(self):
        pass


# 一类机械(什么也不干)
class DoNothingMachine(Machine):
    def __init__(self, key, data):
        super(DoNothingMachine, self).__init__(key, data)

    def dispose_data(self):
        # 判断返回result码决定结果的 (黑名单系列)
        func = import_string('studio.do_nothing.judge_with_result.Handle')
        obj = func(self.data)
        res = obj.handle()
        return res


# 二类机械(处理的数据来自一个数据源)
class SingleOriginMachine(Machine):
    def __init__(self, key, data):
        super(SingleOriginMachine, self).__init__(key, data)

    def dispose_data(self):
        pass


# 三类机械(处理用的数据来自多个不同数据源)
class ComboOriginMachine(Machine):
    def __init__(self, key, data):
        super(ComboOriginMachine, self).__init__(key, data)

    def dispose_data(self):
        pass
