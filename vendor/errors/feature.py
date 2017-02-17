# -*- coding: utf-8 -*-

from vendor.errors.common import ServerError


class FeatureProcessError(ServerError):
    status = ''
    message = ''
