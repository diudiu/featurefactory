# # -*- coding:utf-8 -*-
# import json
# import requests
# import os
# import sys
# import re
# from importlib import import_module
# from bson import ObjectId
# from init_dataocean_data import random_str
# import django
#
# home_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# sys.path.append(home_path)
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'featurefactory.settings')
# django.setup()
#
# from apps.common.mongo_handle import MongoBase
# from apps.common.dispatcher import process_dispatch, data_get_dispatch
# from vendor.utils.cache import RedisX
# from apps.datasource.models import DsInterfaceInfo
#
# CACHE_BASE_NAME = 'cache_base'
#
# headers = {
#     "Content-type": "application/json; charset=utf-8",
# }
#
#
# def get_args():
#     args = DsInterfaceInfo.objects.values('data_identity', 'must_data')
#     tmp_args = {}
#     for i in args:
#         data_identity = i['data_identity']
#         must_data = eval(i['must_data'])
#         tmp = {}
#         for k in must_data:
#             try:
#                 name = re.match(r'%\((\w+)\)s', must_data[k]).groups(1)[0]
#                 tmp[k] = name
#             except Exception as e:
#                 print "ERROR-- fic_interface_info table  %s {'%s':'%s'}" % (data_identity, k, must_data[k])
#         tmp_args[data_identity] = tmp
#     # print tmp_args
#     return tmp_args
#
#
# def main(url):
#     args_name = get_args()
#     path = os.path.dirname(__file__)
#     files = os.listdir(path)
#     for i in files:
#         if i.startswith('dataocean_test_data'):
#             f = import_module(i.split('.')[0])
#             data = f.data
#             print data
#             for fecture, v in data.items():
#                 tmp_lists = []
#                 data_identify = v['data_identify']
#                 lists = v['req_res']
#                 for req_res in lists:
#                     tmp = {}
#                     req_data = req_res['req_data']
#                     req_args = args_name.get(data_identify, '')
#                     fecture_value = req_res['fecture_value']
#                     if not req_args:
#                         print "ERROR-- %s file don't get  data_identify: %s args map" % (i, data_identify)
#                     else:
#                         for j in req_args:
#                             tmp[req_args[j]] = req_data.get(j, '')
#                             if not tmp[req_args[j]]:
#                                 print "ERROR-- %s file miss data_identify:%s args dataocean:%s " \
#                                       "map fecturefactory:%s value" % (i, data_identify, j, req_args[j])
#                                 break
#                         tmp_lists.append(
#                             [{'target_field_name': fecture, 'data_identity': data_identify,
#                               'arguments': tmp}, {'fecture_value': fecture_value}])
#                 if tmp_lists:
#                     # print 'dataocean-data--', tmp_lists
#                     for i, fecture_value in tmp_lists:
#                         tmp = data_get_dispatch_test(url, [i])
#                         fecture_res = {'fecture_value': ''}
#                         if tmp:
#                             fecture_res = process_dispatch(tmp)
#                         # print fecture_res
#                         # print fecture_res[i['target_field_name']],fecture_value['fecture_value']
#                         if fecture_res[i['target_field_name']] != fecture_value['fecture_value']:
#                             print 'ERROR--- fecture: %s data: %s handle except' % (i['target_field_name'], i)
#
#
# def data_get_dispatch_test(url, data):
#     url += '/feature/data_get_dispatch/'
#
#     base_data = {'apply_id': random_str(),
#                  'useful_args': []}
#     base_data.update({'useful_args': data})
#     print 'dataocean-req---', base_data
#     res = requests.post(url, headers=headers, data=json.dumps(base_data))
#
#     cache_base = MongoBase(collection_name=CACHE_BASE_NAME)
#     red = RedisX()
#
#     for i in base_data["useful_args"]:
#         data_identity = i["data_identity"]
#         redis_key = base_data["apply_id"] + ":" + data_identity
#         value = red.get(redis_key)
#         print "redis----%s" % value
#         if value:
#             query = {'_id': ObjectId(value)}
#             mon_value = cache_base.search(query)
#             print "mongo-----%s" % mon_value
#             if not mon_value:
#                 print "%s mongo_cache ------error" % data_identity
#
#         else:
#             print "%s redis_cache ------error" % data_identity
#             print "%s mongo_cache ------error" % data_identity
#     tmp = []
#     if res.status_code == 200:
#         content = json.loads(res.content)
#         print 'dataocean_res---', content
#         for i in content:
#             for data_identify, value in i.items():
#                 if value['status'] == 1:
#                     res = value['res_data']
#                     if res['status'] == 1:
#                         data_ocean_res = json.loads(res['res_data'])
#                         if data_ocean_res['result'] in ('00', '11', '22'):
#                             tmp.append({data_identify: data_ocean_res})
#     else:
#         print "ERROR--- %s dataocean reture error" % data
#     # print tmp
#     return tmp
#
#
# def process_dispatch_test(url, tmp):
#     url += '/feature/process_dispatch/'
#     # print url
#     # original_data_list = [
#     #     {'tianwang_gray': {'time': 'Sun Jan 22 14:53:13 2017'},
#     #      'tianyan_black': {'time': 'Sun Jan 22 14:53:13 2017'},
#     #      'tianwang_multi_loan': {'time': 'Sun Jan 22 14:53:13 2017'},
#     #      'tianwang_black': {'time': 'Sun Jan 22 14:53:13 2017'}
#     #      }
#     # ]
#     original_data_list = tmp
#     res = requests.post(url, headers=headers, data=json.dumps(original_data_list))
#     print res.content
#
#
# if __name__ == '__main__':
#     data = [{'target_field_name': 'is_court_zhixing', 'data_identity': 'court_zhixing_a_s',
#              'arguments': {'card_id': '433031196210056032', 'name': '吴永荣'}},
#             {'target_field_name': 'mobile_online_time', 'data_identity': 'unicome_mobile_online_time_s',
#              'arguments': {'mobile': '15538810634'}},
#             {'target_field_name': 'is_net_black', 'data_identity': 'net_black_a_s',
#              'arguments': {'card_id': '612501198407110021', 'name': '徐娟'}},
#             ]
#     # url = 'http://127.0.0.1:8070'
#     url = 'http://192.168.1.196:8070'
#     main(url)
#     # tmp = data_get_dispatch_test(url, data)
#     # process_dispatch_test(url, tmp)
#     # fecture_res = process_dispatch(tmp)
#     # print fecture_res
