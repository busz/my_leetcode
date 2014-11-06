# -*- coding:utf-8 -*-
'''
Created on 2014-3-18



leetcoder : maximum subarray

Problem : Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.



@author: xqk
'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if len(A) == 1:
            return A[0];
        maxSum = A[0]
        maxhere = A[0];
        for i in range(len(A) - 1):
            if  maxhere < 0 :
                maxhere = A[i+1];
            else:
                maxhere = maxhere + A[i+1]
            if maxhere > maxSum:
                maxSum = maxhere;
        return maxSum
            
            
                
A = [-2, 1,-3,4,-1,2,1,-5,4]
test = Solution()
print test.maxSubArray(A)