#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@Author: linjie

@license: (C) Copyright 2018-2099,  Limited.

@Contact: jielove1@hotmail.com

@Software: PyCharm

@File: maxDistToClosest.py

@Date: 2018/6/13 11:50

@Desc:849. 到最近的人的最大距离
在一排座位（ seats）中，1 代表有人坐在座位上，0 代表座位上是空的。

至少有一个空座位，且至少有一人坐在座位上。

亚历克斯希望坐在一个能够使他与离他最近的人之间的距离达到最大化的座位上。

返回他到离他最近的人的最大距离。

示例 1：

输入：[1,0,0,0,1,0,1]
输出：2
解释：
如果亚历克斯坐在第二个空位（seats[2]）上，他到离他最近的人的距离为 2 。
如果亚历克斯坐在其它任何一个空位上，他到离他最近的人的距离为 1 。
因此，他到离他最近的人的最大距离是 2 。
示例 2：

输入：[1,0,0,0]
输出：3
解释：
如果亚历克斯坐在最后一个座位上，他离最近的人有 3 个座位远。
这是可能的最大距离，所以答案是 3 。
提示：

1 <= seats.length <= 20000
seats 中只含有 0 和 1，至少有一个 0，且至少有一个 1。
'''

from math import ceil, floor


class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        # 计算相邻有人座位之间的距离 /2是新加入坐在之间的最大距离
        # 考虑两个端点的情况，距离不需要/2
        # 所有距离求最大值返回
        index = [i for i, x in enumerate(seats) if x == 1]

        dist = list(map(lambda x, y: int((y - x) / 2), index[:-1], index[1:])) + [index[0] - 0] + [len(seats) - 1 - index[-1]]

        return max(dist)

if __name__ == '__main__':
    seats = [1, 0, 0, 1]
    s = Solution()
    print('坐下后，他到离他最近的人的最大距离 为：')
    print(s.maxDistToClosest(seats))
