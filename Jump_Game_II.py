'''
Created on 2014-7-31

Leetcode : Jump Game II

Given an array of non-negative integers, you are initially positioned at 
the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from 
index 0 to 1, then 3 steps to the last index.)


'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        cmax = 0
        jump = 0
        step = 0
        for i in range(len(A) - 1):
            cmax = max(cmax , A[i] + i)
            if i == jump:
                jump = cmax
                step += 1 
        return step 
test = Solution()
A = [2,3,1]
print test.jump(A)
