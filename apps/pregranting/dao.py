# -*- coding: utf-8 -*-

from .models import ModelFieldOptionWeight, ModelCoefficientConf


class PreModelDao(object):
    def __init__(self):
        pass

    @classmethod
    def get_model_fields(cls, model_name):
        filter_kwargs = {
            'model_name': model_name,
            'is_delete': False
        }

        model_field_qs = ModelFieldOptionWeight.objects.filter(**filter_kwargs)
        return model_field_qs

    @classmethod
    def get_sub_level(cls, model_name, income):
        """ Get all the range """
        filter_kwargs = {
            'model_name': model_name,
            'income_interval_min__lte': income,
            'income_interval_max__gt': income,
            'is_delete': False
        }

        sub_level_qs = ModelCoefficientConf.objects.filter(**filter_kwargs)
        if sub_level_qs.exists():
            return sub_level_qs[0]

        return None

    def get_model_field_list(self, model_name):
        """ get model field list
        @:param model_name
        @:return [] or ['field1', 'field2', ...]
        """
        field_list = []

        model_field_qs = self.get_model_fields(model_name)
        if model_field_qs.exists():
            for item in model_field_qs.iterator():
                if item.field_name not in field_list:
                    field_list.append(item.field_name)

        return field_list

    # @classmethod
    def get_option_weight(self, model_name):
        """ option weight
        @:param model_name  model name
        @:return {} or {"field1": {"option1_code": 1.0, "option2_code": 2.0}, "field2": {...}}
        """
        option_weight_map = {}

        model_field_qs = self.get_model_fields(model_name)
        if model_field_qs.exists():
            for option in model_field_qs.iterator():
                if option.field_name not in option_weight_map:
                    option_weight_map[option.field_name] = {}

                option_weight_map[option.field_name].update({
                    option.field_option_value: option.field_option_weight
                })

        return option_weight_map
