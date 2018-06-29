#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@Author: linjie

@license: (C) Copyright 2018-2099,  Limited.

@Contact: jielove1@hotmail.com

@Software: PyCharm

@File: countBinarySubstrings.py

@Date: 2018/6/21 10:06

@Desc:696. 计数二进制子串
给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。

重复出现的子串要计算它们出现的次数。

示例 1 :

输入: "00110011"
输出: 6
解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。

请注意，一些重复出现的子串要计算它们出现的次数。

另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。
示例 2 :

输入: "10101"
输出: 4
解释: 有4个子串：“10”，“01”，“10”，“01”，它们具有相同数量的连续1和0。
注意：

s.length 在1到50,000之间。
s 只包含“0”或“1”字符。

'''


class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 算法：先计算每个连续字符的数量分布
        # 遍历每个数值，一次取相邻两个值的最小值求和返回
        temp = ''
        # nums = []
        cur_cnt = 0
        pre_cnt = 0
        sum_total = 0

        for str in s:
            if str == temp:
                cur_cnt += 1
            else:
                temp = str
                sum_total += min((cur_cnt,pre_cnt))
                pre_cnt = cur_cnt
                cur_cnt = 1
        # 循环最后的一串字符没有统计，需要再计算一次，
        sum_total += min((cur_cnt, pre_cnt))
        return sum_total

    def countBinarySubstrings2(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 算法：依次遍历每个字符
        # 判断和之前一个字符不同时，数值加1；
        # 和前一个相同时，判断组合长度是不超过之前的不同字符串的长度，统计和加1
        #一个位置记录之前字符的位置,和长度
        sum_total = 0
        pre = s[0]
        pos = 0
        pre_len = 0

        for i in range(1,len(s)):
            if s[i] != pre:
                sum_total += 1
                pre_len = i - pos
                pos = i
            else:
                if i - pos + 1 <= pre_len:
                    sum_total += 1
            pre = s[i]
            # print(i,sum_total,s[:i+1])
        return sum_total

if __name__ == '__main__':
    sol = Solution()
    s = '00110011'
    print('字符串 {} 具有相同数量0和1的非空(连续)子字符串的数量为:'.format(s))
    print(sol.countBinarySubstrings(s))
    print(sol.countBinarySubstrings2(s))
