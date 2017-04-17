# -*- coding:utf-8 -*-
"""
    Copyright (c) 2013-2016 SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/22
    Change Activity:

        _==/          i     i           \==_
      /XX/            |\___/|            \XX\
    /XXXX\            |XXXXX|            /XXXX\
   |XXXXXX\_         _XXXXXXX_         _/XXXXXX|
  XXXXXXXXXXXxxxxxxxXXXXXXXXXXXxxxxxxxXXXXXXXXXXX
 |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
 |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
  XXXXXX/^^^^^\XXXXXXXXXXXXXXXXXXXXX/^^^^^\XXXXXX
   |XXX|       \XXX/^^\XXXXX/^^\XXX/       |XXX|
     \XX\       \X/    \XXX/    \X/       /XX/
        "\       "      \X/      "       /"
"""

import json
import logging
import datetime
import re

from braces.views import CsrfExemptMixin
from django.http.response import HttpResponse
from django.views.generic import View

from apps.etl.models import *
from apps.common.models import FeatureCodeMapping
from apps.datasource.models import *
from vendor.utils.pagination import ExtPaginator
from vendor.utils.commons import json_response
from studio.feature_comment_handle.exec_chain_handle import func_exec_chain
from studio.feature_comment_handle.jsonparse_handle import JSONPathParser
from vendor.utils.defaults import *

logger = logging.getLogger('apps.interface')


class FeatureConfig(CsrfExemptMixin, View):
    def get(self, request, featurename, page, *args, **kwargs):
        """获取特征基础配置信息"""
        data = {
            'status': 1,
            'message': 'success'
        }
        try:
            current_page = page
            page_size = 10
            if featurename == 'all':
                feature_config_obj = FeatureConf.objects.values()
            else:
                feature_config_obj = FeatureConf.objects.filter(feature_name=featurename).values()
            feature_config_count = feature_config_obj.count()
            paginator = ExtPaginator(list(feature_config_obj), page_size, feature_config_count)
            object_list = paginator.page(current_page)
            map(lambda x: [
                x.update({"created_on": x["created_on"].strftime('%Y-%m-%d %H:%M:%S') if x["created_on"] else ''}),
                x.update({"updated_on": x["updated_on"].strftime('%Y-%m-%d %H:%M:%S') if x["updated_on"] else ''}),
                x.update(
                    {"feature_select_value": x["feature_select_value"] if x["feature_select_value"] else ''}),
                x.update({"feature_type_desc": FeatureType.objects.get(pk=x["feature_type_id"]).feature_type_desc if x[
                    "feature_type_id"] else ''}),
                x.update(
                    {"feature_rule_type_desc": FeatureRuleType.objects.get(
                        pk=x["feature_rule_type_id"]).feature_type_desc if x[
                        "feature_rule_type_id"] else ''}),
                x.update(
                    {"feature_card_type_desc": FeatureCardType.objects.get(
                        pk=x["feature_card_type_id"]).feature_type_desc if x[
                        "feature_card_type_id"] else ''}),
            ], object_list)

            page_num = paginator.num_pages
            page_range = paginator.page_range

            res_data = dict(
                total_count=feature_config_count,
                page_num=page_num,
                current_page=current_page,
                config_list=list(object_list),
                page_range=page_range
            )

            data.update({"res_data": res_data})
        except Exception as e:
            logger.error(e.message)
            data = {
                'status': '0',
                'message': e.message
            }

        return json_response(data)

    def put(self, request, item, featureid, *args, **kwargs):
        """更新特征基础配置信息"""
        data = {
            'status': 1,
            'message': 'success'
        }
        try:
            body = json.loads(request.body)
            logger.info("update feature config request data=%s", body)
            updated_on = datetime.datetime.now()
            if item == 'feature_info':
                feature_name_cn = body.get('feature_name_cn')
                if not feature_name_cn:
                    raise Exception(u'特征中文名不能为空')

                feature_type = body.get('feature_type_id')
                feature_rule_type = body.get('feature_rule_type_id')
                feature_card_type = body.get('feature_card_type_id')
                feature_type = FeatureType.objects.get(pk=feature_type) if feature_type else None
                feature_rule_type = FeatureRuleType.objects.get(pk=feature_rule_type) if feature_rule_type else None
                feature_card_type = FeatureCardType.objects.get(pk=feature_card_type) if feature_card_type else None
                FeatureConf.objects.filter(pk=int(featureid)).update(
                    feature_name=body.get('feature_name'),
                    feature_name_cn=body.get('feature_name_cn'),
                    feature_type=feature_type,
                    feature_rule_type=feature_rule_type,
                    feature_card_type=feature_card_type,
                    feature_select_value=body.get('feature_select_value'),
                    updated_on=updated_on,
                    is_delete=body.get('is_delete')
                )
            elif item == 'feature_source':
                data_identity = body.get('data_identity')
                if not data_identity:
                    raise Exception(u'特征数据源不能为空！')
                FeatureConf.objects.filter(pk=int(featureid)).update(
                    collect_type=body.get('collect_type'),
                    data_identity=body.get('data_identity'),
                    updated_on=updated_on
                )
            else:
                raise Exception('url error')
        except Exception as e:
            logger.error(e.message)
            data = {
                'status': '0',
                'message': e.message
            }

        return json_response(data)

    def post(self, request, item, *args, **kwargs):
        """添加特征基本信息配置"""
        data = {
            'status': 1,
            'message': 'success'
        }
        try:
            body = json.loads(request.body)
            logger.info("update feature config request data=%s", body)
            created_on = datetime.datetime.now()
            if item == 'feature_info':
                feature_name = body.get('feature_name')
                feature_name_cn = body.get('feature_name_cn')
                if not feature_name_cn or not feature_name_cn:
                    raise Exception(u'特征名和特征中文名不能为空！')
                count = FeatureConf.objects.filter(feature_name=feature_name)
                if count:
                    raise Exception('%s already exists!' % feature_name)
                feature_type = body.get('feature_type_id')
                feature_rule_type = body.get('feature_rule_type_id')
                feature_card_type = body.get('feature_card_type_id')
                feature_type = FeatureType.objects.get(pk=feature_type) if feature_type else None
                feature_rule_type = FeatureRuleType.objects.get(pk=feature_rule_type) if feature_rule_type else None
                feature_card_type = FeatureCardType.objects.get(pk=feature_card_type) if feature_card_type else None
                FeatureConf(
                    feature_name=body.get('feature_name'),
                    feature_name_cn=body.get('feature_name_cn'),
                    feature_type=feature_type,
                    feature_rule_type=feature_rule_type,
                    feature_card_type=feature_card_type,
                    feature_select_value=body.get('feature_select_value'),
                    is_delete=body.get('is_delete'),
                    updated_on=created_on,
                    created_on=created_on
                ).save()
            else:
                raise Exception('url error')
        except Exception as e:
            logger.error(e.message)
            data = {
                'status': '0',
                'message': e.message
            }
        return json_response(data)


