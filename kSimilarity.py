#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@Author: linjie

@license: (C) Copyright 2018-2099,  Limited.

@Contact: jielove1@hotmail.com

@Software: PyCharm

@File: kSimilarity.py

@Date: 2018/6/27 18:30

@Desc:854. 相似度为 K 的字符串
如果可以通过将 A 中的两个小写字母精确地交换位置 K 次得到与 B 相等的字符串，我们称字符串 A 和 B 的相似度为 K（K 为非负整数）。

给定两个字母异位词 A 和 B ，返回 A 和 B 的相似度 K 的最小值。



示例 1：

输入：A = "ab", B = "ba"
输出：1
示例 2：

输入：A = "abc", B = "bca"
输出：2
示例 3：

输入：A = "abac", B = "baca"
输出：2
示例 4：

输入：A = "aabc", B = "abca"
输出：2


提示：

1 <= A.length == B.length <= 20
A 和 B 只包含集合 {'a', 'b', 'c', 'd', 'e', 'f'} 中的小写字母。

'''