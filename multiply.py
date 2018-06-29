#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@Author: linjie

@license: (C) Copyright 2018-2099,  Limited.

@Contact: jielove1@hotmail.com

@Software: PyCharm

@File: multiply.py

@Date: 2018/6/22 11:38

@Desc:
不直接用bigint， 计算两个数字的乘积，并返回结果的字符串
'''


class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        if num1 == '0' or num2 == '0':
            return '0'
        len1 = len(num1)
        len2 = len(num2)
        prod_sum = [0] * (len1 + len2)

        for i in range(len1):
            for j in range(len2):
                prod_sum[i+j] += int(num1[len1-1-i]) * int(num2[len2-1-j])


        divid = 0
        for i,p in enumerate(prod_sum):
            prod_sum[i] = (divid + p) % 10
            divid = (divid + p) // 10

        return ''.join(map(str,prod_sum))[::-1].lstrip('0')

    def multiply2(self, num1, num2):

        len1 = len(num1)
        len2 = len(num2)

        max_num = num1[::-1] if len1 >= len2 else num2[::-1]
        min_num = num2[::-1] if len2 <= len1 else num1[::-1]

        max_len = max(len1, len2)
        min_len = min(len1, len2)

        # print("max :{}, min:{}, max_len:{}, minlen:{}".format(max_num,min_num,max_len,min_len))

        divid_sum = 0
        prod_num = ''
        for i in range(max_len):

            cur_sum = 0
            p0 = int(max_num[i])
            for j, p in enumerate(min_num):
                if j <= i:
                    cur_sum += p0 * int(p) * 10**j
                else:
                    break

            if i < min_len:
                p0 = int(min_num[i])
                for j, p in enumerate(max_num):
                    if j < i:
                        cur_sum += p0 * int(p) * 10**j
                    else:
                        break

            prod_num += str((divid_sum + cur_sum) % 10)
            divid_sum = (divid_sum + cur_sum) // 10

            # print('loop:{}, divid_sum:{},prod_num:{},cur_sum:{}'.format(i,divid_sum,prod_num,cur_sum))

        while divid_sum:
            prod_num += str(divid_sum % 10)
            divid_sum = divid_sum // 10

        return str(prod_num)[::-1]

if __name__ == '__main__':
    sol = Solution()
    num1, num2 = '123', '456'
    print('数值 {} 和 {}相乘的积为：'.format(num1, num2))
    print(sol.multiply(num1,num2))
    print(sol.multiply2(num1, num2))
