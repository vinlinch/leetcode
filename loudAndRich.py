#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@Author: linjie

@license: (C) Copyright 2018-2099,  Limited.

@Contact: jielove1@hotmail.com

@Software: PyCharm

@File: loudAndRich.py

@Date: 2018/6/19 16:25

@Desc:851. 喧闹和富有
在一组 N 个人（编号为 0, 1, 2, ..., N-1）中，每个人都有不同数目的钱，以及不同程度的安静（quietness）。

为了方便起见，我们将编号为 x 的人简称为 "person x "。

如果能够肯定 person x 比 person y 更有钱的话，我们会说 richer[i] = [x, y] 。注意 richer 可能只是有效观察的一个子集。

另外，如果 person x 的安静程度为 q ，我们会说 quiet[x] = q 。

现在，返回答案 answer ，其中 answer[x] = y 的前提是，在所有拥有的钱不少于 person x 的人中，person y 是最安静的人（也就是安静值 quiet[y] 最小的人）。

示例：

输入：richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]
输出：[5,5,2,5,4,5,6,7]
解释：
answer[0] = 5，
person 5 比 person 3 有更多的钱，person 3 比 person 1 有更多的钱，person 1 比 person 0 有更多的钱。
唯一较为安静（有较低的安静值 quiet[x]）的人是 person 7，
但是目前还不清楚他是否比 person 0 更有钱。

answer[7] = 7，
在所有拥有的钱肯定不少于 person 7 的人中(这可能包括 person 3，4，5，6 以及 7)，
最安静(有较低安静值 quiet[x])的人是 person 7。

其他的答案也可以用类似的推理来解释。
提示：

1 <= quiet.length = N <= 500
0 <= quiet[i] < N，所有 quiet[i] 都不相同。
0 <= richer.length <= N * (N-1) / 2
0 <= richer[i][j] < N
richer[i][0] != richer[i][1]
richer[i] 都是不同的。
对 richer 的观察在逻辑上是一致的。
'''
class Solution:

    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]],
        :type quiet: List[int] quiet = [3,2,5,4,6,1,7,0]
        :rtype: List[int] [5,5,2,5,4,5,6,7]
        """
        # dfs深度搜索和回溯过程就是结果
        #定义dfs搜索
        def dfs(x, map, re, q):
            """
            :param x: 搜索下标
            :param map: 财富关系矩阵
            :param re: 结果向量
            :param q: 安静程度向量
         :return:
            """
            n = len(q)
            for i in range(n):
                # 依次遍历比第x人rich的人i，找到了i深度优先遍历
                # 遍历后回溯过程对re[x]赋值，
                # 更新map[x][i], 表示已经搜索过
                if map[x][i] == 1:
                    dfs(i, map, re, q)
                    if q[re[x]] > q[re[i]]:
                        re[x] = re[i]
                    map[x][i] = -1

        n = len(quiet)
        # n维矩阵存储返回结果，初始化默认值为自身下标
        res = list(range(n))
        # n*n 矩阵存储richer关系list[1][0]，m[i][j]=1 表示 richer 中的元素[j,i]
        mp = [[0 for i in range(n)] for j in range(n)]
        for e in richer:
            mp[e[1]][e[0]] = 1

        for i in range(n):
            dfs(i,mp,res,quiet)
        return res


    def loudAndRich2(self, richer, quiet):
        """
        :type richer: List[List[int]]richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]],
        :type quiet: List[int] quiet = [3,2,5,4,6,1,7,0]
        :rtype: List[int] [5,5,2,5,4,5,6,7]
        """
        quietest = list(range(len(quiet)))
        # print(quietest)
        init_set = set(quietest)
        next_loop = set()
        # print(init_set)
        i = 1
        richers_dict = {}

        for rich in richer:
            richers_dict.setdefault(rich[0],[]).append(rich[1])
            init_set.discard(rich[1])

        loops_rich = list(init_set)

        # 宽度优先遍历规则，
        while (loops_rich):
            # print('loop {0},foreach:{1}:'.format(i,loops_rich))
            for rich in loops_rich:
                for man in richers_dict.get(rich, []):
                    if quiet[quietest[man]] > quiet[quietest[rich]]:
                        quietest[man] = quietest[rich]
                    next_loop.add(man)

            loops_rich = []
            loops_rich.extend(list(next_loop))
            next_loop.clear()

            # print('loop {0},quietest:{1}:'.format(i, quietest))
            i += 1
        return quietest


if __name__ == '__main__':
    sol = Solution()
    richer = [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]]
    quiet = [3, 2, 5, 4, 6, 1, 7, 0]
    print('在所有拥有的钱不少于{}的人中，最安静的人为:'.format(list(range(len(quiet)))))
    print(sol.loudAndRich(richer, quiet))
    print(sol.loudAndRich2(richer, quiet))
