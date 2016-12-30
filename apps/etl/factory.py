# -*- coding:utf-8 -*-
"""
    Copyright (c) 2013-2016 SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/22
    Change Activity:

"""
from apps.etl.machine import Machine, DoNothingMachine, SingleOriginMachine, ComboOriginMachine


# 抽象工厂
class Factory(object):

    def __init__(self, data):
        self.data = data

    def __call__(self, son_type, key):
        if son_type == 'direct':
            return DoNothingFactory(key, self.data)


# 一类工厂(什么也不干)
class DoNothingFactory(Factory):

    def __init__(self, key, data):
        super(DoNothingFactory, self).__init__(data)
        self.machine = DoNothingMachine(key, self.data)


# 二类工厂(处理的数据来自一个数据源)
class SingleOriginFactory(Factory):

    def __init__(self, key, data):
        super(SingleOriginFactory, self).__init__(data)
        self.machine = SingleOriginMachine(key, self.data)


# 三类工厂(处理用的数据来自多个不同数据源)
class ComboOriginFactory(Factory):

    def __init__(self, key, data):
        super(ComboOriginFactory, self).__init__(data)
        self.machine = ComboOriginMachine(key, self.data)
