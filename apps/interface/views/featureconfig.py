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

from braces.views import CsrfExemptMixin
from django.http.response import HttpResponse
from django.views.generic import View

from apps.interface.decorator import data_check, data_send, json_load
from apps.etl.models import *
from apps.datasource.models import *
from vendor.utils.pagination import ExtPaginator
from vendor.utils.commons import json_response

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
                x.update({"data_identity": eval(x["data_identity"]) if x["data_identity"] else ''}),
                x.update(
                    {"feature_select_value": eval(x["feature_select_value"]) if x["feature_select_value"] else ''}),
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
                'message': 'error message:%s' % e.message
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
                'message': 'error message:%s' % e.message
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
                count = FeatureConf.objects.filter(feature_name=feature_name)
                if count:
                    raise Exception('%s already exists' % feature_name)
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

            # elif item == 'feature_source':
            #
            #     FeatureConf(
            #         collect_type=body.get('collect_type'),
            #         data_identity=body.get('data_identity'),
            #         updated_on=created_on,
            #         created_on=created_on
            #     ).save()
            else:
                raise Exception('url error')
        except Exception as e:
            logger.error(e.message)
            data = {
                'status': '0',
                'message': 'error message:%s' % e.message
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
            page_size = 10
            if featurename == 'all':
                feature_config_obj = FeatureShuntConf.objects.filter(is_delete=False).values()
            else:
                feature_config_obj = FeatureShuntConf.objects.filter(is_delete=False, feature_name=featurename).values()
            feature_config_count = feature_config_obj.count()

            paginator = ExtPaginator(list(feature_config_obj), page_size, feature_config_count)
            object_list = paginator.page(current_page)
            map(lambda x: [
                x.update({"created_on": x["created_on"].strftime('%Y-%m-%d %H:%M:%S') if x["created_on"] else ''}),
                x.update({"updated_on": x["updated_on"].strftime('%Y-%m-%d %H:%M:%S') if x["updated_on"] else ''}),
                x.update({"shunt_value": eval(x["shunt_value"]) if x["shunt_value"] else ''}),
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
                'message': 'error'
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
            feature_name = body['feature_name']
            shunt_key = body['shunt_key']
            shunt_type = body['shunt_type']
            shunt_value = tuple(body['shunt_value'])
            data_identity = body['data_identity']
            is_delete = body['is_delete']
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
                'message': 'error'
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
            feature_name = body['feature_name']
            shunt_key = body['shunt_key']
            shunt_type = body['shunt_type']
            shunt_value = tuple(body['shunt_value'])
            data_identity = body['data_identity']
            is_delete = body['is_delete']
            FeatureShuntConf(
                feature_name=feature_name,
                shunt_key=shunt_key,
                data_identity=data_identity,
                shunt_type=shunt_type,
                shunt_value=shunt_value,
                is_delete=is_delete
            ).save()
        except Exception as e:
            logger.error(e.message)
            data = {
                'status': '0',
                'message': 'error'
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
            page_size = 10
            if featurename == 'all':
                feature_config_obj = FeatureRelevanceConf.objects.filter(is_delete=False).values()
            else:
                feature_config_obj = FeatureRelevanceConf.objects.filter(
                    is_delete=False,
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
                'message': 'error'
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
            depend_di = body['depend_di']
            is_delete = body['is_delete']
            updated_on = datetime.datetime.now()

            FeatureRelevanceConf.objects.filter(pk=int(featureid)).update(
                feature_name=feature_name,
                depend_feature=depend_feature,
                data_identity=data_identity,
                depend_di=depend_di,
                updated_on=updated_on,
                is_delete=is_delete
            )
        except Exception as e:
            logger.error(e.message)
            data = {
                'status': '0',
                'message': 'error'
            }

        return json_response(data)

    def post(self, request, *args, **kwargs):
        """添加依赖特征基本信息配置"""
        data = {
            'status': 1,
            'message': 'success'
        }
        try:
            body = json.loads(request.body)
            logger.info("add shunt feature config request data=%s", body)
            feature_name = body['feature_name']
            depend_feature = body['depend_feature']
            data_identity = body['data_identity']
            depend_di = body['depend_di']
            is_delete = body['is_delete']
            updated_on = datetime.datetime.now()
            FeatureRelevanceConf(
                feature_name=feature_name,
                depend_feature=depend_feature,
                data_identity=data_identity,
                depend_di=depend_di,
                updated_on=updated_on,
                is_delete=is_delete
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
                'message': 'error message:%s' % e.message
            }

        return json_response(data)

    def put(self, request, fieldid, *args, **kwargs):
        """更新特征基础配置信息"""
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
            if (source and path) or (not source and not path):
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
                'message': 'error message:%s' % e.message
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
                count = FeatureConf.objects.filter(feature_name=feature_name)
                if count:
                    raise Exception('%s already exists' % feature_name)
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

            # elif item == 'feature_source':
            #
            #     FeatureConf(
            #         collect_type=body.get('collect_type'),
            #         data_identity=body.get('data_identity'),
            #         updated_on=created_on,
            #         created_on=created_on
            #     ).save()
            else:
                raise Exception('url error')
        except Exception as e:
            logger.error(e.message)
            data = {
                'status': '0',
                'message': 'error message:%s' % e.message
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
            page_size = 10
            if data_identity == 'all':
                data_identity_obj = DsInterfaceInfo.objects.filter(is_delete=False).values()
            else:
                data_identity_obj = DsInterfaceInfo.objects.filter(
                    is_delete=False,
                    data_identity=data_identity
                ).values()
            data_identity_count = data_identity_obj.count()

            paginator = ExtPaginator(list(data_identity_obj), page_size, data_identity_count)
            object_list = paginator.page(current_page)
            map(lambda x: [
                x.update({"created_on": x["created_on"].strftime('%Y-%m-%d %H:%M:%S') if x["created_on"] else ''}),
                x.update({"updated_on": x["updated_on"].strftime('%Y-%m-%d %H:%M:%S') if x["updated_on"] else ''}),
                x.update({"must_data": eval(x["must_data"]) if x["must_data"] else ''}),
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
                'message': 'error'
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


class GetItemList(CsrfExemptMixin, View):
    def get(self, request, item, *args, **kwargs):
        """获取下拉列表信息"""
        try:
            if item == 'feature_name':
                data = FeatureConf.objects.filter(is_delete=False).values_list('id', 'feature_name')
            elif item == 'feature_type':
                data = FeatureType.objects.values_list('id', 'feature_type_desc')
            elif item == 'feature_card_type':
                data = FeatureCardType.objects.values_list('id', 'feature_type_desc')
            elif item == 'feature_rule_type':
                data = FeatureRuleType.objects.values_list('id', 'feature_type_desc')
            elif item == 'args':
                data = PreFieldInfo.objects.filter(is_delete=False).values_list('id', 'field_name')
            elif item == 'funcname':
                data = FuncLibSource.objects.values_list('func_name', 'func_type')
            elif item == 'data_identity':
                data = DsInterfaceInfo.objects.values_list('id', 'data_identity')
            else:
                raise Exception('url error')
            data = {id: value for id, value in data}
        except Exception as e:
            logger.error(e.message)
            data = {
                'status': '0',
                'message': 'error message:%s' % e.message
            }

        return json_response(data)
