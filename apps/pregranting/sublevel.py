# -*- coding: utf-8 -*-

import logging
import operator

from apps.etl.context import PortraitContext

from .base import GrantCreditAbstract
from .dao import PreModelDao

logger = logging.getLogger('apps.openapi')


class BasePreGrant(object):
    name = ''
    abstract = True

    def __init__(self, identity):
        self.feature_library = {}
        self.feature_context = PortraitContext(identity)


class LinearPreGrant(GrantCreditAbstract, BasePreGrant):
    """ linear pre grant """
    name = 'sub_level_linear'
    abstract = False

    def __init__(self, identity):
        super(LinearPreGrant, self).__init__(identity)
        self.dao = PreModelDao()

    def grant(self):
        """ do grant """
        logger.info('=================== start to grant =================== \n')
        pre_grant_amount = 0

        self.pre_process()

        def _get_weight(weight_map, feature, code):
            if not weight_map or not isinstance(weight_map, dict):
                return 1.0

            feature_option_map = weight_map.get(feature, {})
            return feature_option_map.get(code, 1.0)

        option_weight_map = self.dao.get_option_weight(self.name)
        feature_val_weight = {feature: _get_weight(option_weight_map, feature, val) for feature, val
                              in self.feature_library.iteritems()}

        annual_income = self.feature_context.get('annual_income')
        feature_val_weight.update({'annual_income': annual_income})
        sub_level = self.dao.get_sub_level(self.name, annual_income)
        if sub_level is not None:
            pre_grant_amount_str = sub_level.computational_formula % feature_val_weight
            pre_grant_amount_str = '%s * %s' % (sub_level.coefficient, pre_grant_amount_str)
            pre_grant_amount = eval(pre_grant_amount_str)
            try:
                pre_grant_amount = int(float(str(pre_grant_amount)))
            except ValueError:
                pre_grant_amount = int(pre_grant_amount)
            logger.info('level is %s', sub_level)

        logger.info('\n\t===> model feature value weight map=%s\n\n\tannual_income=%s\n\n\tpre_grant_amount=%s',
                    feature_val_weight, annual_income, pre_grant_amount)

        # calibration result
        if operator.lt(pre_grant_amount, 5288):
            pre_grant_amount = 5288
        elif operator.lt(pre_grant_amount, 200000) and operator.ge(pre_grant_amount, 5288):
            pre_grant_amount = operator.mul(operator.div(pre_grant_amount, 100), 100)
        else:
            pre_grant_amount = 200000

        if operator.lt(pre_grant_amount, 5288):
            pre_grant_amount = 5288

        logger.info('calibration result pre_grant_amount=%s\n\n'
                    '=================== end to grant =================== \n', pre_grant_amount)
        return pre_grant_amount

    def pre_process(self):
        logger.info('===> start to %s.pre_process', self.__class__.name)

        to_be_init_features = {
            'is_on_the_job': '0',
            'highest_education': '',
            'annual_income': 0.0
        }

        # process industry_code, is_on_the_job, highest_education, annual_income
        work_exp_form = self.feature_context.get('work_exp_form')
        logger.debug('\n\twork_exp_form=%s', work_exp_form)

        # for is_on_the_job annual_income
        if work_exp_form and isinstance(work_exp_form, list):
            work_first = work_exp_form[:1][0]
            work_last = work_exp_form[:-1][0]
            if '999999' in (work_first.get('work_end'), work_last.get('work_end')):
                to_be_init_features.update({'is_on_the_job': '1'})

            first_salary = work_first.get('salary', 0) * 12
            last_salary = work_last.get('salary', 0) * 12
            to_be_init_features.update({
                'annual_income': max(first_salary, last_salary)
            })

        # for highest_education
        edu_exp_form = self.feature_context.get('edu_exp_form')
        logger.debug('\n\twork_exp_form=%s', work_exp_form)
        if edu_exp_form and isinstance(edu_exp_form, list):
            edu_first = edu_exp_form[:1][0]
            edu_last = edu_exp_form[:-1][0]
            try:
                edu_first_degree = int(edu_first.get('degree'))
            except ValueError:
                edu_first_degree = 999

            try:
                edu_last_degree = int(edu_last.get('degree'))
            except ValueError:
                edu_last_degree = 999

            edu_degree = min(edu_first_degree, edu_last_degree)
            to_be_init_features.update({
                'highest_education': str(edu_degree)
            })

        # save
        self.feature_context.set(**to_be_init_features)

        all_field_by_model = self.dao.get_model_field_list(self.name)
        self.feature_library = {feature: self.feature_context.get(feature) for feature in all_field_by_model}
        logger.debug('\n\t===> all field by model=%s\n feature library=%s', all_field_by_model, self.feature_library)

        logger.info('\n\t===> init features=%s\n\n===> end for %s.pre_process', to_be_init_features, self.__class__.name)
