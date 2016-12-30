# -*- coding:utf-8 -*-
"""
    Copyright (c) 2013-2016 SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/22
    Change Activity:

"""


# 抽象工厂
class Factory(object):

    def __init__(self):
        pass


# 一类工厂(什么也不干)
class DoNothingFactory(Factory):

    def __init__(self):
        super(DoNothingFactory, self).__init__()
        pass


# 二类工厂(处理的数据来自一个数据源)
class SingleOriginFactory(Factory):

    def __init__(self):
        super(SingleOriginFactory, self).__init__()
        pass


# 三类工厂(处理用的数据来自多个不同数据源)
class ComboOriginFactory(Factory):

    def __init__(self):
        super(ComboOriginFactory, self).__init__()
        pass
