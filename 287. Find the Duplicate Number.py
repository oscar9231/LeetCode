#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/08/16 10:28
# @Author  : lyc
# @File    : leetcode.py
# @Software: PyCharm

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for index, value in enumerate(nums):
            if value not in dic:
                dic[value] = index
            else:
                return value
