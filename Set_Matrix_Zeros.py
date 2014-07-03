'''
Created on 2014-3-22

Leetcoder : set matrix zeros

Problem : 

Given a m x n matrix, if an element is 0, set its entire row and column 
to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.

Could you devise a constant space solution?


@author: xqk
'''

class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        fRow = False
        
        fCol = False
        
        for i in range(m):
            if matrix[i][0] == 0:
                fCol = True
                
        for i in range(n):
            if matrix[0][i] == 0:
                fRow = True;
                
        for i in range(m - 1):
            for j in range(n -1):
                if matrix[i+1][j+1] == 0 :
                    matrix[0][j+1] = 0
                    matrix[i+1][0] = 0
        #print matrix
        for i in range(m - 1):
            if matrix[i+1][0] == 0:
                for j in range(n-1):
                    matrix[i+1][j+1] = 0
        
          
        for i in range(n-1):
            if matrix[0][i+1] == 0:
                for j in range(m-1):
                    matrix[j+1][i+1] = 0
        
       
        if fRow:
            for i in range(n):
                matrix[0][i] = 0;
        
        if fCol:
            for i in range(m ):
                matrix[i][0] = 0;
           
        return matrix
        
        
        
        
matrix = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
test = Solution()
print test.setZeroes(matrix)