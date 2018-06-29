#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@Author: linjie

@license: (C) Copyright 2018-2099,  Limited.

@Contact: jielove1@hotmail.com

@Software: PyCharm

@File: peakIndexInMountainArray.py

@Date: 2018/6/20 9:46

@Desc:852. 山脉数组的峰顶索引
我们把符合下列属性的数组 A 称作山脉：

A.length >= 3
存在 0 < i < A.length - 1 使得A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
给定一个确定为山脉的数组，返回任何满足 A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1] 的 i 的值。



示例 1：

输入：[0,1,0]
输出：1
示例 2：

输入：[0,2,1,0]
输出：1


提示：

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A 是如上定义的山脉
'''


class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        start = 0
        end = len(A)
        i = int((start + end) / 2)
        while start < end:
            if A[i-1] < A[i] and A[i] > A[i+1]:
                break
            elif A[i - 1] > A[i]:
                end = i
            elif A[i] < A[i+1]:
                start = i + 1
            i = int((start + end) / 2)

        return i

if __name__ == '__main__':
    sol = Solution()
    A = [0,1,2,3,4,5,8,9,10,12,15,17,89,73,72,50,49,38,27,19,2,1,0]
    index = sol.peakIndexInMountainArray(A)
    print('山脉数组\n{}\n的峰顶索引{}, 数字为 {}'.format(A,index, A[index]))

