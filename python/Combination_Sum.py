'''
Created on 2014.8.4

Leetcode : Combination Sum 

Given a set of candidate numbers (C) and a target number (T), find all unique 
combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2,... , ak) must be in non-descending order. 
(ie, a1 <= a2 <=... <= ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7, 
A solution set is: 
[7] 
[2, 2, 3] 

'''

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        
        candidates.sort()
        candidates.reverse();
        
        return self.combinSum(candidates, target)
    def combinSum(self , candidates , target):
        r = []
        while len(candidates) > 0 and candidates[0] > target:
            candidates = candidates[1:]
        
        if len(candidates) > 0 and candidates[0] == target:
            r.append([target])
            candidates = candidates[1:]
            
        if len(candidates) == 0:
            return r    
        
        if len(candidates) == 1:
            if target%candidates[0] == 0:
                newPrefix = []
                while target != 0:
                    newPrefix.append(candidates[0])
                    target = target - candidates[0]
                r.append(newPrefix)
            return r
        
        for i in range(len(candidates)):
            num = 1
            while num*candidates[i] <= target:
                postfix = [];
                for j in range(num):
                    postfix.append(candidates[i])
                if target - num*candidates[i] == 0:
                    r.append(postfix)
                else:
                    prefix = self.combinSum(candidates[i+1:], target - num*candidates[i])
                    if len(prefix) != 0:
                        for item in prefix:
                            r.append(item + postfix)
                        
                num = num + 1
        return r
            
test = Solution()
candidates = [2,3,5]
target = 7
print test.combinationSum(candidates, target)
