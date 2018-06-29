#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@Author: linjie

@license: (C) Copyright 2018-2099,  Limited.

@Contact: jielove1@hotmail.com

@Software: PyCharm

@File: knightProbability.py

@Date: 2018/6/21 17:02

@Desc:688. “马”在棋盘上的概率
已知一个 NxN 的国际象棋棋盘，棋盘的行号和列号都是从0开始。即最左上角的格子记为 (0, 0), 最右下角的记为 (N-1, N-1)。

现有一个“马”（也译作“骑士”）位于 (r, c) ，并打算进行 K 次移动。

如下图所示，国际象棋的“马”每一步先沿水平或垂直方向移动2个格子，然后向与之相垂直的方向再移动1个格子，共有8个可选的位置。



现在“马”每一步都从可选的位置（包括棋盘外部的）中独立随机地选择一个进行移动，直到移动了 K 次或跳到了棋盘外面。

求移动结束后，“马”仍留在棋盘上的概率。

例:

输入: 3, 2, 0, 0
输出: 0.0625
解释:
输入的数据依次为 N, K, r, c
第1步时，有且只有2种走法令“马”可以留在棋盘上(跳到(1,2)或(2,1))。对于以上的两种情况，各自在第2步均有且只有2种走法令“马”仍然留在棋盘上。
所以“马"在结束后仍在棋盘上的概率为0.0625。
注意:

N 的取值范围为 [1, 25]
K 的取值范围为 [0, 100]
开始时，“马”总是位于棋盘上

'''


class Solution:

    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        # 使用dsf深度优先搜索算法，依次遍历每步结果
        # 优化，对于已经计算过相同位置结果的值直接返回，需要存储一个数字在数组中
        # 递归调用函数
        moves = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]
        # python数组的构建
        # 不能使用 [[0] * range(N)], 这样导致每个元素都是同一个list引用，更新其中一个元素就会更新所有的
        prob = [[[0 for i in range(N)] for j in range(N)] for t in range(K + 1)]

        def J(k, r1, c1):
            if k == 0:
                return 1
            if prob[k][r1][c1] != 0:
                return prob[k][r1][c1]

            for m in moves:
                x, y = r1 + m[0], c1 + m[1]
                if 0 <= x < N and 0 <= y < N:
                    prob[k][r1][c1] += J(k-1,x,y)
            return prob[k][r1][c1]

        return J(K,r,c) / (8**K)


    def knightProbability2(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        # 循环依次添加所有步骤后的所有结果，计数
        # 效率差，重复计算相同位置的结果
        moves = [(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(-2,1),(2,-1),(-2,-1)]

        start = [(r,c)]
        pos = [start]

        for i in range(K):
            new_step = []
            for p in pos[i]:
                for m in moves:
                    x, y = p[0] + m[0], p[1] + m[1]
                    if 0 <= x < N and 0 <= y < N:
                        new_step.append((x,y))
            pos.append(new_step)

        return len(pos[-1]) / (8**K)

if __name__ == '__main__':
    sol = Solution()
    N,K,r,c = 3, 5,0,0
    list = [N,K,r,c]
    # list = [6,12,6,4]
    print('{0}X{0}的棋牌上，初始位置({2},{3})的“马”经过{1}步后，\n在棋盘上的概率为：'.format(*list))
    print(sol.knightProbability(*list))
    print(sol.knightProbability2(*list))