# -*- coding:utf-8 -*-
"""
    Copyright (c) 2013-2017 SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2017/2/10
    Change Activity:


        _==/          i     i           \==_
      /XX/            |\___/|            \XX\
    /XXXX\            |XXXXX|            /XXXX\
   |XXXXXX\_         _XXXXXXX_         _/XXXXXX|
  XXXXXXXXXXXxxxxxxxXXXXXXXXXXXxxxxxxxXXXXXXXXXXX
 |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
 |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
  XXXXXX/^^^^^\XXXXXXXXXXXXXXXXXXXXX/^^^^^\XXXXXX
   |XXX|       \XXX/^^\XXXXX/^^\XXX/       |XXX|
     \XX\       \X/    \XXX/    \X/       /XX/
        "\       "      \X/      "      /"
"""

import re

from vendor.utils.constant import cons


class PhoneOperator(object):

    def __init__(self, mobile):
        self.mobile = ''.join(mobile.split())

    def distinguish(self):
        p_yd = re.compile(cons.YD_MATCH_STR)
        p_unicom = re.compile(cons.UNICOM_MATCH_STR)
        p_telecom = re.compile(cons.TELECOME_MATCH_STR)

        if p_yd.match(self.mobile):
            return cons.YD_MOBILE_NUMBER
        if p_unicom.match(self.mobile):
            return cons.UNICOM_MOBILE_NUMBER
        if p_telecom.match(self.mobile):
            return cons.TELECOME_MOBILE_NUMBER
