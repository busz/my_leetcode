'''
Created on 2014-8-8

Leetcode : Longest_Consecutive_Sequence

Given an unsorted array of integers, find the length of the longest consecutive 

elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

'''

class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        if len(num) == 0:
            return 0
        
        maxLen = 0
        
        setA = set()
        for item in num:
            setA.add(item)
            
        for item in num:
            n = 1
            v = item - 1
            while v  in setA:
                n += 1
                setA.remove(v)
                v -= 1
            v = item + 1
            while v in setA:
                n += 1
                setA.remove(v)
                v += 1
            if n > maxLen:
                maxLen = n
        
        return maxLen
                

test = Solution()
#num = [100, 4, 200, 1, 3, 2]
#num = [2147483646,-2147483647,0,2,2147483644,-2147483645,2147483645]
num = [1,2,0,1]
print test.longestConsecutive(num)
                