class FeatureShuntConfig(CsrfExemptMixin, View):
    def get(self, request, featurename, page, *args, **kwargs):
        """获取分流特征基础配置信息"""
        data = {
            'status': 1,
            'message': 'success'
        }
        try:
            current_page = page
            page_size = 500
            if featurename == 'all':
                feature_config_obj = FeatureShuntConf.objects.values()
            else:
                feature_config_obj = FeatureShuntConf.objects.filter(feature_name=featurename).values()
            feature_config_count = feature_config_obj.count()

            paginator = ExtPaginator(list(feature_config_obj), page_size, feature_config_count)
            object_list = paginator.page(current_page)
            map(lambda x: [
                x.update({"created_on": x["created_on"].strftime('%Y-%m-%d %H:%M:%S') if x["created_on"] else ''}),
                x.update({"updated_on": x["updated_on"].strftime('%Y-%m-%d %H:%M:%S') if x["updated_on"] else ''}),
                x.update({"shunt_value": x["shunt_value"] if x["shunt_value"] else ''}),
            ], object_list)

            page_num = paginator.num_pages
            page_range = paginator.page_range

            res_data = dict(
                total_count=feature_config_count,
                page_num=page_num,
                current_page=current_page,
                config_list=list(object_list),
                page_range=page_range
            )

            data.update({"res_data": res_data})
        except Exception as e:
            logger.error(e.message)
            data = {
                'status': '0',
                'message': e.message
            }

        return json_response(data)

    def put(self, request, featureid, *args, **kwargs):
        """更新分流特征基础配置信息"""
        data = {
            'status': 1,
            'message': 'success'
        }

        try:
            body = json.loads(request.body)
            logger.info("update shunt feature config request data=%s", body)
            feature_name = body.get('feature_name')
            shunt_key = body.get('shunt_key')
            shunt_type = body.get('shunt_type')
            shunt_value = body.get('shunt_value')
            data_identity = body.get('data_identity')
            is_delete = body.get('is_delete')
            if not (feature_name and shunt_key and data_identity and shunt_type and shunt_value):
                raise Exception("all values don't is null !")

            if not isinstance(eval(body['shunt_value']), tuple):
                raise Exception(u'数据源适应范围必须为元组类型!')
            updated_on = datetime.datetime.now()
            FeatureShuntConf.objects.filter(pk=int(featureid)).update(
                feature_name=feature_name,
                shunt_key=shunt_key,
                data_identity=data_identity,
                shunt_type=shunt_type,
                shunt_value=shunt_value,
                updated_on=updated_on,
                is_delete=is_delete
            )
        except Exception as e:
            logger.error(e.message)
            data = {
                'status': '0',
                'message': e.message
            }

        return json_response(data)

    def post(self, request, *args, **kwargs):
        """添加分流特征基本信息配置"""
        data = {
            'status': 1,
            'message': 'success'
        }
        try:
            body = json.loads(request.body)
            logger.info("add shunt feature config request data=%s", body)
            feature_name = body.get('feature_name')
            shunt_key = body.get('shunt_key')
            shunt_type = body.get('shunt_type')
            shunt_value = body.get('shunt_value')
            data_identity = body.get('data_identity')
            is_delete = body.get('is_delete')
            if not (feature_name and shunt_key and data_identity and shunt_type and shunt_value):
                raise Exception("all values don't is null !")

            if not isinstance(eval(body['shunt_value']), (tuple, list)):
                raise Exception(u'数据源适应范围必须为元组类型!')
            if FeatureShuntConf.objects.filter(feature_name=feature_name).count():
                raise Exception('this feature_name already exists!')
            FeatureShuntConf(
                feature_name=feature_name,
                shunt_key=shunt_key,
                data_identity=data_identity,
                shunt_type=shunt_type,
                shunt_value=tuple(eval(shunt_value)),
                is_delete=is_delete
            ).save()
        except Exception as e:
            logger.error(e.message)
            data = {
                'status': '0',
                'message': e.message
            }

        return json_response(data)


