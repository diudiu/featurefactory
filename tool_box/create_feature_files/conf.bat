# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2013- DIGCREDIT, All Rights Reserved.
    -----------------------------------------------------------
    Author: 
    Date:  
    Change Activity:
"""
from vendor.utils.defaults import *

import logging

logger = logging.getLogger('apps.common')


class Handle(object):
    """
    Attributes:
        name: 特征名称，可由模版自动生成
    """
    name = "%s"

    def __init__(self, data):
        """
        初始化方法

        初始化特征处理类使用到的数据上下文

        Args: 
            data: 由调用处传进来的实际待处理的数据，data数据的样例数据：

            {<插入样例数据>}

            对data的处理可采用jsonpath的方式
        """
        pass

    def handle(self):
        """
        <描述特征计算方法>
        
        Dependency lists:
            
            Lists:
                
        
        Inputs:
            该特征计算需要使用到的字段列表：
                

        Outputs:
            overspeed_count: 

        Raises:
            可能会抛出的异常，在这里描述
        """
        result = {self.name: PositiveSignedTypeDefault}
