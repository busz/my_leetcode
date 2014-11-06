'''
Created on 2014.7.31
Leetcode : Combinations 

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

'''

class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        
        if n < k:
            return []
        if n == k:
            return [range(1,n+1)]
        if k == 1:
            r = []
            for i in range(n):
                r.append([i+1])
            return r
        else:
            subR = self.combine(n-1, k-1)
            for sub in subR:
                sub.append(n);
            subR += self.combine(n-1, k)
            return subR
test = Solution();
print test.combine(4, 2)
        
