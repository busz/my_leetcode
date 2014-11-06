'''
Created on 2014.8.6

Leetcode : Valid_Sudoku

Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. 
Only the filled cells need to be validated.

'''

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        flag = True
        for x in range(9):
            for y in range(9):
                if board[x][y] != '.':
                    char = board[x][y]
                    for i in range(9):
                        if x != i and board[i][y] == char:
                            flag = False
                            break
                        if y != i and board[x][i] == char:
                            flag = False
                            break
                        posX = x - x%3 + i/3
                        posY = y - y%3 + i%3
                        if x !=  posX and y != posY and board[posX][posY] == char:
                            flag = False
                            break
                    if not flag:
                        break
            if not flag:
                break
        return flag
                
