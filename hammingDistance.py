#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@Author: linjie

@license: (C) Copyright 2018-2099,  Limited.

@Contact: jielove1@hotmail.com

@Software: PyCharm

@File: hammingDistance.py

@Date: 2018/6/21 16:57

@Desc:461. 汉明距离
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。

注意：
0 ≤ x, y < 231.

示例:

输入: x = 1, y = 4

输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

上面的箭头指出了对应二进制位不同的位置。

'''


class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # 数据取异或，结果每位数位上的1求和
        cnt = 0
        res = x ^ y
        for i in range(32):
            while res:
                cnt += 1
                res = res & (res - 1)  # 经典算法，依次取出最右边的数位1
                # print(res)

        return cnt

    def hammingDistance2(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # 直接使用函数bin转换为二进制字符串，计数
        return bin(x ^ y).count('1')

if __name__ == '__main__':
    sol = Solution()
    x = 1
    y = 4
    print('{} 和 {} 汉明距离为：'.format(x,y))
    print(sol.hammingDistance(x,y))
    print(sol.hammingDistance2(x, y))
