# -*- coding:utf-8 -*-

"""
    Licensed SYPH (beijing LTC).
    Copyright (c) 2013-2015 SYPH (Shaohan Niu), All Rights Reserved.
    ------------------------------------------------------------------------------
    Package        : vendor.helper
    File Name      : pagination.py
    Description    : extend django.core.paginator.Paginator

    Author: Shaohan Niu
    Date: 2015/9/11
    Email: niushaohan@digcredit.com
    Change Activity:
        list here
    ------------------------------------------------------------------------------
    ~ ~
"""
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage, Page


class ExtPaginator(Paginator):
    def __init__(self, object_list, per_page, total_nums, range_num=5, orphans=0, allow_empty_first_page=True):
        super(ExtPaginator, self).__init__(object_list, per_page, orphans, allow_empty_first_page)
        self.range_num = range_num
        self.page_num = 1
        self.total_nums = total_nums

    def page(self, number):
        try:
            number = self.validate_number(number)
            self.page_num = number
            bottom = (number - 1) * self.per_page
            top = bottom + self.per_page
            if top + self.orphans >= self.count:
                top = self.count
        except (InvalidPage, EmptyPage, PageNotAnInteger):
            number = 1
            bottom = 0
            top = self.per_page

        return Page(self.object_list[bottom:top], number, self)

    def _page_range_ext(self):
        num_count = 2 * self.range_num + 1
        if self.num_pages <= num_count:
            return range(1, self.num_pages + 1)

        num_list = list()
        num_list.append(self.page_num)
        for i in range(1, self.range_num + 1):
            if self.page_num - i <= 0:
                num_list.append(num_count + self.page_num - i)
            else:
                num_list.append(self.page_num - i)

            if self.page_num + i <= self.num_pages:
                num_list.append(self.page_num + i)
            else:
                num_list.append(self.page_num + i - num_count)
        num_list.sort()
        return num_list

    page_range_ext = property(_page_range_ext)

    def _get_count_ext(self):
        """
        Returns the total number of objects, across all pages.
        """
        if self._count is None:
            self._count = self.total_nums
        return self._count

    count = property(_get_count_ext)