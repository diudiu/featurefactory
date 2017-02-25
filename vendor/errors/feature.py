# -*- coding: utf-8 -*-

from vendor.errors.common import ServerError
from vendor.messages.response_code import ResponseCode


class FeatureProcessError(ServerError):
    status = ResponseCode.FEATURE_PROCESS_ERROR
    message = ResponseCode.message(status)
    log_message = message

    def __init__(self, message=None):
        if message:
            self.message = message

        super(FeatureProcessError, self).__init__(self.message)



