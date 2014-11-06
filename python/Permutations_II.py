'''
Created on 2014.7.23

Leetcode : Permutations

Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

@author: xqk
'''
import time

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        if len(num) <2:
            return num
            
        r = [];
        num.sort()
        
       
        r = self.permuteList(num)
        return r
    def permuteList(self , sortList):
        if len(sortList) == 1:
            return [sortList]
        else:
            result = [];
            for i in range(len(sortList)):
                bak = sortList[:];
                if i!= 0 and bak[i] == bak[i-1]:
                    continue
                head = bak.pop(i);
                for j in self.permuteList(bak):
                    j.insert(0 , head)
                    result.append(j)
                    
            return result
        

start = time.clock()      
        
test = Solution();

n = 4
num = [1,1,2]

print test.permute(num)
end = time.clock()
print end - start
