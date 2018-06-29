#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@Author: linjie

@license: (C) Copyright 2018-2099,  Limited.

@Contact: jielove1@hotmail.com

@Software: PyCharm

@File: rectangleArea.py

@Date: 2018/6/15 17:35

@Desc:850. 矩形面积 II
我们给出了一个（轴对齐的）矩形列表 rectangles 。 对于 rectangle[i] = [x1, y1, x2, y2]，其中（x1，y1）是矩形 i 左下角的坐标，（x2，y2）是该矩形右上角的坐标。

找出平面中所有矩形叠加覆盖后的总面积。 由于答案可能太大，请返回它对 10 ^ 9 + 7 取模的结果。



示例 1：

输入：[[0,0,2,2],[1,0,2,3],[1,0,3,1]]
输出：6
解释：如图所示。
示例 2：

输入：[[0,0,1000000000,1000000000]]
输出：49
解释：答案是 10^18 对 (10^9 + 7) 取模的结果， 即 (10^9)^2 → (-7)^2 = 49 。
提示：

1 <= rectangles.length <= 200
rectanges[i].length = 4
0 <= rectangles[i][j] <= 10^9
矩形叠加覆盖后的总面积不会超越 2^63 - 1 ，这意味着可以用一个 64 位有符号整数来保存面积结果。
'''
import random

class Solution:
    def rectangleArea(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        # 算法： 拆分区块累计求和
        # 这里把所有矩形的y坐标去重排序后，依次作为分区
        # 计算每个分区里x轴覆盖的宽度 Xi
        # 计算每个分区y的高度 Yi= y[i] - y[i-1]，离散化后每个矩形对区间高度要么全覆盖要么不覆盖
        # 求和Xi * Yi ，累计所以分区得到总覆盖面积
        # 注意边界， 从最小的y[0]开始之上有面积，再最大的有[max]只是没有，防止循环溢界
        # 从下往上依次扫描，可以避免，坐标都是整数

        y_list = []

        for rect in rectangles:
            y_list.extend([rect[1], rect[3]])
        sorted_y = sorted(list(set(y_list)))

        sorted_rects = sorted(rectangles, key=lambda x:(x[0],x[2]))

        # p rint('sorted_rects is :')
        # print(sorted_rects)

        # x轴覆盖长度，对矩形按照(x1,x2)排序依次扫描，方便计算覆盖
        # 一次扫描x轴,若后边的轴的左边界一定是在前一个轴的左端点的右边，
        # 只有 x后[1] <= x前[1], 两个轴才有香蕉
        lens_list = []
        sum_area = []
        y_counts = len(sorted_y)
        for i, y in enumerate(sorted_y):
            start_x, end_x, length = 0, 0, 0
            for rect in sorted_rects:
                if rect[3] <= y or rect[1] > y:
                    continue
                else:
                    if end_x >= rect[0]:
                        if end_x < rect[2]:
                            end_x = rect[2]
                    else:
                        length += (end_x - start_x)
                        start_x, end_x = rect[0], rect[2]
            length += (end_x - start_x)

            lens_list.append(length)
            if i == y_counts - 1:
                break
            sum_area.append((sorted_y[i+1] - sorted_y[i]) * length)
        # print('lens_list:',lens_list)
        return sum(sum_area) % (10**9 + 7)


if __name__ == '__main__':
    sol = Solution()
    rectangles = []
    rand_r = random.randint(1,20)
    for i in range(rand_r):
        x1 = random.randint(1, rand_r)
        y1 = random.randint(1, rand_r)

        vec_x = random.randint(1, rand_r)
        vec_y = random.randint(1, rand_r)

        rectangles.append([x1, y1, vec_x + x1, vec_y + y1])

    # rectangles = [[0, 0, 1, 1], [2, 2, 3, 3]]
    # rectangles = [[0,0,1000000000,1000000000]]

    # print('rectangles :', rectangles)
    # print(rectangles)
    # for rec in rectangles:
    #     print('y is: ', (rec[1],rec[3]))

    print('平面中所有矩形\n{} \n叠加覆盖后的总面积(10 ^ 9 + 7 取模)为：'.format(rectangles))
    print(sol.rectangleArea(rectangles))

