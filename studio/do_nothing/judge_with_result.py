# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/26
    Change Activity:
"""


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):
        """
        在这里写数据处理逻辑
        self.data就是DataOcean直接返回来的数据

        这里一顿处理 一顿计算 乱七八糟儿的自己写

        :return: 返回经过处理之后的数据
        返回数据格式  key:value
        """

        # TODO 抽取DataOcean返回的源数据
        content = self.data.content
        key = self.data.key
        result = self.data.result

        # TODO 计算维度
        if result == u'00':
            value = True
        else:
            value = False
        return {key: value}
