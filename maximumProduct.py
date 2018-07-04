#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@Author: linjie

@license: (C) Copyright 2018-2099,  Limited.

@Contact: jielove1@hotmail.com

@Software: PyCharm

@File: maximumProduct.py

@Date: 2018/7/3 18:29

@Desc:628. 三个数的最大乘积
给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

示例 1:

输入: [1,2,3]
输出: 6
示例 2:

输入: [1,2,3,4]
输出: 24
注意:

给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。
输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。


'''


class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        n = sorted(nums)

        a = n[-1] * n[-2] * n[-3]
        b = n[0] * n[1] * n[-1]

        return max(a,b)

    def maximumProduct2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import heapq
        large = heapq.nlargest(3,nums)
        small = heapq.nsmallest(2,nums)
        a= large[0] * large[1] * large[2]
        b = small[0] * small[1] * large[0]
        return max(a,b)


if __name__ == '__main__':
    sol = Solution()
    nums = [-4,-3,-2,-1,60]
    b = sol.maximumProduct(nums)
    print('三个数的最大乘积:')
    print(sol.maximumProduct(nums))
    print(sol.maximumProduct2(nums))