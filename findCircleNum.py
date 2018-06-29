#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@Author: linjie

@license: (C) Copyright 2018-2099,  Limited.

@Contact: jielove1@hotmail.com

@Software: PyCharm

@File: findCircleNum.py

@Date: 2018/6/20 11:55

@Desc:547. 朋友圈
班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。

给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。

示例 1:

输入:
[[1,1,0],
 [1,1,0],
 [0,0,1]]
输出: 2
说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
第2个学生自己在一个朋友圈。所以返回2。
示例 2:

输入:
[[1,1,0],
 [1,1,1],
 [0,1,1]]
输出: 1
说明：已知学生0和学生1互为朋友，学生1和学生2互为朋友，所以学生0和学生2也是朋友，所以他们三个在一个朋友圈，返回1。
注意：

N 在[1,200]的范围内。
对于所有学生，有M[i][i] = 1。
如果有M[i][j] = 1，则有M[j][i] = 1。
'''
class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        # 1.对朋友进行深度优先遍历，使用标记
        # 2.递归调用，访问数组的每个元素，具有相同朋友圈的先访问完，朋友圈数值加1
        # 3.接着从下一个未被访问的新的朋友圈开始，
        # 4.重复执行 2，3，访问完美一个人
        set = 0
        visit = [False] * len(M)

        def DFS(Mat, k, visits):
            visits[k] = True
            for j, fri in enumerate(Mat[k]):
                if fri and not visits[j]:
                    DFS(Mat, j, visits)

        for i, friends in enumerate(M):
            if not visit[i]:
                DFS(M, i, visit)
                set += 1
        return set

if __name__ == '__main__':
    sol = Solution()
    M = [[1, 1, 0],
         [1, 1, 1],
         [0, 1, 1]]
    print('朋友圈的数量为: ')
    print(sol.findCircleNum(M))