class FeatureRelevanceConfig(CsrfExemptMixin, View):
    def get(self, request, featurename, page, *args, **kwargs):
        """获取依赖特征基础配置信息"""
        data = {
            'status': 1,
            'message': 'success'
        }
        try:
            current_page = page
            page_size = 100
            if featurename == 'all':
                feature_config_obj = FeatureRelevanceConf.objects.values()
            else:
                feature_config_obj = FeatureRelevanceConf.objects.filter(
                    feature_name=featurename
                ).values()
            feature_config_count = feature_config_obj.count()

            paginator = ExtPaginator(list(feature_config_obj), page_size, feature_config_count)
            object_list = paginator.page(current_page)
            map(lambda x: [
                x.update({"created_on": x["created_on"].strftime('%Y-%m-%d %H:%M:%S') if x["created_on"] else ''}),
                x.update({"updated_on": x["updated_on"].strftime('%Y-%m-%d %H:%M:%S') if x["updated_on"] else ''}),
            ], object_list)

            page_num = paginator.num_pages
            page_range = paginator.page_range

            res_data = dict(
                total_count=feature_config_count,
                page_num=page_num,
                current_page=current_page,
                config_list=list(object_list),
                page_range=page_range
            )

            data.update({"res_data": res_data})
        except Exception as e:
            logger.error(e.message)
            data = {
                'status': '0',
                'message': e.message
            }

        return json_response(data)

    def put(self, request, featureid, *args, **kwargs):
        """更新依赖特征基础配置信息"""
        data = {
            'status': 1,
            'message': 'success'
        }

        try:
            body = json.loads(request.body)
            logger.info("update relevance feature config request data=%s", body)
            feature_name = body['feature_name']
            depend_feature = body['depend_feature']
            data_identity = body['data_identity']
            is_delete = body['is_delete']
            updated_on = datetime.datetime.now()

            FeatureRelevanceConf.objects.filter(pk=int(featureid)).update(
                feature_name=feature_name,
                depend_feature=depend_feature,
                data_identity=data_identity,
                updated_on=updated_on,
                is_delete=is_delete
            )
        except Exception as e:
            logger.error(e.message)
            data = {
                'status': '0',
                'message': e.message
            }

        return json_response(data)

    def post(self, request, *args, **kwargs):
        """添加依赖特征基本信息配置"""
        data = {
            'status': 1,
            'message': 'success'
        }
        try:
            path = request.path
            if 'check' in path:
                con = FeatureRelevanceConf.objects.filter(is_delete=False)
                for i in con:
                    if i.depend_feature:
                        depend_feature_list = i.depend_feature.split(',')
                        for j in depend_feature_list:
                            con = FeatureRelevanceConf.objects.filter(is_delete=False, feature_name=j).count()
                            if not con:
                                raise Exception("%s  dependent feature %s, %s is not available in relevance table !" % (
                                    i.feature_name, j, j))

            else:
                body = json.loads(request.body)
                logger.info("add shunt feature config request data=%s", body)
                feature_name = body['feature_name']
                depend_feature = body['depend_feature']
                data_identity = body['data_identity']
                is_delete = body['is_delete']
                updated_on = datetime.datetime.now()
                if FeatureRelevanceConf.objects.filter(feature_name=feature_name).count():
                    raise Exception('this feature_name already exists!')

                FeatureRelevanceConf(
                    feature_name=feature_name,
                    depend_feature=depend_feature,
                    data_identity=data_identity,
                    updated_on=updated_on,
                    is_delete=is_delete
                ).save()
        except Exception as e:
            logger.error(e.message)
            data = {
                'status': '0',
                'message': e.message
            }

        return json_response(data)


