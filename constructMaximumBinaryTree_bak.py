#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@Author: linjie

@license: (C) Copyright 2018-2099,  Limited.

@Contact: jielove1@hotmail.com

@Software: PyCharm

@File: constructMaximumBinaryTree_bak.py

@Date: 2018/6/20 12:26

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


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left_node=None, right_node=None):
        self.val = x
        self.left = left_node
        self.right = right_node

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node


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

            max_num = max(num)
            index = num.index(max_num)
            tree = TreeNode(max_num)
            if index > 0:
                tree.set_left(set_tree(num[:index]))
            else:
                tree.set_left(TreeNode(None))
            if index < len(num)-1:
                tree.set_right(set_tree(num[index+1:]))
            else:
                tree.set_right(TreeNode(None))
            return tree

        def navigate_tree(tree):
            import queue
            q = queue.Queue()
            que_list = []
            q.put(tree)
            while (not q.empty()):
                t = q.get()
                que_list.append(t.val)
                if t.left:
                    q.put(t.left)
                if t.right:
                    q.put(t.right)
            return que_list


        return navigate_tree(set_tree(nums))

if __name__ == '__main__':
    nums = [3, 2, 1, 6, 0, 5]
    sol = Solution()
    print(sol.constructMaximumBinaryTree(nums))
