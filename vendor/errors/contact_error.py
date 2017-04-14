# -*- coding: utf-8 -*-

from vendor.errors.common import ServerError
from vendor.messages.response_code import ResponseCode


class ClientCodeInexistence(ServerError):
    status = ResponseCode.UNAVAILABLE_CLIENT_CODE
    message = ResponseCode.message(status)


class MissingManageType(ServerError):
    status = ResponseCode.MISSING_JUDGE_TYPE
    message = ResponseCode.message(status)


class JudgeInitializeFailed(ServerError):
    status = ResponseCode.JUDGE_INIT_ERROR
    message = ResponseCode.message(status)


class JudgeWorkError(ServerError):
    status = ResponseCode.JUDGE_WORK_ERROR
    message = ResponseCode.message(status)


class JudgeReturenError(ServerError):
    status = ResponseCode.JUDGE_RET_ERROR
    message = ResponseCode.message(status)


class FeatureNameUnfound(ServerError):
    status = ResponseCode.FEATURE_UNFOUND
    message = ResponseCode.message(status)


class DataIdentityUnfound(ServerError):
    status = ResponseCode.DATAIDENTITY_UNFOUND
    message = ResponseCode.message(status)


class JunkmanInitializeFailed(ServerError):
    status = ResponseCode.JUNKMAN_INIT_ERROR
    message = ResponseCode.message(status)


class JunkmanWorkError(ServerError):
    status = ResponseCode.JUNKMAN_WORK_ERROR
    message = ResponseCode.message(status)


class HandleInitializeFailed(ServerError):
    status = ResponseCode.HANDLE_INIT_ERROR
    message = ResponseCode.message(status)


class HandleWorkError(ServerError):
    status = ResponseCode.HANDLE_WORK_ERROR
    message = ResponseCode.message(status)


class FeatureProcessError(ServerError):
    status = ResponseCode.FEATURE_PROCESS_ERROR
    message = ResponseCode.message(status)


class FeatureConfigError(ServerError):
    status = ResponseCode.WRONG_FEATURE_CONFIG
    message = ResponseCode.message(status)


class RelevanceFeatureConfigError(ServerError):
    status = ResponseCode.RELEVANCE_FEATURE_CONFIG_ERROR
    message = ResponseCode.message(status)


class CommonFeatureConfigError(ServerError):
    status = ResponseCode.COMMON_FEATURE_CONFIG_ERROR
    message = ResponseCode.message(status)


class ShuntFeatureConfigError(ServerError):
    status = ResponseCode.SHUNT_FEATURE_CONFIG_ERROR
    message = ResponseCode.message(status)


class AsyncCallInterfaceError(ServerError):
    status = ResponseCode.ASYNC_CALL_INTERFACE_ERROR
    message = ResponseCode.message(status)


class DoingAsyncCallInterface(ServerError):
    status = ResponseCode.DOING_ASYNC_CALL_INTERFACE
    message = ResponseCode.message(status)


class AsyncCallInterfaceTimeout(ServerError):
    status = ResponseCode.ASYNC_CALL_INTERFACE_TIMEOUT
    message = ResponseCode.message(status)


class InterfaceInfoTableConfigError(ServerError):
    status = ResponseCode.INTERFACE_INFO_TABLE_CONFIG_ERROR
    message = ResponseCode.message(status)