class RemoteConfig(CsrfExemptMixin, View):
    def get(self, request, data_identity, page, *args, **kwargs):
        """获取数据源基础配置信息"""
        data = {
            'status': 1,
            'message': 'success'
        }
        try:
            current_page = page
            page_size = 100
            if data_identity == 'all':
                data_identity_obj = DsInterfaceInfo.objects.values()
            else:
                data_identity_obj = DsInterfaceInfo.objects.filter(
                    data_identity=data_identity
                ).values()
            data_identity_count = data_identity_obj.count()

            paginator = ExtPaginator(list(data_identity_obj), page_size, data_identity_count)
            object_list = paginator.page(current_page)
            map(lambda x: [
                x.update({"created_on": x["created_on"].strftime('%Y-%m-%d %H:%M:%S') if x["created_on"] else ''}),
                x.update({"updated_on": x["updated_on"].strftime('%Y-%m-%d %H:%M:%S') if x["updated_on"] else ''}),
                # x.update({"must_data": eval(x["must_data"]) if x["must_data"] else ''}),
            ], object_list)

            page_num = paginator.num_pages
            page_range = paginator.page_range

            res_data = dict(
                total_count=data_identity_count,
                page_num=page_num,
                current_page=current_page,
                config_list=list(object_list),
                page_range=page_range
            )
            data.update({"res_data": res_data})
        except Exception as e:
            logger.error(e.message)
            data = {
                'status': '0',
                'message': e.message
            }

        return json_response(data)

    def put(self, request, id, *args, **kwargs):
        """更新数据源基础配置信息"""
        data = {
            'status': 1,
            'message': 'success'
        }

        try:
            body = json.loads(request.body)
            logger.info("update datasource  config request data=%s", body)
            name = body['name']
            data_identity = body['data_identity']
            data_source = body['data_source_id']
            data_origin_type = body['data_origin_type']
            route = body['route']
            method = body['method']
            comment = body['comment']
            common_data = body['common_data']
            must_data = body['must_data']
            is_need_token = body['is_need_token']
            is_need_encrypt = body['is_need_encrypt']
            is_async = body['is_async']
            encrypt_type = body['encrypt_type']
            is_delete = body['is_delete']
            updated_on = datetime.datetime.now()

            DsInterfaceInfo.objects.filter(pk=int(id)).update(
                name=name,
                data_identity=data_identity,
                data_source=data_source,
                data_origin_type=data_origin_type,
                route=route,
                method=method,
                comment=comment,
                common_data=common_data,
                must_data=must_data,
                is_need_token=is_need_token,
                is_need_encrypt=is_need_encrypt,
                is_async=is_async,
                encrypt_type=encrypt_type,
                is_delete=is_delete,
                updated_on=updated_on
            )
        except Exception as e:
            logger.error(e.message)
            data = {
                'status': '0',
                'message': 'error'
            }

        return json_response(data)

    def post(self, request, *args, **kwargs):
        """添加数据源基本信息配置"""
        data = {'status': 1,
                'message': 'success'}
        try:
            body = json.loads(request.body)
            logger.info("add datasource  config request data=%s", body)
            name = body['name']
            data_identity = body['data_identity']
            data_source = int(body['data_source_id'])
            data_origin_type = body['data_origin_type']
            route = body['route']
            method = body['method']
            comment = body['comment']
            common_data = body['common_data']
            must_data = body['must_data']
            is_need_token = body['is_need_token']
            is_need_encrypt = body['is_need_encrypt']
            is_async = body['is_async']
            encrypt_type = body['encrypt_type']
            is_delete = body['is_delete']
            data_source = DataSourceInfo.objects.get(pk=data_source)
            DsInterfaceInfo(
                name=name,
                data_identity=data_identity,
                data_source=data_source,
                data_origin_type=data_origin_type,
                route=route,
                method=method,
                comment=comment,
                common_data=common_data,
                must_data=must_data,
                is_need_token=is_need_token,
                is_need_encrypt=is_need_encrypt,
                is_async=is_async,
                encrypt_type=encrypt_type,
                is_delete=is_delete,
            ).save()
        except Exception as e:
            logger.error(e.message)
            data = {
                'status': '0',
                'message': 'error'
            }

        return json_response(data)


