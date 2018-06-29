#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@Author: linjie

@license: (C) Copyright 2018-2099,  Limited.

@Contact: jielove1@hotmail.com

@Software: PyCharm

@File: totalHammingDistance.py

@Date: 2018/6/20 14:49

@Desc:477. 汉明距离总和
两个整数的 汉明距离 指的是这两个数字的二进制数对应位不同的数量。

计算一个数组中，任意两个数之间汉明距离的总和。

示例:

输入: 4, 14, 2

输出: 6

解释: 在二进制表示中，4表示为0100，14表示为1110，2表示为0010。（这样表示是为了体现后四位之间关系）
所以答案为：
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
注意:

数组中元素的范围为从 0到 10^9。
数组的长度不超过 10^4。
'''

# import numpy as np
class Solution:
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 对每个数值转换成32位的2进制字符串
        # 每个字符串相同位置的字符重新合成新的字符串
        # 对新字符串使用count计算数字0和1的个数相乘
        # 对所有乘积求和
        return sum(b.count('0') * b.count('1') for b in zip(*map('{:032b}'.format, nums)))


    def totalHammingDistance02(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 每个数位上的hanmming和求和
        # 重复执行，只变化mask
        # 缺点 ： 计算次数都是 32 × len(nums)
        total_sum = 0
        numbers = len(nums)
        # print('numbers: {}'.format(numbers))
        loop_num = nums[:]
        for i in range(32):
            mask = 1 << i
            counts = 0
            for num in loop_num:
                if num & mask:
                    counts += 1
            total_sum += (numbers - counts) * counts

        return total_sum

    def totalHammingDistance03(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 对每个数值，计算相同数位上的1的数量
        # 相同数位上任意2个数的haming距离为组合数counts(1) * (len- count(1))
        # 所有数位上的hamming求和
        total_sum = 0
        numbers = len(nums)
        # print('numbers: {}'.format(numbers))
        loop_num = nums[:]
        for i in range(32):
            counts = 0
            temp = []
            for num in loop_num:
                if num % 2:
                    counts += 1
                c = num >> 1
                if c:
                    temp.append(c)
                # temp.append(num >> 1)
            total_sum += (numbers - counts) * counts
            # loop_num = list(filter(bool, temp))
            loop_num = temp[:]
            if len(loop_num) == 0:
                break
            # print('loop :{}, sum:{}'.format(i,total_sum))
        return total_sum

    def totalHammingDistance04(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 每个数位上的hanmming和求和
        # 重复执行，只变化mask
        # 缺点 ： 计算次数都是 32 × len(nums)
        total_sum = 0
        bin_nums = [bin(n)[2:][::-1] for n in nums]
        numbers = len(nums)
        # print('bin_nums: {}'.format(bin_nums))

        for i in range(32):
            counts = 0
            for num in bin_nums:
                if len(num) > i and num[i] == '1':
                    # print('num[i]:',format(num[i]))
                    counts += 1
                # print('i :{},num:{},counts:{} '.format(i,num,counts))
            total_sum += (numbers - counts) * counts
            # print('i :{}, total_sum:{} '.format(i,   total_sum))

        return total_sum

if __name__ == '__main__':
    nums = [4, 14, 2]
    sol = Solution()
    print('汉明距离总和 为:')
    print(sol.totalHammingDistance(nums))
    print(sol.totalHammingDistance02(nums))
    print(sol.totalHammingDistance03(nums))
    print(sol.totalHammingDistance04(nums))




