# -*- coding:utf-8 -*-

import logging
import os
import importlib

from featrue_process import FeatureProcess

logger = logging.getLogger('apps.fecturetest')


def test(data):
    for feature_name, datas_list in data.items():
        for datas in datas_list:
            res = datas.pop('res')
            fecture_obj = FeatureProcess(feature_name, datas)
            result = fecture_obj.run()
            if result:
                result = result[feature_name]
                if result != res:
                    logger.error(
                        '\n************%s************\n data=%s\n output:%s expect: %s 测试失败\n******************'
                        % (feature_name, datas, result, res))
                else:
                    logger.info('\n************%s************\n data=%s\n output:%s expect: %s 测试通过\n******************'
                                % (feature_name, datas, result, res))
            else:
                logger.error(
                    '\n************%s************\n%s config not find or config error!!! 测试失败\n******************'
                    % (feature_name, feature_name))


if __name__ == '__main__':
    def load_feature_test():
        path = os.path.dirname(os.path.dirname(__file__)) + '/fecture_test'
        file_list = os.listdir(path)
        tests = {}
        for file in file_list:
            if file.endswith('_test.py'):
                test = importlib.import_module('studio.fecture_test.' + file[:-3])

                test = test.data
                tests.update(test)
        return tests


    test_datas = load_feature_test()
    data = {'mobile': test_datas['mobile']}
    test(data)
