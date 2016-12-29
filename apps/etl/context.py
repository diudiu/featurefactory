# -*- coding:utf-8 -*-

import logging
import datetime

from .backend import MongodbBackend
from apps.common.mongo_model import OriginalBase, ProcessBase, CacheBase

logger = logging.getLogger('apps.etl')


class OriginalContext(object):
    """
    这是一个储存原始数据的Mongo集合
    以受信人为文档标识
    每一组数据包含:
        1.数据源直接返回的查询结果
        2.请求数据源用到的参数
        3.查询时间
    储存模式:永久
    """

    def __init__(self, apply_id, **kwargs):
        """if apply_id is None initialize for it, or get it"""
        self.original_model = OriginalBase
        self.apply_id = apply_id
        self.kwargs = kwargs if kwargs else {}
        if not self.kwargs:
            filters = dict(apply_id=self.apply_id, limit_start=0, limit_end=1)
            apply_info = MongodbBackend(self.original_model, **filters).load(only_one=True)
            if apply_info:
                self.kwargs.update(apply_info)

    def save(self):
        """save apply kwargs to backend"""
        apply_info = MongodbBackend(self.original_model, apply_id=self.apply_id).load(only_one=True, obj=True)
        if apply_info:
            apply_info.update(**self.kwargs)
        else:
            backend = MongodbBackend(self.original_model, **self.kwargs)
            backend.save()

        return self.apply_id

    def get(self, key):
        """get value for key from kwargs"""

        return self.kwargs.get(key, None)

    @property
    def data(self):
        """return all attribute for apply info dict"""
        return self.kwargs


class ProcessContext(object):
    """Store proposer audit information,
        usage:
            1. other module get audit information
            2. update proposer audit information, status , score and so on
    """

    def __init__(self, apply_id):
        """if audit info has not been in backend, At first get info from apply info
            And then store in backend, also save it for portrait
            if audit info has been store in backend, get all information from backend
            :param apply_id, apply identity
        """
        assert apply_id
        self.apply_id = apply_id
        self.kwargs = {}
        self.fields_dict = {}
        self._init_data()

    def _init_data(self):
        """get data from audit info backend or init from apply info backend
        """
        audit_info = MongodbBackend(self.audit_info_model, apply_id__value=self.apply_id).load(only_one=True)
        if not audit_info:
            apply_info = MongodbBackend(self.apply_info_model, apply_id=self.apply_id).load(only_one=True)
            if apply_info:
                audit_info = {}
                fields = FieldInfo.objects.all().values('name', 'confidence', 'is_derived', 'effective_days')
                fields_dict = dlist_to_dict(key="name", dlist=fields)
                self.fields_dict = fields_dict
                for k, v in apply_info.iteritems():
                    if k in fields_dict.keys():
                        audit = {
                            "value": v,
                            "confidence": fields_dict[k]["confidence"],
                            "is_derived": fields_dict[k]["is_derived"],
                            "created_time": datetime.datetime.now()
                        }
                        audit_info.update({k: audit})
                    else:
                        audit_info.update({k: v})
                MongodbBackend(self.audit_info_model, **audit_info).save()
                proposer_id = apply_info.get("proposer_id", "")
                if proposer_id:
                    portrait = MongodbBackend(self.portrait_model, proposer_id__value=proposer_id).load(only_one=True)
                    if portrait:
                        MongodbBackend(self.portrait_model).update(proposer_id__value=proposer_id, **audit_info)
                    else:
                        MongodbBackend(self.portrait_model, **audit_info).save()  # need check exist
                else:
                    raise FieldNotBlankError("apply info:%s proposer_id None" % self.apply_id)
            else:
                raise RecordNoneError("apply_id error")
        if audit_info:
            self.kwargs.update(audit_info)

    def get(self, key):
        """get value for key from kwargs, if None try get it from portrait(need check effectiveness) and data source
        """
        if key not in self.kwargs.keys():
            value = None
        else:
            temp_value = self.kwargs[key]
            if isinstance(temp_value, dict):
                value = temp_value["value"]
            else:
                value = temp_value
        if value is None:  # or value == ""
            portrait = PortraitContext(self.kwargs["proposer_id"])
            value_dict = portrait.get(key)
            server_datetime = datetime.datetime.now()
            if value_dict:
                field_info = FieldInfo.objects.get(name=key)
                effective_days = field_info.effective_days
                if (server_datetime - value_dict['created_time']).days < effective_days:
                    value = value_dict["value"]
                else:
                    logger.warn("portrait value:%s is overdue", value_dict["value"])
            dim = DimensionDerivation.objects.filter(target_dim_field_name=key)
            if dim and not value:
                value_dict = self.get_data_by_interface(key, dims=dim)
                if value_dict is None:
                    return None
                if isinstance(value_dict, dict):
                    self.kwargs.update(value_dict)
                    self.set(lazy=False, **value_dict)
                    return value_dict[key]
                else:
                    value_dict = {key: value_dict}
                self.set(lazy=False, **value_dict)
                if value_dict:
                    self.kwargs.update(value_dict)
                    value = value_dict[key]
        return value

    def get_keys(self, *keys):
        """
            try through multiprocessing concurrence get result
            :return []
        """
        assert keys
        pool_size = multiprocessing.cpu_count() * 2
        pool = ThreadPool(pool_size)
        values = pool.map(lambda key: self.get(key), keys)
        pool.close()
        pool.join()

        return values

    def set(self, lazy=True, query={}, **kwargs):
        """update value for key
            :type kwargs: object
            :param lazy, decide whether update backend
            :param query, update for query documents
            if lazy is True, just update AuditInfoContext instance attribute,
            if is False update AuditInfoContext instance and backend and also update portrait
        """
        if not getattr(self, "fields_dict"):
            fields = FieldInfo.objects.all().values('name', 'confidence', 'is_derived', 'effective_days')
            fields_dict = dlist_to_dict(key="name", dlist=fields)
            self.fields_dict = fields_dict

        for k, v in kwargs.iteritems():
            if isinstance(v, dict) and ("value" in v.keys()):
                continue
            if k in self.fields_dict.keys():
                audit = {
                    "value": v,
                    "confidence": self.fields_dict[k]["confidence"],
                    "is_derived": self.fields_dict[k]["is_derived"],
                    "created_time": datetime.datetime.now()
                }
            else:
                audit = v
            kwargs.update({k: audit})

        self.kwargs.update(kwargs)
        if not lazy:
            query.update({"apply_id__value": self.kwargs["apply_id"].get("value")})
            audit = MongodbBackend(self.audit_info_model)
            audit.update(query=query, **kwargs)
            portrait = PortraitContext(self.kwargs["proposer_id"])
            portrait.set(lazy=False, **kwargs)

    def save(self):
        """update all attribute for audit info, and check update portrait"""
        audit_info = MongodbBackend(self.audit_info_model, apply_id__value=self.apply_id).load(only_one=True, obj=True)
        if audit_info:
            audit_info.update(**self.kwargs)
        else:
            backend = MongodbBackend(self.audit_info_model, **self.kwargs)
            backend.save()

        # save portrait
        portrait = MongodbBackend(self.portrait_model, proposer_id=self.kwargs["proposer_id"]).load(only_one=True)
        if not portrait:
            por = PortraitContext(self.kwargs["proposer_id"], **self.kwargs)
            por.save()
        else:
            por = PortraitContext(self.kwargs["proposer_id"])
            por.set(lazy=False, **self.kwargs)

    @property
    def data(self):
        """return all attribute for audit info dict"""
        return self.kwargs

    def get_data_by_interface(self, key, dims=None):
        """Get data through interface
            steps follow this：
                1. get parameters by key, source:DimensionFieldRel
                2. get interface by key, source:DimensionDerivation
                3. packet parameters for interface request
                4. request interface and get result
        """
        if dims.count() > 1:
            result = self.get_data_by_many_interface(key, dims)
            return result
        parameters = {}
        parameter_list = DimensionFieldRel.objects.filter(target_dim_field_name=key).values_list(
            'raw_field_name', flat=True)
        for param in parameter_list:
            if self.kwargs.get(param) and isinstance(self.kwargs[param], dict):
                value = self.kwargs.get(param, {}).get("value")
                if isinstance(value, dict):
                    parameters.update(value)
                else:
                    parameters.update({param: value})
            else:
                return None
        interface = DimensionDerivation.objects.get(target_dim_field_name=key).interface
        service = RcApiService(interface.id, parameters)
        service.do_service()
        if service.is_async:
            raise AsyncCallError()

        result = getattr(service, interface.target_fields)
        return result

    def get_data_by_many_interface(self, key, dims):
        """Get data through interface
            steps follow this：
                1. get parameters by key, source:DimensionFieldRel
                2. get interface by key, source:DimensionDerivation
                3. packet parameters for interface request
                4. request interface and get result
        """
        has_param = True
        result = None
        for dim in dims.iterator():
            derivation_id = dim.id
            interface_id = dim.interface_id
            parameters = {}
            parameter_list = DimensionFieldRel.objects.filter(
                target_dim_field_name=key,
                derivation_id=derivation_id
            ).values_list('raw_field_name', flat=True)
            for param in parameter_list:
                if self.kwargs.get(param) and isinstance(self.kwargs[param], dict):
                    value = self.kwargs.get(param, {}).get("value")
                    if isinstance(value, dict):
                        parameters.update(value)
                    else:
                        parameters.update({param: value})
                else:
                    has_param = False
                    continue
            interface = DsInterfaceInfo.objects.filter(id=interface_id)[0]
            service = RcApiService(interface.id, parameters)
            try:
                service.do_service()
            except Exception as e:
                continue
            if service.is_async:
                raise AsyncCallError()

            result = getattr(service, interface.target_fields)
            if result is not None:
                break
        return result


