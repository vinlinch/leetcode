#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@Author: linjie

@license: (C) Copyright 2018-2099,  Limited.

@Contact: jielove1@hotmail.com

@Software: PyCharm

@File: constructMaximumBinaryTree.py

@Date: 2018/6/20 14:39

@Desc:654. 最大二叉树
给定一个不含重复元素的整数数组。一个以此数组构建的最大二叉树定义如下：

二叉树的根是数组中的最大元素。
左子树是通过数组中最大值左边部分构造出的最大二叉树。
右子树是通过数组中最大值右边部分构造出的最大二叉树。
通过给定的数组构建最大二叉树，并且输出这个树的根节点。

Example 1:

输入: [3,2,1,6,0,5]
输入: 返回下面这棵树的根节点：

      6
    /   \
   3     5
    \    /
     2  0
       \
        1
注意:

给定的数组的大小在 [1, 1000] 之间。

'''

import queue
class TreeNode:
    def __init__(self, x ):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def set_tree(num):
            if len(num) == 1:
                tree = TreeNode(num[0])
                return tree

            # 构造二叉树，定位最大值位置，左右递归调用生成
            max_num = max(num)
            index = num.index(max_num)
            tree = TreeNode(max_num)
            if index > 0:
                tree.left = set_tree(num[:index])
            if index < len(num) - 1:
                tree.right = set_tree(num[index + 1:])
            return tree

        return set_tree(nums)

    def print_bigBTrees(self, nums):
        tree = self.constructMaximumBinaryTree(nums)

        q = queue.Queue()
        q.put(tree)
        while not q.empty():
            a = q.get()
            if a:
                print(a.val, end=',')
                q.put(a.left)
                q.put(a.right)
            else:
                print('null', end=',')


if __name__ == '__main__':
    nums = [3, 2, 1, 6, 0, 5]
    sol = Solution()
    # tree = sol.constructMaximumBinaryTree(nums)
    print("{} 最大二叉树为：".format(nums))
    sol.print_bigBTrees(nums)
