'''
Created on 2014-8-18

Leetcode : Combination_Sum_II

Given a collection of candidate numbers (C) and a target number (T), find all 

unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, ... , ak) must be in non-descending order. 

(ie, a1 <= a2 <= ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
A solution set is: 
[1, 7] 
[1, 2, 5] 
[2, 6] 
[1, 1, 6] 

'''

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        candidates.sort()
       
        r = self.combine(candidates, target)
        return r
        
        
    def combine(self , cand , target):
        r = []
        if not cand or target < cand[0]:
            return r
        
        for i in range(len(cand)):
            if cand[i] > target:
                break
            elif cand[i] == target:
                r.append([cand[i]])
                break
            else:
                part = self.combine(cand[i+1:], target - cand[i])
                if part:
                    newr = [ [cand[i] ] + item for item in part  ]
                    for item in newr:
                        if item not in r:
                            r.append(item)
        
        return r
       
        
test = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
print test.combinationSum2(candidates, target)
