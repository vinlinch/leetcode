#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@Author: linjie

@license: (C) Copyright 2018-2099,  Limited.

@Contact: jielove1@hotmail.com

@Software: PyCharm

@File: removeDuplicateLetters.py

@Date: 2018/6/20 16:04

@Desc:316. 去除重复字母
给定一个仅包含小写字母的字符串，去除字符串中重复的字母，使得每个字母只出现一次。需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

示例 1:

输入: "bcabc"
输出: "abc"
示例 2:

输入: "cbacdcbc"
输出: "acdb"

'''



class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 因为要字典序，所以一定是先确定那个字母排在第一位，第一个字母确定之后再确定第二个字母。
        # 如何确定第一个字母？首先看有没有a，如果有，尽量把a放在最前，也就是把第一个a之前的字母全部删掉。但是如果有的字母只在第一个a之前出现，那么a就不能放在第一个，否则这个字母的所有副本都会被删掉。如果a不能在第一个位置，就接着看b能不能在第一个位置，以此类推。
        # 确定第一个字母之后，把这个字母之前的字母全部删掉，该字母之后重复出现的也删掉，然后从剩下的字母中字典序最小的字母开始，用同样的方法确定第二个字母。

        lastpos = {}
        for i, str in enumerate(s):
            lastpos[str] = i
        order_strs = sorted(lastpos.keys())
        res = []
        # loop = 1
        # print('lastpos: {}, order_strs:{}'.format(lastpos,order_strs))
        while order_strs:
            # remostr = []
            for str in order_strs:
                p = s.find(str)
                if p <= min(lastpos.values()):
                    res.append(str)
                    # remostr.append(str)
                    order_strs.remove(str)
                    s = ':' * p + s[p:]
                    del lastpos[str]
                    # print('loop: {},pos:{},res:{}'.format(loop,p,res))
                    # loop +=1
                    break

        return ''.join(res)

    def removeDuplicateLetters2(self, s):
        """
        :type s: str
        :rtype: str
        """
        import collections
        remaining = collections.defaultdict(int)
        for c in s:
            remaining[c] += 1

        in_stack, stk = set(), []
        for c in s:
            if c not in in_stack:
                while stk and stk[-1] > c and remaining[stk[-1]]:
                    in_stack.remove(stk.pop())
                stk += c
                in_stack.add(c)
            remaining[c] -= 1
        return "".join(stk)

if __name__ == '__main__':
    import random
    alphabeta = [chr(ord('a') + i) for i in range(26)]
    # s = "bbcaac"
    r = random.Random()
    s = ''.join(r.choices(alphabeta,k=r.randint(2,123)))

    sol = Solution()
    print('{} 去除重复字母后的字符为：'.format(s))
    print(sol.removeDuplicateLetters(s))
    print(sol.removeDuplicateLetters2(s))
