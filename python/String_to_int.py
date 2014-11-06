# -*- coding: utf-8 -*-
'''
Created on 2014.10.14

Leetcode : String_to_int.py

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases.

If you want a challenge, please do not see below and

ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified

vaguely (ie, no given input specs). You are responsible

to gather all the input requirements up front.


'''


class Solution:
    # @return an integer
    def atoi(self, str):
        if not str:
            return 0
        MAX = (1 << 31) - 1
        flag = 1
        while str[0] == ' ':
            str = str[1:]
        if not str:
            return 0
        if str[0] == '-':
            flag = -1
            str = str[1:]
        elif str[0] == '+':
            str = str[1:]
        sumV = 0
        while 1:
            if '0' <= str[0] <= '9':
                sumV = sumV * 10 + int(str[0]) - int('0')
            elif str[0] == '-' or str[0] == '+':
                return 0
            else:
                break
            if len(str) > 1:
                str = str[1:]
            else:
                break
        sumV = sumV * flag
        if sumV > MAX:
            sumV = MAX
        elif sumV < - MAX - 1:
            sumV = -MAX - 1
        return sumV


test = Solution()
str = ''
print test.atoi(str)
