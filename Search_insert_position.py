#-*- coding:utf-8 -*-
'''
Created on 2014-2-21

leetcode : search insert position

Problem : 

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 �� 2
[1,3,5,6], 2 �� 1
[1,3,5,6], 7 �� 4
[1,3,5,6], 0 �� 0

solve : search


@author: xqk
'''

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        for i in range(len(A)):
            if A[i] == target:
                return i
            else:
                if target < A[0]:
                    return 0
                elif target > A[-1]:
                    return len(A)
                elif target < A [i] and target > A[i-1]:
                    return i 
                
                    
  
A = [1,3,5,6]
test = Solution()
print test.searchInsert(A, 7)              
