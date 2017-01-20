# -*- coding:utf-8 -*-
"""
    Copyright (c) 2013-2016 SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/22
    Change Activity:

"""
import logging
import json

from apps.remote.models import FeatureFieldRel
from apps.etl.context import ApplyContext
from vendor.errors.api_errors import *

logger = logging.getLogger('apps.featureapi')


class Judger(object):
    """
        1.authentication (_check_identity)
        2.data decryption (_decrypt)
        3.check availability of arguments (_args_useful_check)
        4.throw the Exceptions
        5.finally check all works
    """

    def __init__(self, content):
        self.content = content
        self.feature_list = []

    def work_stream(self):
        pass

    def fill_attributes(self):
        pass

    def _prepare_args(self):
        pass
