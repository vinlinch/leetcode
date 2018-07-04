#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@Author: linjie

@license: (C) Copyright 2018-2099,  Limited.

@Contact: jielove1@hotmail.com

@Software: PyCharm

@File: maxProduct.py

@Date: 2018/7/4 11:59

@Desc:318. 最大单词长度乘积
给定一个字符串数组 words，找到 length(word[i]) * length(word[j]) 的最大值，并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。

示例 1:

输入: ["abcw","baz","foo","bar","xtfn","abcdef"]
输出: 16
解释: 这两个单词为 "abcw", "xtfn"。
示例 2:

输入: ["a","ab","abc","d","cd","bcd","abcd"]
输出: 4
解释: 这两个单词为 "ab", "cd"。
示例 3:

输入: ["a","aa","aaa","aaaa"]
输出: 0
解释: 不存在这样的两个单词。
'''


class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        l = len(words)
        mask = [0 for i in range(l)]
        res = 0
        for i in range(l):
            for c in words[i]:
                mask[i] |= (1 << (ord(c) - ord('a')))
            for j in range(i):
                if mask[j] & mask[i] == 0:
                   res = max(res, len(words[i]) * len(words[j]))
        return res



if __name__ == '__main__':
    sol = Solution()
    words = ["abcw","baz","foo","bar","xtfn","abcdef"]
    print('不含相同字符 的两个最大单词长度乘积 : ',sol.maxProduct(words))