class CacheContext(object):
    """proposer portrait object, get or update for proposer portrait"""
    portrait_model = PortraitBase

    def __init__(self, proposer_id, user_id=None, **kwargs):
        """:param proposer_id, proposer identity
           :param user_id, who create or own this portrait
        """
        assert proposer_id
        self.proposer_id = proposer_id
        self.kwargs = kwargs
        if not self.kwargs:
            self._init_data()

    def _init_data(self):
        portrait = MongodbBackend(self.portrait_model, proposer_id=self.proposer_id).load(only_one=True)
        if portrait and isinstance(portrait, dict):
            self.kwargs.update(portrait)

    def get(self, key):
        """get value for key"""

        return self.kwargs.get(key)

    def set(self, lazy=True, query=None, **kwargs):
        """update portrait attribute
            :param lazy, if True just update PortraitContext instance, or update backend
            :param query, update for query documents
        """
        if query is None:
            query = {}
        self.kwargs.update(kwargs)
        if not lazy:
            query.update({"proposer_id__value": self.proposer_id})
            proposer = MongodbBackend(self.portrait_model)
            proposer.update(query=query, **kwargs)

    def save(self):
        """update kwargs for portrait to backend"""
        proposer = MongodbBackend(self.portrait_model,
                                  proposer_id__value=self.proposer_id).load(only_one=True, obj=True)
        if proposer:
            proposer.update(**self.kwargs)
        else:
            backend = MongodbBackend(self.portrait_model, **self.kwargs)
            backend.save()

    @property
    def data(self):
        """return all attribute for portrait info dict"""
        return self.kwargs
