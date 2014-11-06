'''
Created on 2014-2-20

Leetcode : Single number II

Problem:

Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Solve :
 mode 3 XOR


@author: xqk
'''

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        
        one = 0
        two = 0
        xorThree = 0
        for i in range(len(A)):
            two = two | (one & A[i])
            one = one ^ A[i]
            xorThree = ~( one & two )
            one  = one & xorThree
            two = two & xorThree
        return one
    
A = [ 1,1,1,4 ]
test = Solution()
print test.singleNumber(A)
            