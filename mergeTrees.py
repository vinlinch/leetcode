#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@Author: linjie

@license: (C) Copyright 2018-2099,  Limited.

@Contact: jielove1@hotmail.com

@Software: PyCharm

@File: mergeTrees.py

@Date: 2018/7/2 16:44

@Desc:617. 合并二叉树
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

示例 1:

输入:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
输出:
合并后的树:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
注意: 合并必须从两个树的根节点开始。


'''

from constructMaximumBinaryTree import Solution as contree
# Definition for a binary tree node.
import queue
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def createTrees(self, num):
        tlist = []
        for i in num:
            tlist.append(TreeNode(i))
        l = len(num)
        for i in range(l):
            if 2*i + 1 < l:
                tlist[i].left = tlist[2*i + 1]
            if 2*i + 2 < l:
                tlist[i].right = tlist[2*i + 2]
        return tlist[0]
        # root = TreeNode(None)
        # q = queue.Queue()
        # q.put(root)
        # for i in num:
        #     t = q.get()
        #     t = TreeNode(i)
        #     q.put(t.left)
        #     q.put(t.right)
        # return root

        # def dfsTree(t,nums,len,index):
        #     t.val = nums[index]

        # return root


    def printTrees(self,tree):
        q = queue.Queue()
        q.put(tree)
        while not q.empty():
            t = q.get()
            if t:
                print(t.val, end=',')
                q.put(t.left)
                q.put(t.right)
            # else:
            #     print('null', end=',')




    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        def dfs(n1, n2):
            if n1 and n2:
                new_node = TreeNode(n1.val + n2.val)
                new_node.left = dfs(n1.left, n2.left)
                new_node.right = dfs(n1.right, n2.right)
                return new_node
            else:
                return n2 or n1

        return dfs(t1, t2)
if __name__ == '__main__':
    sol = Solution()
    a = [1, 3, 2, 5]
    b = [2, 1, 3, 4,  7]
    t1 = sol.createTrees(b)
    t2 = sol.createTrees(a)
    # sol.printTrees(t1)
    r = sol.mergeTrees(t1,t2)
    sol.printTrees(r)
