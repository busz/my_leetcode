'''
Created on 2014-2-19
leetcode two sum

Problem:

Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2


Solve:

using hash mapping

somebody said, using a hash mapping is cheating 

@author: xqk
'''
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        d = {}
        for i in range(len(num)):
            if target - num[i] in d:
                
                return d[target - num[i]] , i
            else:
                d[num[i]] = i
        
        
num = [-1,-6,11,15]
test = Solution();
print test.twoSum(num, 9)