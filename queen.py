#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@Author: linjie

@license: (C) Copyright 2018-2099,  Limited.

@Contact: jielove1@hotmail.com

@Software: PyCharm

@File: queen.py

@Date: 2018/6/22 15:55

@Desc:
八皇后问题：
递归和回溯算法，输出所有可能的解

'''
class Solution:
    def eightQueen(self, n):
        numbers = n
        rec = 2 * numbers - 1
        b = [[0 for i in range(numbers)] for j in range(numbers)]
        b1 = [0 for i in range(numbers)]
        b2 = [0 for i in range(rec)]
        b3 = [0 for i in range(rec)]

        sol_cnt = [0]

        def print_result( a):
            for i in a:
                for j in i:
                    # p = '*' if a[i][j] else '-'
                    print(('X' if j else '.'), end='')
                print('')

        def dsfQueen(i, num, a,a1,a2,a3,cnt):
            if i == num:
                cnt[0] += 1
                print('solution :{}'.format(cnt))
                print_result(a)
                return
            # 判定a[i][j]  能否放皇后
            for j in range(num):
                if a1[j] == 0 and a2[i + j] == 0 and a3[i - j + num -1] == 0:
                    a[i][j], a1[j], a2[i + j], a3[i - j + num -1] = 1, 1, 1, 1
                    dsfQueen(i + 1,numbers, b,b1,b2,b3,sol_cnt)
                    # if cnt[0]:
                    #     return

                    a[i][j], a1[j], a2[i + j], a3[i - j + num-1] = 0, 0, 0, 0

        dsfQueen(0, numbers, b,b1,b2,b3,sol_cnt)

if __name__ == '__main__':
    sol = Solution()
    num = 6
    print('{} 皇后的问题方案有：'.format(num))
    sol.eightQueen(num)







