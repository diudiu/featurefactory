# -*- coding:utf-8 -*-

import logging
import os
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')
from django.utils.module_loading import import_string
from studio.feature_comment_handle.featrue_process import FeatureProcess

logger = logging.getLogger('apps.featuretest')

case_name = sys.argv[2] + '_test'
case_path = os.path.join(os.path.dirname(__file__), case_name + '.py')

data = import_string('studio.feature_test.%s.data' % case_name)


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
    test(data)
