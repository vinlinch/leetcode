#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@Author: linjie

@license: (C) Copyright 2018-2099,  Limited.

@Contact: jielove1@hotmail.com

@Software: PyCharm

@File: findLadders.py

@Date: 2018/6/22 17:01

@Desc:126. 单词接龙 II
给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：

每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回一个空列表。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: []

解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。
'''

import queue

class Solution:
    def isChangeALetter(self,fromword, toword):
        """
        :type beginWord: str
        :type endWord: str
        :return: bool
        """
        # 判读两个给定的字符串，是否能有改变一个字符获得
        if len(fromword) != len(toword):
            return False
        cmp = map(lambda x, y: x != y, list(fromword), list(toword))

        return sum(list(cmp)) == 1

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        # 使用队列按广度优先搜索，当第一次出现endword时，就是最短路径
        # 需要返回所有的路径，所以还需要反向查找
        # print(beginWord)
        # todo 需要解决生成所有路径的效率问题
        if not endWord in wordList:
            return []

        alphabet = [chr(ord('a') + i) for i in range(26)]

        q = queue.Queue()
        words_dict = {}
        words_dict[beginWord] = 0

        # 记录图路径，反向查找输出路径
        word_path = {}
        word_path[0] = [beginWord]
        flag = False
        q.put(beginWord)
        # 广度搜索查找到第一次出现的位置
        while q.not_empty and len(words_dict) <= len(wordList):
            word = q.get()
            for i in range(len(word)):
                for new_word in [word[:i] + alp + word[i+1:] for alp in alphabet if alp != word[i]]:
                    # print(words_dict)
                    if not words_dict.get(new_word,0) and new_word in wordList:
                        words_dict[new_word] = words_dict[word] + 1
                        word_path.setdefault(words_dict[word] + 1,[])
                        word_path[words_dict[word] + 1].append(new_word)
                        # print(words_dict[word] ,word_path.get(words_dict[word] + 1,[]))
                        q.put(new_word)
                    if new_word == endWord:
                        flag = True
                        break
                if flag:
                    break
            if flag:
                break

        # print(words_dict,flag,word_path)
        result_list = []
        temp = []
        result_list.append([endWord])

        # 逆向查找到路径
        if flag:
            for i in sorted(word_path.keys(), reverse=True)[1:]:
                if len(result_list) == 0:
                    for v in word_path[i]:
                        result_list.append([v])
                else:
                    for res in result_list:
                        for v in word_path[i]:
                            if self.isChangeALetter(res[-1], v):
                                temp.append(res[:])
                                temp[-1].append(v)
                    result_list = temp[:]
                    temp = []
        return [res[::-1] for res in result_list]

if __name__ == '__main__':
    sol = Solution()
    beginWord = 'a' # "hit"
    endWord = 'c' #"cog"
    wordList = ['a','b','c'] #'["hot", "dot", "dog", "lot", "log", "cog"]
    # wordList = ["hot", "dot", "dog", "lot", "log"]
    res = sol.findLadders(beginWord, endWord, wordList)
    print('{}和{}的所有单词接龙:'.format(beginWord,endWord))
    # print(res)
    for r in res:
        print(r)







