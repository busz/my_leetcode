'''
Created on 2014.7.24

Leetcode : Spiral Matrix II

Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]


'''

class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        mat = [ [0 for i in range(n) ] for i in range(n)];
       
        num = 1;
        i = 0;
        j = 0;
        
        #status: 1 left , 2 down , 3 right , 4 up
        status = 0;
        move = [ [0,1] , [1,0] , [0,-1] ,[-1,0] ]
        
        
        while num <= n*n:
            
            mat[i][j] = num;
            newI = i + move[status][0];
            newJ = j + move[status][1]
            num = num+1;
              
            if  newI < n and  newJ < n and mat[newI][newJ] ==0:
                
                
                i = newI
                j = newJ
            else:
                status = (status + 1)%4
                i = i + move[status][0];
                j = j + move[status][1]
        return mat
    
    
test = Solution();
print test.generateMatrix(3)    
            
