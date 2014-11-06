'''
Created on 2014-7-30

Leetcode : N-Queens 

The n-queens puzzle is the problem of placing n queens on an n*n chessboard such
that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

'''

class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        
        pos = 0
        A = [0 for i in range(n)]
        r = self.subNQueen(A, n, pos)
        rBoard = []
        for sub in r:
            board = [ ['.' for i in range(n)] for i in range(n) ]
            for i in range(len(sub)):
                board[i][sub[i]] = 'Q'
            newSolution = []
            for subList in board:
                newSolution.append(''.join(subList))
            rBoard.append(newSolution)
        return rBoard
            
            
    def subNQueen(self , A , n , pos):
        r = []
        
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
                r = [ A[:] ]
            elif flag and pos < n - 1:            
                r = r + self.subNQueen(A, n, pos+1)
        
        return r
        
        
        
                
                 
test = Solution()
n = 4
#print test.solveNQueens(n)
print test.solveNQueens(5) 

