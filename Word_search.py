'''
Created on 2014-7-31

Leetcode : Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.


'''

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
       
        board = [ [ k for k in board[l] ] for l in range(len(board) ) ];
        print board
        flag = False
        for i in range(len(board) ):
            for j in range(len(board[0])):
                
              
                
                flag = self.find(board, word,  i, j)
                
                
                if flag:
                    break
            if flag:
                break
        return flag
    
    def find(self , board , word  , x , y):
       
        if len(word) == 0:
            return True
        if x < 0  or y < 0 or x >= len(board) or y >= len(board[0]):
            return False
        
        if board[x][y] == word[0]:
            t , board[x][y] = board[x][y] , ' '
            flag = self.find(board, word[1:],  x+1, y) or self.find(board, word[1:],  x-1, y) \
                or self.find(board, word[1:],  x, y-1) or self.find(board, word[1:],  x, y+1)
            if not flag :
                board[x][y] = t
            return flag
        else:
            
            return False
test = Solution()

board = ["ab" , 'cd']
word = 'acdb'

print test.exist(board, word)
