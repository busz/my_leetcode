'''
Created on 2014-3-22

Leetcoder : Pascal's Triangle

Problem : 

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

@author: xqk
'''

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return []
        
        if numRows == 1:
            return [ [1] ];
        A = [ [1] , [1,1] ]
        if numRows ==2:
            return A
        l = 3
        while l <= numRows:
            t = []
            i = 0
            while i < l:
                if i == 0:
                    t.append(1)
                    i = i + 1
                    continue
                if i == l -1:
                    t.append(1)
                    break
                t.append(A[len(A) - 1][i-1]+A[len(A) - 1][i])
                i = i + 1
            l = l + 1
            A.append(t)
        return A
test = Solution()
print test.generate(5)               