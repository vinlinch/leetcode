#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@Author: linjie

@license: (C) Copyright 2018-2099,  Limited.

@Contact: jielove1@hotmail.com

@Software: PyCharm

@File: findPeakElement.py

@Date: 2018/6/20 10:23

@Desc:162. 寻找峰值
峰值元素是指其值大于左右相邻值的元素。

给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。

数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞。
输入: nums = [1,2,3,1]
输出: 2
解释: 3 是峰值元素，你的函数应该返回其索引 2。
示例 2:

输入: nums = [1,2,1,3,5,6,4]
输出: 1 或 5
解释: 你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6。

'''
class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 二分查找 时间复杂logN
        # 每次区间下标左右移动，取中间下标的数值比较
        start = 0
        end = len(nums)
        if len(nums) == 2:
            i = 0 if nums[0] > nums[1] else 1
            return i

        i = int((start + end) / 2)
        while True:
            if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                break
            elif nums[i - 1] > nums[i]:
                end = i
            else:
                start = i + 1

            i = int((start + end) / 2)
            if i == 0 or i == len(nums) - 1:
                break
        return i

if __name__ == '__main__':
    nums = [1, 2, 1, 3, 5, 6, 4]
    sol = Solution()
    print('{}\n峰值元素索引是:'.format(nums))
    print(sol.findPeakElement(nums))
