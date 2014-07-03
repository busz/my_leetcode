'''
Created on 2014-2-19

@author: xqk
'''

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        for i in range(len(A) - 1):
            A[0] = A[0]^A[1+i]
        return A[0]

s = Solution()
A = [1,2,3,1,2,4,4,5,6,6,5]
print s.singleNumber(A)