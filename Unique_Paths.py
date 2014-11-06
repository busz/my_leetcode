'''
Created on 2014-8-5

Leetcode : Unique_Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the
 diagram below).

The robot can only move either down or right at any point in time. The robot is
 trying to reach the bottom-right corner of the grid (marked 'Finish' in the 
 diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

'''
class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        if m==0 or n==0:
            return 0
        if m == 1 or n == 1:
            return 1
        grid = [[0 for i in range(n)] for i in range(m)];
        grid[0][0] = 1
        x , y= 0 , 0
        
        while 1:
            if x < m - 1:
                x = x + 1
            if y < n - 1:
                y = y + 1
            for i in range(x):
                if grid[i][y] != 0:
                    break
                if i - 1 >= 0:
                    grid[i][y] = grid[i][y] + grid[i-1][y]
                if y - 1 >= 0:
                    grid[i][y] = grid[i][y] + grid[i][y-1]
            for j in range(y):
                if grid[x][j] != 0:
                    break
                if j - 1 >= 0:
                    grid[x][j] += grid[x][j-1]
                if x - 1 >= 0:
                    grid[x][j] += grid[x-1][j]
            grid[x][y] = grid[x-1][y] + grid[x][y-1]
            
            if x == m - 1 and y == n - 1:
                break
            
        return grid[m-1][n-1]
test = Solution()
print test.uniquePaths(1, 1)
