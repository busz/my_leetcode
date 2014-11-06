'''
Created on 2014.7.31

Leetcode : Subsets

Given a set of distinct integers, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

'''

class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        r = []
        n = 2**(len(S));
        S.sort()
        for i in range(n):
            k = i
            subset = []
            p = 0
            while k:
                if k & 1:
                   
                    subset.append(S[p])
                k = k >> 1;
                p = p + 1
               
            r.append(subset)
        return r
test = Solution();
S = [4,1,0]
print test.subsets(S)
            
