'''
Created on 2014.7.26

Leetcode : Pascal's Triangle II

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

'''


class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        r = [1,1];
        for i in range(rowIndex - 1):
            for i in range(len(r) - 1):
                r[i] = r[i] + r[i+1]
            r.insert(0,1);
        return r;
    
    
test = Solution();
print test.getRow(0)
