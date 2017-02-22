# -*- coding:utf-8 -*-

from featrue_process import FeatureProcess

data = {
        'content': {
            'constellation': '水瓶座',
            'age': 10,
            'home_address': '江西 - 九江',
            'sex': '男',
        },
    }


def test():
    fecture_obj = FeatureProcess('age', data)
    result = fecture_obj.run()
    print result


if __name__ == '__main__':
    test()
