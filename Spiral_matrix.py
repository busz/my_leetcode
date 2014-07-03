'''
Created on 2014-3-25

Leetcoder : spiral matrix 

problem : 
Given a matrix of m x n elements (m rows, n columns), return all elements of 
the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].

@author: xqk
'''

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return None;
        m = len(matrix)
        n = len(matrix[0])
        
        A = []
        mp = 0
        np = 0
        rA = [ [0,1] , [0,-1] , [-1,0] , [1,0] ]
        fM = [ [ 0 for i in range(n)] for i in range(m)]
        #left 0 , right 1  , up 2 , down 3
        r = 0 
        e = 0
        end = [0,0]
        while e <3:
            
            while self.inRange(mp , m) and self.inRange(np , n) and fM[mp][np] == 0:
                fM[mp][np] = 1;
                
                A.append(matrix[mp][np])
                mp = mp + rA[r][0]
                np = np + rA[r][1]
               
            mp = mp - rA[r][0]
            np = np - rA[r][1]
            
            r = self.changeR(r)
            if end[0] == mp and end[1] == np:
                e = e + 1;
            else:
                e = 0
                end[0] = mp
                end[1] = np
            mp = mp + rA[r][0]
            np = np + rA[r][1]
            
        return A
    def inRange(self , p , maxV):
        if p>= 0 and p < maxV:
            return True
        else:
            return False
            
    def changeR(self , r):
        if r == 0:
            return 3
        if r == 1 :
            return 2
        if r == 2 :
            return 0
        if r == 3:
            return 1
        
matrix  = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
matrix = [[3],[2]]
test = Solution()
print test.spiralOrder(matrix)
        