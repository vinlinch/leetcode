#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@Author: linjie

@license: (C) Copyright 2018-2099,  Limited.

@Contact: jielove1@hotmail.com

@Software: PyCharm

@File: maximumSwap.py

@Date: 2018/7/3 18:11

@Desc:670. 最大交换
给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。

示例 1 :

输入: 2736
输出: 7236
解释: 交换数字2和数字7。
示例 2 :

输入: 9973
输出: 9973
解释: 不需要交换。
注意:

给定数字的范围是 [0, 108]
'''


class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        temp = {}
        n = list(str(num))
        l = len(n)

        for i in range(len(n)):
            temp = '0'
            f = False
            p = i
            for j in range(i + 1, l):
                if n[i] < n[j]:
                    if temp <= n[j]:
                        temp = n[j]
                        p = j
                        f = True
            if f:
                n[i], n[p] = n[p], n[i]
                break
        return int(''.join(n))

import random
if __name__ == '__main__':
    sol = Solution()
    r = random.Random()
    num = r.randint(1,10**8)
    print('{} 交换一次数字的最大值为: {}'.format(num, sol.maximumSwap(num)))