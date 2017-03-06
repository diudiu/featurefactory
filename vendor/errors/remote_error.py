# -*- coding: utf-8 -*-

from vendor.errors.common import ServerError
from vendor.messages.response_code import ResponseCode


class OriginDataGetError(ServerError):
    status = ResponseCode.ORIGIN_DATA_GET_ERROR
    message = ResponseCode.message(status)
