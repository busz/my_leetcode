'''
Leetcode : Minimum_Path_Sum 

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

@author: xqk
'''

class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        for i in range(len(grid) - 1):
            grid[i+1][0] = grid[i][0]+grid[i+1][0];
        for i in range(len(grid[0]) - 1):
            grid[0][i+1] = grid[0][i] + grid[0][i+1];
        for j in range(len(grid[0]) - 1):
            for i in range(len(grid) - 1):
                if grid[i][j+1] > grid[i+1][j]:
                    grid[i+1][j+1] = grid[i+1][j] + grid[i+1][j+1]
                else:
                    grid[i+1][j+1] = grid[i][j+1] + grid[i+1][j+1]
        return grid[len(grid)-1][len(grid[0])-1];
