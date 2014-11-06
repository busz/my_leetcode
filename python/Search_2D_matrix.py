'''
Created on 2014-3-20


Leetcoder  : Search a 2D Matrix

Problem : 

Write an efficient algorithm that searches for a value in an m x n matrix. This 
matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.


@author: xqk
'''
class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False;
        end = len(matrix)*len(matrix[0]) - 1
       
        start = 0
        rowNum = len(matrix[0])
        row = (end + start)/2/rowNum
        col = (end + start)/2%rowNum
        while start != end and matrix[row][col] != target :
            if matrix[row][col] > target:
                end = ( start + end )/2 -1
                if start > end:
                    break
            else : 
                start = (start + end) /2 + 1
                
            row = (end + start)/2/rowNum
            col = (end + start)/2%rowNum
            
        #print row ,col
        if matrix[row][col] == target  :
            return True
        else:
            return False
        
#===============================================================================
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
#===============================================================================
matrix = [ [ 1,1] ]

target = 0
test = Solution();
print test.searchMatrix(matrix, target)
        