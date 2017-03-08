# -*- coding:utf-8 -*-

import logging
import os

from django.utils.module_loading import import_string

from studio.feature_comment_handle.featrue_process import FeatureProcess

logger = logging.getLogger('apps.featuretest')


def test(data):
    for feature_name, datas_list in data.items():
        for datas in datas_list:
            res = datas.pop('res')
            feature_obj = FeatureProcess(feature_name, datas)
            result = feature_obj.run()
            print result
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
        path = os.path.dirname(os.path.dirname(__file__)) + '/feature_test'
        file_list = os.listdir(path)
        tests = {}
        for file in file_list:
            if file.endswith('_test.py'):
                test = import_string('studio.feature_test.%s.data' % file[:-3])
                tests.update(test)
        return tests


    test_datas = load_feature_test()
    test_datas = {'education_tz': test_datas['education_tz']}
    test(test_datas)
