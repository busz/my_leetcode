'''
Created on 2014-7-31

Leetcode : Jump Game

Given an array of non-negative integers, you are initially positioned at the 
first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

'''
class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        
        max = 0
        for i in range(len(A) - 1):
            if i <= max :
                cmax = i + A[i]
                max = max if max > cmax else cmax
            else:
                break
        return max >= len(A) -1
            
test = Solution()
A = [2,3,1,1,4]
print test.canJump(A)
