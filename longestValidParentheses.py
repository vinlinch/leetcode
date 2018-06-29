#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@Author: linjie

@license: (C) Copyright 2018-2099,  Limited.

@Contact: jielove1@hotmail.com

@Software: PyCharm

@File: longestValidParentheses.py

@Date: 2018/6/21 10:33
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
@Desc:

'''


class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        maxlen = 0
        # //1、通过记录匹配括号的位置信息，来确认当前有效字串的最大长度
        # //（由于记录了更多信息，所以能力更强）
        # //2、当栈为空时，表示匹配至此处的整个字符串有效。

        for i, str in enumerate(s):
            if str == ')' and len(stack) > 0 and s[stack[-1]] == '(':
                stack.pop()
                if len(stack) == 0:
                    maxlen = i + 1
                else:
                    # // 记录当前子串有效长度
                    maxlen = max(i - stack[-1], maxlen)

            else:
                stack.append(i)
            # print('loop : {}, stack is {}: max is :{}'.format(i,stack,maxlen))
        return maxlen

    def longestValidParentheses2(self, s):
        dp, stack = [0] * (len(s) + 1), []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    p = stack.pop()
                    dp[i + 1] = dp[p] + i - p + 1
                    # print('p : {}, dp[p]: {}, dp[i+1]:{}'.format(p,dp[p],dp[i+1]))
            # print('loop : {}, stack is {}:  dp[] is {}'.format(i,stack,dp[:i]))
        return max(dp)

    def longestValidParentheses3(self, s):
        """
        :type s: str
        :rtype: int
        """
        # stack[0]都必须有值，
        # 每次'('压入 坐标，遇到')'弹出，
        # 弹出时判断stack是否为空， 空说明没有匹配到'('，压入当前的i;
        # 不为空表示匹配到'(',计算匹配长度为i-stack[-1], 因为前一位存储的都是坐标位
        start = 0
        max_len = 0
        stack = [-1]

        for i in range(start, len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if (len(stack) == 0):
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
            # print('loop: {}, maxlen:{},stack:{} '.format(i, max_len, stack))
        return max_len



if __name__ == '__main__':
    sol = Solution()
    s = "()())(((((()))))))()()()()()(((())))()()"
    print('最长有效括号子串为 :')
    print(sol.longestValidParentheses(s))
    print(sol.longestValidParentheses2(s))
    print(sol.longestValidParentheses3(s))

