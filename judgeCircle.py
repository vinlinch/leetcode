#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@Author: linjie

@license: (C) Copyright 2018-2099,  Limited.

@Contact: jielove1@hotmail.com

@Software: PyCharm

@File: judgeCircle.py

@Date: 2018/6/20 11:38

@Desc:657. 判断路线成圈
初始位置 (0, 0) 处有一个机器人。给出它的一系列动作，判断这个机器人的移动路线是否形成一个圆圈，换言之就是判断它是否会移回到原来的位置。

移动顺序由一个字符串表示。每一个动作都是由一个字符来表示的。机器人有效的动作有 R（右），L（左），U（上）和 D（下）。输出应为 true 或 false，表示机器人移动路线是否成圈。

示例 1:

输入: "UD"
输出: true
示例 2:

输入: "LL"
输出: false
'''


class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # 判断字符的个数是否相等
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')

if __name__ == '__main__':
    moves = 'UD'
    sol = Solution()
    print('经过路线{}后，是否会移回到原来的位置？：'.format(moves))
    print(sol.judgeCircle(moves))
