#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@Author: linjie

@license: (C) Copyright 2018-2099,  Limited.

@Contact: jielove1@hotmail.com

@Software: PyCharm

@File: numberOfBoomerangs.py

@Date: 2018/6/19 18:29

@Desc:447. 回旋镖的数量
给定平面上 n 对不同的点，“回旋镖” 是由点表示的元组 (i, j, k) ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。

找到所有回旋镖的数量。你可以假设 n 最大为 500，所有点的坐标在闭区间 [-10000, 10000] 中。

示例:

输入:
[[0,0],[1,0],[2,0]]

输出:
2

解释:
两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
'''
class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # 对每个点i 求出所有点的距离
        # 相同距离的点组成一组
        # 计算每组依次取2个点的排列数，求和所有的排列数就是点i为顶点的回旋镖数
        # 对其他点j重复上面3个步骤
        total_count = 0
        length = len(points)
        # init_dict = {}

        def distance(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

        for i in range(length):
            dist_dicts = {}
            for j in range(length):
                if i != j:
                    dist = distance(points[i], points[j])
                    dist_dicts[dist] = dist_dicts.setdefault(dist,0) + 1
            for key, value in dist_dicts.items():
                total_count += value * (value - 1)

        return total_count

if __name__ == '__main__':
    points = [[0, 0], [1, 0], [2, 0]]

    sol = Solution()
    print('两个回旋镖为 {}'.format(sol.numberOfBoomerangs(points)))

