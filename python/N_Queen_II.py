'''
Created on 2014-7-3

Leetcode : N que


Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of 
distinct solutions.

'''

class Solution:
    # @return an integer
    def totalNQueens(self, n):
        pos = 0
        A = [0 for i in range(n)]
        return self.subNQueen(A, n, pos)
            
            
    def subNQueen(self , A , n , pos):
        num = 0
        
        for i in range(n):
            A[pos] = i
            flag = True
            j = 0
            while j < pos:
                if A[j] == i or abs(pos - j) == abs(i - A[j]):
                    flag = False
                    break
                j = j + 1
            if flag and pos == n-1:
                num = 1
            elif flag and pos < n - 1:            
                num = num + self.subNQueen(A, n, pos+1)
        
        return num
