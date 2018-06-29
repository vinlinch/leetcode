#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@Author: linjie

@license: (C) Copyright 2018-2099,  Limited.

@Contact: jielove1@hotmail.com

@Software: PyCharm

@File: ExamRoom.py

@Date: 2018/6/26 11:13

@Desc:855. 考场就座
在考场里，一排有 N 个座位，分别编号为 0, 1, 2, ..., N-1 。

当学生进入考场后，他必须坐在能够使他与离他最近的人之间的距离达到最大化的座位上。如果有多个这样的座位，他会坐在编号最小的座位上。(另外，如果考场里没有人，那么学生就坐在 0 号座位上。)

返回 ExamRoom(int N) 类，它有两个公开的函数：其中，函数 ExamRoom.seat() 会返回一个 int （整型数据），代表学生坐的位置；函数 ExamRoom.leave(int p) 代表坐在座位 p 上的学生现在离开了考场。请确保每次调用 ExamRoom.leave(p) 时都有学生坐在座位 p 上。



示例：

输入：["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[],[4],[]]
输出：[null,0,9,4,2,null,5]
解释：
ExamRoom(10) -> null
seat() -> 0，没有人在考场里，那么学生坐在 0 号座位上。
seat() -> 9，学生最后坐在 9 号座位上。
seat() -> 4，学生最后坐在 4 号座位上。
seat() -> 2，学生最后坐在 2 号座位上。
leave(4) -> null
seat() -> 5，学生最后坐在 5 号座位上。


提示：

1 <= N <= 10^9
在所有的测试样例中 ExamRoom.seat() 和 ExamRoom.leave() 最多被调用 10^4 次。
调用 ExamRoom.leave(p) 时需要确保当前有学生坐在座位 p 上。
'''

class ExamRoom:
    def __init__(self, N):
        """
        :type N: int
        """
        self.seats = set()
        self.n = N

    def seat(self):
        """
        :rtype: int
        """
        if len(self.seats) == 0:
            self.seats.add(0)
            return 0
        else:
            start = -1
            max_dist = -1
            p = -1
            for i in sorted(self.seats):
                if start == -1:
                    max_dist = i
                    p = 0
                else:
                    dist = (i - start)//2
                    if dist > max_dist:
                        max_dist = dist
                        p = (start + i)//2
                start = i
            if self.n - 1 - start > max_dist:
                p = self.n - 1
                max_dist = self.n - 1 - start
            self.seats.add(p)
        return p



    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        if p in self.seats:
            self.seats.remove(p)

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)