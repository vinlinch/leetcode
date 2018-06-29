#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@Author: linjie

@license: (C) Copyright 2018-2099,  Limited.

@Contact: jielove1@hotmail.com

@Software: PyCharm

@File: flipAndInvertImage.py

@Date: 2018/6/20 11:33

@Desc:832. 翻转图像
给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。

水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。

反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。

示例 1:

输入: [[1,1,0],[1,0,1],[0,0,0]]
输出: [[1,0,0],[0,1,0],[1,1,1]]
解释: 首先翻转每一行: [[0,1,1],[1,0,1],[0,0,0]]；
     然后反转图片: [[1,0,0],[0,1,0],[1,1,1]]
示例 2:

输入: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
输出: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
解释: 首先翻转每一行: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]]；
     然后反转图片: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
说明:

1 <= A.length = A[0].length <= 20
0 <= A[i][j] <= 1
'''
class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # 每行按反序，与1取异或生成
        reverse_a = []
        for row in A:
            reverse_a.append([x^1 for x in row[::-1]])
        return reverse_a

    def flipAndInvertImage02(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # 每行按反序，与1取异或生成
        return [[x^1 for x in row[::-1]] for row in A]

if __name__ == '__main__':
    sol = Solution()
    A = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    print('{} \n翻转图像后为:'.format(A))
    # print(sol.flipAndInvertImage(A))
    print(sol.flipAndInvertImage02(A))
