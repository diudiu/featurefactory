# -*- coding:utf-8 -*-
import os, sys

home_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(home_path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'featurefactory.settings')
import django
django.setup()
from django.utils.module_loading import import_string
from apps.etl.models import FeatureProcess


def load_feature_config():
    path = os.path.dirname(__file__)
    file_list = os.listdir(path)
    config = {}
    for file in file_list:
        if file.endswith('_config.py'):
            title = 'studio.feature_comment_handle.%s.config' % file[:-3]
            configs = import_string(title)
            config.update(configs)
    return config


def config_to_mysql():
    configs = load_feature_config()
    for name, config in configs.items():
        feature_name = config['feature_name']
        feature_data_type = config['feature_data_type']
        default_value = config['default_value']
        json_path_list = config['json_path_list']
        f_map_and_filter_chain = config['f_map_and_filter_chain']
        reduce_chain = config['reduce_chain']
        l_map_and_filter_chain = config['l_map_and_filter_chain']
        if FeatureProcess.objects.filter(feature_name=feature_name).count():
            FeatureProcess.objects.filter(feature_name=feature_name).update(
                feature_data_type=feature_data_type,
                default_value=default_value,
                json_path_list=json_path_list,
                f_map_and_filter_chain=f_map_and_filter_chain,
                reduce_chain=reduce_chain,
                l_map_and_filter_chain=l_map_and_filter_chain
            )
        else:
            FeatureProcess(
                feature_name=feature_name,
                feature_data_type=feature_data_type,
                default_value=default_value,
                json_path_list=json_path_list,
                f_map_and_filter_chain=f_map_and_filter_chain,
                reduce_chain=reduce_chain,
                l_map_and_filter_chain=l_map_and_filter_chain
            ).save()

if __name__ == '__main__':
    config_to_mysql()