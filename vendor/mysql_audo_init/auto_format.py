# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH(Shaohan Niu), All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/26
    Change Activity:

"""

from vendor.mysql_audo_init.mysql_auto_initialization import add_client_overview
from vendor.mysql_audo_init.data_source_info_init import init_data_source
from vendor.mysql_audo_init.feature_field_rel_init import init_feature_field


if __name__ == '__main__':
    add_client_overview()
    init_data_source()
    init_feature_field()
