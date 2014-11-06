'''
Created on 2014-2-20

Leetcode :  Remove Element

Problem:
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Solve:

  


@author: xqk
'''


class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        
        #=======================================================================
        # #my method
        # pos = len(A)-1
        # for i in range(len(A)):
        #     if A[i] == elem:
        #         while(A[pos] == elem):
        #             pos = pos - 1
        #             if pos < 0:
        #                 break
        #         if pos < i :
        #             return i
        #         else:
        #             A[i] = A[pos]
        #             A[pos] = elem
        # return pos+1
        #=======================================================================
        
        
        # a easer method
        
        pos = 0
        for i in range(len(A)):
            if A[i] != elem:
                A[pos] = A[i]
                pos = pos + 1
        A = A[:pos+1]
        return pos
    
A = [1]    
#A = [1,2,3,4,1,1,3,1,1,4,5]
elem = 1
test = Solution()
print test.removeElement(A, elem)