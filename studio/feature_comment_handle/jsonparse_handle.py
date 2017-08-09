# -*- coding:utf-8 -*-

import logging

from jsonpath_rw_ext import parse
from exec_chain_handle import func_exec_chain
from vendor.errors.feature import FeatureProcessError

logger = logging.getLogger('apps.common')


class JSONPathParser(object):
    def parsex(self, data, json_path_list):
        """
        Args:
            :param data 实际的数据
            :param json_path_list  json path的列表
                  [("path的key值", "path的路径，如$..content.age",
                  "断言链，如f_assert_not_null->f_assert_must_int->f_assert_length_must(10)")],

        Returns:
            :return [("path的key值", "path路径", "断言链", "获取到的值")]，比如：
                        [
                            ("api_age", "$..content.age", "f_assert_not_null->f_assert_must_digit->f_assert_must_between(0,100)", [40]),
                        ]

        Raises:
            FeatureJSONParseError  自定义的特征JSONPath处理异常，继承自FeatureProcessError
        """
        json_path_value = []
        for key, path, assert_chain in json_path_list:
            path_expr = parse(path)
            value = path_expr.find(data)
            result = []
            for val in value:
                result.append(val.value)
            if not result:
                logger.error('(%s, %s) jsonpath value is null ' % (key, path))
                result = []
            else:
                logger.info('(%s, %s) jsonpath value is %s ' % (key, path, result))
            result = func_exec_chain(result, assert_chain)

            json_path_value.append((key, path, assert_chain, result))

        return json_path_value


if __name__ == '__main__':
    data = {
        'content': {
            'constellation': '水瓶座',
            'age': 10,
            'home_address': '江西 - 九江',
            'sex': '男',
        },
    }
    json_path_list = [(
        "age", "$..content.age",
        "f_assert_not_null->f_assert_must_digit"
    )]

    jparse = JSONPathParser()
    jparse.parsex(data, json_path_list)