class PreFieldInfoConfig(CsrfExemptMixin, View):
    def get(self, request, fieldname, page, *args, **kwargs):
        """获取数据源参数配置信息"""
        data = {
            'status': 1,
            'message': 'success'
        }
        try:
            current_page = page
            page_size = 100
            if fieldname == 'all':
                config_obj = PreFieldInfo.objects.values()
            else:
                config_obj = PreFieldInfo.objects.filter(field_name=fieldname).values()
            config_count = config_obj.count()
            paginator = ExtPaginator(list(config_obj), page_size, config_count)
            object_list = paginator.page(current_page)
            map(lambda x: [
                x.update({"created_on": x["created_on"].strftime('%Y-%m-%d %H:%M:%S') if x["created_on"] else ''}),
                x.update({"updated_on": x["updated_on"].strftime('%Y-%m-%d %H:%M:%S') if x["updated_on"] else ''}),
            ], object_list)

            page_num = paginator.num_pages
            page_range = paginator.page_range

            res_data = dict(
                total_count=config_count,
                page_num=page_num,
                current_page=current_page,
                config_list=list(object_list),
                page_range=page_range
            )

            data.update({"res_data": res_data})
        except Exception as e:
            logger.error(e.message)
            data = {
                'status': '0',
                'message': e.message
            }

        return json_response(data)

    def put(self, request, fieldid, *args, **kwargs):
        """更新数据源参数配置信息"""
        data = {
            'status': 1,
            'message': 'success'
        }

        try:
            body = json.loads(request.body)
            logger.info("update feature config request data=%s", body)
            updated_on = datetime.datetime.now()
            source = body.get('source')
            path = body.get('path')
            if not ((source and path) or (not source and not path)):
                raise Exception(u'参数来源和jsonpath只能同时为空或同时不为空!')
            PreFieldInfo.objects.filter(pk=int(fieldid)).update(
                field_name=body.get('field_name'),
                field_name_cn=body.get('field_name_cn'),
                source=body.get('source'),
                path=body.get('path'),
                updated_on=updated_on,
                is_delete=body.get('is_delete')
            )
        except Exception as e:
            logger.error(e.message)
            data = {
                'status': '0',
                'message': e.message
            }

        return json_response(data)

    def post(self, request, *args, **kwargs):
        """添加数据源参数配置信息"""
        data = {
            'status': 1,
            'message': 'success'
        }
        try:
            body = json.loads(request.body)
            logger.info("update feature config request data=%s", body)
            created_on = datetime.datetime.now()
            field_name = body.get('field_name')
            count = PreFieldInfo.objects.filter(field_name=field_name)
            source = body.get('source')
            path = body.get('path')
            if count:
                raise Exception('%s already exists' % field_name)
            if not ((source and path) or (not source and not path)):
                raise Exception(u'参数来源和jsonpath只能同时为空或同时不为空!')
            PreFieldInfo(
                field_name=field_name,
                field_name_cn=body.get('field_name_cn'),
                source=source,
                path=path,
                updated_on=created_on,
                created_on=created_on,
                is_delete=body.get('is_delete')
            ).save()

        except Exception as e:
            logger.error(e.message)
            data = {
                'status': '0',
                'message': e.message
            }
        return json_response(data)


