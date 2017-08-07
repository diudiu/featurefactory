# -*- coding:utf-8 -*-

from featrue_process import FeatureProcess



def test():
    for feature_name, datas in data.items():
        feature_obj = FeatureProcess(feature_name, datas)
        result = feature_obj.run()
        print result


if __name__ == '__main__':
    # data = {'now_work_time': data['now_work_time']}
    test()
