'''
Created on 2014-3-27

Leetcoder : Maximal Rectangle 

Problem : 

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle 
containing all ones and return its area.


@author: xqk
'''

class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        nMatrix = [ [0 for i in range(len(matrix[0]))] for i in range(len(matrix)+1) ]
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                nMatrix[x][y] = int(matrix[x][y])
        matrix = nMatrix
        
        for x in range(len(matrix)-1):
            for y in range(len(matrix[0]) ):
                if matrix[x][y] == 0:
                    continue
                for i in range(y+1,len(matrix[0])):
                    if matrix[x][i] != 1:
                        break
                    matrix[x][y] += 1
        
        
        for y in range(len(matrix[0])):
            stack = []
            i = 0
            maxV = 0
            while i < len(matrix):
                
                if not stack or matrix[stack[-1]][y] < matrix[i][y]:
                    stack.append(i)
                    i += 1
                else:
                    pos = stack[-1]
                    stack = stack[:-1]
                    
                    
                    maxV = max( maxV , matrix[pos][y]*( i if not stack else i -1  - stack[-1]) )
                    #print i , maxV
            matrix[-1][y] = maxV
        return max(matrix[-1][:])  
test = Solution()
print test.maximalRectangle(["0010","1111","1111","1110","1100","1111","1110"])
        
                
