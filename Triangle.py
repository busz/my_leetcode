'''
Created on 2014.8.5

Leetcode : Triangle

Given a triangle, find the minimum path sum from top to bottom.
 Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, 
where n is the total number of rows in the triangle.

'''

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        level = len(triangle);
       
        if level == 0:
            return 0
        if level == 1:
            return triangle[0][0]
       
        level = level - 1
        while level >= 0:
            
            length = len( triangle[level] )
            if level != len(triangle) - 1:
                for i in range(length ):
                    triangle[level][i] += triangle[level+1][i]
            for i in range(length - 1):
                triangle[level][i] = min(triangle[level][i] , triangle[level][i+1])
            level = level - 1
        return triangle[0][0]
test = Solution();
triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
print test.minimumTotal(triangle)
