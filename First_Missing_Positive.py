'''
Created on 2014-8-9

Leetcode : First_Missing_Positive

Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.


'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        if A == None or len(A) < 1:
            return 1
        
        pos = 0
        while pos < len(A):
            if pos + 1 != A[pos] and A[pos] > 0\
             and A[pos] < len(A) + 1 and A[pos] != A[A[pos] -1]:
                temp =  A[pos] 
                A[pos] = A[A[pos]-1]
                A[temp-1] = temp 
               
            else:
                pos += 1
              
        
        for i in range(0,len(A)):
            if i+1 != A[i] :
                return i+1
        return len(A) + 1
test = Solution()
#A = [2,1]
A = [3,4,-1,1]
print test.firstMissingPositive(A)
            
