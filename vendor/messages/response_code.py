# -*- coding: utf-8 -*-


class ResponseCode(object):
    """
        define for various code for response status
    """
    FAILED = 0
    SUCCESS = 1
    FEATURE_SUCCESS = 1

    SERVER_BUSY = 5000
    REQUEST_TYPE_ERROR = 30001
    USERS_IDENTIFICATION_ERROR = 30002
    INCOME_ENCRYPT_ERROR = 30003
    ARGUMENTS_UNAVAILABLE = 30004
    MISSING_APPLY_ID = 30010
    MISSING_RES_KEYS = 30011
    MISSING_ARGUMENTS = 30012
    MISSING_CALLBACK_URL = 30013
    MISSING_PROPOSER_ID = 30014
    MISSING_CLIENT_CODE = 30015

    DATABASE_ERROR = 40101
    NO_PORTRAIT_DATA = 40201

    UNAVAILABLE_CLIENT_CODE = 50001
    MISSING_JUDGE_TYPE = 50002
    JUDGE_INIT_ERROR = 50003
    JUDGE_WORK_ERROR = 50004
    JUDGE_RET_ERROR = 50005

    FEATURE_UNFOUND = 50010
    DATAIDENTITY_UNFOUND = 50011
    JUNKMAN_INIT_ERROR = 50012
    JUNKMAN_WORK_ERROR = 50013

    HANDLE_INIT_ERROR = 50020
    HANDLE_WORK_ERROR = 50021
    WRONG_FEATURE_CONFIG = 50022

    FEATURE_PROCESS_ERROR = 50014

    ORIGIN_DATA_GET_ERROR = 60001
    ORIGIN_DATA_GET_PARMS_MISS = 60002
    RELEVANCE_FEATURE_CONFIG_ERROR = 60003
    COMMON_FEATURE_CONFIG_ERROR = 60004
    SHUNT_FEATURE_CONFIG_ERROR = 60004
    ASYNC_CALL_INTERFACE_ERROR = 60005
    DOING_ASYNC_CALL_INTERFACE = 60006
    ASYNC_CALL_INTERFACE_TIMEOUT = 60006
    INTERFACE_INFO_TABLE_CONFIG_ERROR = 60007

    RESPONSE_MESSAGE = {
        FAILED:                         u"操作失败",
        SUCCESS:                        u"操作成功",

        SERVER_BUSY:                    u"服务器繁忙，请稍后重试！",
        REQUEST_TYPE_ERROR:             u"请求方式错误, 请求数据应为JSON  请求方式应为HTTP-POST",
        USERS_IDENTIFICATION_ERROR:     u"用户身份不合法 client_code 错误或不存在",
        INCOME_ENCRYPT_ERROR:           u"数据解密错误, 传入参数加密错误",
        ARGUMENTS_UNAVAILABLE:          u'传入参数不足以获取所有目标特征, 请检查参数列表',
        MISSING_APPLY_ID:               u"传入数据内容缺失 apply_id",
        MISSING_RES_KEYS:               u"传入数据内容缺失 res_keys",
        MISSING_ARGUMENTS:              u"受信人输入数据缺失",
        MISSING_CALLBACK_URL:           u"传入数据内容缺失 callback_url",
        MISSING_PROPOSER_ID:            u"proposer_id 查询获取失败",
        MISSING_CLIENT_CODE:            u"传入数据内容缺失 client_code",

        DATABASE_ERROR:                 u"数据库服务错误",
        NO_PORTRAIT_DATA:               u"portrait_base中无此用户预授信数据",

        UNAVAILABLE_CLIENT_CODE:        u"client_code 无效 不存在的客户",
        FEATURE_SUCCESS:                u"特征处理成功",
        MISSING_JUDGE_TYPE:             u"没有匹配该客户的judger逻辑",
        JUDGE_INIT_ERROR:               u"检查方法类内部错误: 无法初始化",
        JUDGE_WORK_ERROR:               u"检查方法执行错误: 空的执行结果",
        JUDGE_RET_ERROR:                u"检车方法执行返回结果有缺失: 空的apply_Id 或 空的 useful_args",

        FEATURE_UNFOUND:                u"无该特征名的配置信息, FeatureFieldRel",
        DATAIDENTITY_UNFOUND:           u"无该数据源标识配置信息, DsInterfaceInfo",
        JUNKMAN_INIT_ERROR:             u"原始数据获取方法内部错误: 无法初始化",
        JUNKMAN_WORK_ERROR:             u"原始数据获取方法执行作物: 空的执行结果",

        HANDLE_INIT_ERROR:              u"特征处理方法内部错误: 无法初始化",
        HANDLE_WORK_ERROR:              u"特征数理方法执行错误: 空的执行结果",
        WRONG_FEATURE_CONFIG:           u"特征处理方法配置错误, 特征名称与期待不同",

        FEATURE_PROCESS_ERROR:          u"特征加工计算出现错误",

        ORIGIN_DATA_GET_ERROR:          u"原始数据获取失败",
        ORIGIN_DATA_GET_PARMS_MISS:     u"获取原始数据参数丢失",
        RELEVANCE_FEATURE_CONFIG_ERROR: u'依赖特征表配置错误',
        COMMON_FEATURE_CONFIG_ERROR:    u'通用配置表错误',
        SHUNT_FEATURE_CONFIG_ERROR:     u'分流配置表错误',
        ASYNC_CALL_INTERFACE_ERROR:               u'异步调用数据源错误',
        DOING_ASYNC_CALL_INTERFACE:     u'启动异步调用数据源',
        ASYNC_CALL_INTERFACE_TIMEOUT:   u'异步调用数据源超时',
        INTERFACE_INFO_TABLE_CONFIG_ERROR: u'接口配置表must_data配置错误'
    }

    @classmethod
    def message(cls, status):
        return cls.RESPONSE_MESSAGE.get(status, u'')
