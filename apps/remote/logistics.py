# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH(Shaohan Niu), All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/26
    Change Activity:
"""

# TODO 传进来的参数已经过验证  全部是可用的

# TODO 获取common_data , 和 apply_id

# TODO 根据apply_id 查询历史数据库中是否有历史数据

# TODO 有历史数据则直接返回, 没有的话  去DataOcean获取一下子

# TODO 获取回来的原始数据留存一份, 然后甩到特征处理环节

# TODO 特征处理返回的数据留存, 留存格式 (apply_id + 请求用参数包 + 访问接口 + 数据结果)

# TODO 整合得到的结果  甩回去给上一步 准备返回