class GetItemList(CsrfExemptMixin, View):
    def get(self, request, item, *args, **kwargs):
        """获取下拉列表信息"""
        try:
            if item == 'feature_name':
                data = FeatureConf.objects.filter(is_delete=False).values_list('id', 'feature_name').order_by(
                    'feature_name')
            elif item == 'feature_type':
                data = FeatureType.objects.filter(is_delete=False).values_list('id', 'feature_type_desc')
            elif item == 'feature_card_type':
                data = FeatureCardType.objects.filter(is_delete=False).values_list('id', 'feature_type_desc')
            elif item == 'feature_rule_type':
                data = FeatureRuleType.objects.filter(is_delete=False).values_list('id', 'feature_type_desc')
            elif item == 'args':
                data = PreFieldInfo.objects.filter(is_delete=False).values_list('id', 'field_name')
            elif item == 'funcname':
                data = FuncLibSource.objects.values_list('func_name', 'func_type', 'func_desc').order_by('func_type')
                tmp = {}
                for func_name, func_type, func_desc in data:
                    f = re.search("(.*)\\((.*)\\)", func_name)
                    f_name = f.group(1)
                    f_args = f.group(2)
                    f_s_args = ''
                    if len(f_args.split(',')) > 1:
                        f_s_args = f_args.split(',')[1]
                    tmp['%s' % f_name] = [func_name, f_s_args, func_type, func_desc]
                return json_response(tmp)

            elif item == 'data_identity':
                data = DsInterfaceInfo.objects.values_list('id', 'data_identity').order_by('data_identity')
            elif item == 'data_identity_args':
                data = DsInterfaceInfo.objects.values_list('id', 'data_identity', 'must_data').order_by('data_identity')
                tmp = []
                for id, data_identity, must_data in data:
                    if must_data:
                        args_list = []
                        for args in eval(must_data).values():
                            if re.search("%\\((.*)\\)s", args):
                                args_list.append(re.search("%\\((.*)\\)s", args).group(1))
                        tmp.append([id, "'%s':%s" % (data_identity, str(args_list))])
                data = tmp

            else:
                raise Exception('url error')
            data = {id: value for id, value in data}
        except Exception as e:
            logger.error(e.message)
            data = {
                'status': '0',
                'message': e.message
            }

        return json_response(data)


class FeatureProcessAPI(CsrfExemptMixin, View):
    def get(self, request, featurename, page, *args, **kwargs):
        """获取特征计算配置信息"""
        data = {
            'status': 1,
            'message': 'success'
        }
        try:
            current_page = page
            page_size = 10
            if featurename == 'all':
                feature_config_obj = FeatureProcess.objects.values()
            else:
                feature_config_obj = FeatureProcess.objects.filter(feature_name=featurename).values()
            feature_config_count = feature_config_obj.count()

            paginator = ExtPaginator(list(feature_config_obj), page_size, feature_config_count)
            object_list = paginator.page(current_page)
            page_num = paginator.num_pages
            page_range = paginator.page_range

            res_data = dict(
                total_count=feature_config_count,
                page_num=page_num,
                current_page=current_page,
                config_list=list(object_list),
                page_range=page_range
            )

            data.update({"res_data": res_data})
        except Exception as e:
            logger.error(e.message)
            data = {
                'status': '0',
                'message': e.message
            }

        return json_response(data)

    def post(self, request):
        path = request.path
        body = request.body
        datas = json.loads(body)
        if 'delete' in path:
            data = {
                'status': 1,
                'message': 'success'
            }
            try:
                feature_name = datas.get('feature_name')
                FeatureProcess.objects.filter(feature_name=feature_name).delete()
            except Exception as e:
                logger.error(e.message)
                data = {
                    'status': '0',
                    'message': e.message
                }
            return json_response(data)

        elif 'test' in path:
            origin_data = datas.get('origin_data', None)
            configx = datas.get('config', None)
            feature_name = 'feature_name'
            default_value = ''
            try:
                feature_name = configx.get('feature_name', 'null')
                json_path_list = configx.get('json_path_list', None)
                default_value = configx.get('default_value', None)
                if not (feature_name and default_value and json_path_list):
                    raise Exception("feature_name,default_value, json_path_list can't are null !")
                f_map_and_filter_chain = configx.get('f_map_and_filter_chain', None)
                reduce_chain = configx.get('reduce_chain', None)
                l_map_and_filter_chain = configx.get('l_map_and_filter_chain', None)
                json_path_parser = JSONPathParser()
                value_list = json_path_parser.parsex(origin_data, json_path_list)
                result = []
                for i in value_list:
                    result = result + i[3]
                if len(result) == 1 and isinstance(result[0], list):
                    result = result[0]
                if f_map_and_filter_chain:
                    result = func_exec_chain(result, f_map_and_filter_chain)
                if reduce_chain:
                    result = func_exec_chain(result, reduce_chain)
                if l_map_and_filter_chain:
                    result = func_exec_chain(result, l_map_and_filter_chain)
                res = {'message': 'success', 'result': {feature_name: result}}
            except Exception as e:
                res = {
                    'message': e.message,
                    'result': {feature_name: eval(default_value) if default_value else ''}
                }
            return json_response(res)

    def put(self, request):
        data = {
            'status': 1,
            'message': 'success'
        }
        try:
            body = request.body
            datas = json.loads(body, encoding='utf8')
            configx = datas.get('config', None)
            feature_name = configx.get('feature_name')
            if FeatureProcess.objects.filter(feature_name=feature_name).count():
                FeatureProcess.objects.filter(feature_name=feature_name).update(
                    feature_data_type=configx.get('feature_data_type'),
                    default_value=configx.get('default_value'),
                    json_path_list=configx.get('json_path_list'),
                    reduce_chain=configx.get('reduce_chain'),
                    f_map_and_filter_chain=configx.get('f_map_and_filter_chain'),
                    l_map_and_filter_chain=configx.get('l_map_and_filter_chain')
                )

            else:
                FeatureProcess(
                    feature_name=configx.get('feature_name'),
                    feature_data_type=configx.get('feature_data_type'),
                    default_value=configx.get('default_value'),
                    json_path_list=configx.get('json_path_list'),
                    reduce_chain=configx.get('reduce_chain'),
                    f_map_and_filter_chain=configx.get('f_map_and_filter_chain'),
                    l_map_and_filter_chain=configx.get('l_map_and_filter_chain')
                ).save()
        except Exception as e:
            logger.error(e.message)
            data = {
                'status': '0',
                'message': e.message
            }
        return json_response(data)


