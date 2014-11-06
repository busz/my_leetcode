'''
Created on 2014-8-19

Leetcode : 3Sum_Closest

Given an array S of n integers, find three integers in S such that the sum is 

closest to a given number, target. Return the sum of the three integers. You 

may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        diff = 1000000000
        r = 0
        num.sort()
        for i in range(len(num) - 2):
            left = i + 1
            right = len(num) - 1
            while left < right:
                newDiff = num[i] + num[left] + num[right] - target
                if newDiff > 0:
                    right = right - 1
                elif newDiff == 0:
                    return target
                else:
                    left = left + 1
                if abs(newDiff) < diff:
                    r = newDiff + target
                    diff = abs(newDiff)
                 
        return r
    
    
test = Solution()
num = [-1,2,1,-4]
target = 1
num = [1,1,1,0]
target = -100
print test.threeSumClosest(num, target)
