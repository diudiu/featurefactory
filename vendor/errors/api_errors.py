# -*- coding: utf-8 -*-

from vendor.errors.common import ServerError

from vendor.messages.response_code import ResponseCode


# E01 请求类型错误
class RequestTypeError(AttributeError):
    status = ResponseCode.REQUEST_TYPE_ERROR,
    message = ResponseCode.message(status),


# E02 用户身份不合法
class UserIdentityError(ServerError):
    status = ResponseCode.USERS_IDENTIFICATION_ERROR,
    message = ResponseCode.message(status),


# E03 数据包解密失败  加密方式错误
class EncryptError(ServerError):
    status = ResponseCode.INCOME_ENCRYPT_ERROR,
    message = ResponseCode.message(status),


# E04 传入参数缺失 apply_id
class GetApplyIdError(ServerError):
    status = ResponseCode.MISSING_APPLY_ID,
    message = ResponseCode.message(status),


# E05 传入参数缺失 res_keys
class GetResKeysError(ServerError):
    status = ResponseCode.MISSING_RES_KEYS,
    message = ResponseCode.message(status),


# E06 传入参数缺失 arguments
class GetArgumentsError(ServerError):
    status = ResponseCode.MISSING_ARGUMENTS,
    message = ResponseCode.message(status),


# E07 res_keys 与 arguments 对应关系错误, 参数不足以获取所有res_keys
class ArgumentsAvailableError(ServerError):
    status = ResponseCode.ARGUMENTS_UNAVAILABLE,
    message = ResponseCode.message(status),
