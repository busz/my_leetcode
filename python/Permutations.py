'''
Leetcode : Permutations

Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].


'''


class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        if len(num) <2:
            return [num]
            
        r = [];
        
       
        r = self.permuteList(num)
        return r
    def permuteList(self , sortList):
        if len(sortList) == 1:
            return [sortList]
        else:
            result = [];
            for i in range(len(sortList)):
                bak = sortList[:];
                head = bak.pop(i);
                for j in self.permuteList(bak):
                    j.insert(0 , head)
                    result.append(j)
            
            return result