class TypeInfoConfig(CsrfExemptMixin, View):
    def get(self, request, item, page, *args, **kwargs):
        """获取规则类型、特征类型、打分卡类型 配置信息"""
        data = {
            'status': 1,
            'message': 'success'
        }
        try:
            current_page = page
            page_size = 100
            obj = FeatureType
            if item == 'feature_type':
                obj = FeatureType.objects.values()
            elif item == 'feature_card_type':
                obj = FeatureCardType.objects.values()
            elif item == 'feature_rule_type':
                obj = FeatureRuleType.objects.values()
            count = obj.count()

            paginator = ExtPaginator(list(obj), page_size, count)
            object_list = paginator.page(current_page)
            page_num = paginator.num_pages
            page_range = paginator.page_range

            res_data = dict(
                total_count=count,
                page_num=page_num,
                current_page=current_page,
                config_list=list(object_list),
                page_range=page_range
            )

            data.update({"res_data": res_data})
        except Exception as e:
            logger.error(e.message)
            data = {
                'status': '0',
                'message': e.message
            }

        return json_response(data)

    def put(self, request, item, id, *args, **kwargs):
        """更新类型配置信息"""
        data = {
            'status': 1,
            'message': 'success'
        }

        try:
            body = json.loads(request.body)
            logger.info("update type config request data=%s", body)
            is_delete = body.get('is_delete', 0)
            feature_type_desc = body.get('feature_type_desc', '')
            obj = FeatureType
            if not feature_type_desc:
                raise Exception(u'类型描述不能为空!')
            if item == 'feature_type':
                obj = FeatureType
            elif item == 'feature_card_type':
                obj = FeatureCardType
            elif item == 'feature_rule_type':
                obj = FeatureRuleType
            obj.objects.filter(pk=id).update(is_delete=is_delete, feature_type_desc=feature_type_desc)
        except Exception as e:
            logger.error(e.message)
            data = {
                'status': '0',
                'message': e.message
            }

        return json_response(data)

    def post(self, request, item, *args, **kwargs):
        """添加类型配置信息"""
        data = {
            'status': 1,
            'message': 'success'
        }
        try:
            body = json.loads(request.body)
            is_delete = body.get('is_delete', 0)
            feature_type_desc = body.get('feature_type_desc', '')
            obj = ''
            if not feature_type_desc:
                raise Exception(u'类型描述不能为空!')
            if item == 'feature_type':
                obj = FeatureType
            elif item == 'feature_card_type':
                obj = FeatureCardType
            elif item == 'feature_rule_type':
                obj = FeatureRuleType
            if obj.objects.filter(feature_type_desc=feature_type_desc).count():
                raise Exception(u"此类型已经存在！")
            obj(is_delete=is_delete, feature_type_desc=feature_type_desc).save()

        except Exception as e:
            logger.error(e.message)
            data = {
                'status': '0',
                'message': e.message
            }

        return json_response(data)


