#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@Author: linjie

@license: (C) Copyright 2018-2099,  Limited.

@Contact: jielove1@hotmail.com

@Software: PyCharm

@File: smallestDistancePair.py

@Date: 2018/6/20 18:24

@Desc:719. 找出第 k 小的距离对
给定一个整数数组，返回所有数对之间的第 k 个最小距离。一对 (A, B) 的距离被定义为 A 和 B 之间的绝对差值。

示例 1:

输入：
nums = [1,3,1]
k = 1
输出：0
解释：
所有数对如下：
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
因此第 1 个最小距离的数对是 (1,1)，它们之间的距离为 0。
提示:

2 <= len(nums) <= 10000.
0 <= nums[i] < 1000000.
1 <= k <= len(nums) * (len(nums) - 1) / 2.
'''


class Solution:
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 对距离转换成查找
        # 数值排序后，计算 数组最大距离right
        # 每次按照二分法, 得到距离 mid, 计算出所有小于等于mid的数对(x,y)的和sum
        # 循环结束和返回right值 , 就是要找的距离k
        ordernums = sorted(nums)
        left = 0
        right = ordernums[-1] - ordernums[0]
        num = len(nums)
        while left < right:

            mid = left + int((right - left) / 2)
            cnt = 0
            start = 0
            for i in range(num):
                while start < i and ordernums[i] - ordernums[start] > mid:
                    start += 1
                cnt += i - start
            if cnt < k:
                left = mid + 1
            else:
                right = mid

        return right

if __name__ == '__main__':
    sol = Solution()
    nums = [1, 3, 1]
    k = 1
    print('第 {} 小的距离对的距离:'.format(k))
    print(sol.smallestDistancePair(nums, k))