class MapCodeConfig(CsrfExemptMixin, View):
    def get(self, request, featurename, page, *args, **kwargs):
        """获取map code表配置信息"""
        data = {
            'status': 1,
            'message': 'success'
        }
        try:
            current_page = page
            page_size = 10
            if featurename == 'all':
                obj = FeatureCodeMapping.objects.values()
            else:
                obj = FeatureCodeMapping.objects.filter(feature_name=featurename).values()
            count = obj.count()
            paginator = ExtPaginator(list(obj), page_size, count)
            object_list = paginator.page(current_page)
            map(lambda x: [
                x.update({"created_on": x["created_on"].strftime('%Y-%m-%d %H:%M:%S') if x["created_on"] else ''}),
                x.update({"updated_on": x["updated_on"].strftime('%Y-%m-%d %H:%M:%S') if x["updated_on"] else ''}),
            ], object_list)

            page_num = paginator.num_pages
            page_range = paginator.page_range

            res_data = dict(
                total_count=count,
                page_num=page_num,
                current_page=current_page,
                config_list=list(object_list),
                page_range=page_range
            )

            data.update({"res_data": res_data})
        except Exception as e:
            logger.error(e.message)
            data = {
                'status': '0',
                'message': e.message
            }

        return json_response(data)

    def put(self, request, id, *args, **kwargs):
        """更新mapcode配置信息"""
        data = {
            'status': 1,
            'message': 'success'
        }
        try:
            body = json.loads(request.body)
            updated_on = datetime.datetime.now()
            is_delete = body.get('is_delete', 0)
            feature_name = body.get('feature_name', '')
            feature_desc = body.get('feature_desc', '')
            unitary_value = str(body.get('unitary_value', ''))
            dual_value = body.get('dual_value', '')
            mapped_value = str(body.get('mapped_value', ''))
            value_type = body.get('value_type', '')
            arithmetic_type = body.get('arithmetic_type', '')

            if not (feature_name and unitary_value and mapped_value and arithmetic_type):
                raise Exception("all values don't is null !")
            FeatureCodeMapping.objects.filter(pk=int(id)).update(
                feature_name=feature_name,
                feature_desc=feature_desc,
                unitary_value=unitary_value,
                dual_value=dual_value,
                mapped_value=mapped_value,
                value_type=value_type,
                arithmetic_type=arithmetic_type,
                updated_on=updated_on,
                is_delete=is_delete
            )

        except Exception as e:
            logger.error(e.message)
            data = {
                'status': '0',
                'message': e.message
            }

        return json_response(data)

    def post(self, request, *args, **kwargs):
        """添加mapcode配置"""
        data = {
            'status': 1,
            'message': 'success'
        }
        try:
            body = json.loads(request.body)
            updated_on = datetime.datetime.now()
            is_delete = body.get('is_delete', 0)
            feature_name = body.get('feature_name', '')
            feature_desc = body.get('feature_desc', '')
            unitary_value = str(body.get('unitary_value', ''))
            dual_value = body.get('dual_value', '')
            mapped_value = str(body.get('mapped_value', ''))
            value_type = body.get('value_type', '')
            arithmetic_type = body.get('arithmetic_type', '')
            if not (feature_name and unitary_value and mapped_value and arithmetic_type):
                raise Exception("all values don't is null !")
            t = FeatureCodeMapping.objects.filter(feature_name=feature_name, unitary_value=unitary_value,
                                                 dual_value=dual_value)
            print t[0].id
            if t.count():
                raise Exception(u'此配置的map值已经存在！')
            FeatureCodeMapping(
                feature_name=feature_name,
                feature_desc=feature_desc,
                unitary_value=unitary_value,
                dual_value=dual_value,
                mapped_value=mapped_value,
                value_type=value_type,
                arithmetic_type=arithmetic_type,
                updated_on=updated_on,
                created_on=updated_on,
                is_delete=is_delete
            ).save()

        except Exception as e:
            logger.error(e.message)
            data = {
                'status': 0,
                'message': e.message
            }

        return json_response(data)
