'''
Created on 2014-8-5

Leetcode : Unique_Paths_II

Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths
 would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.

'''

class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        if len(obstacleGrid) == 0:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
       
        grid = [ [ 0 for i in range(n)] for i in range(m) ]
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            grid[0][0] = 1
        
        short = min(m,n)
        
        for pos in range(1, short ):
            for x in range(pos):
                if obstacleGrid[x][pos] != 1:
                    if x != 0:
                        grid[x][pos] += grid[x-1][pos]
                    
                    grid[x][pos] += grid[x][pos-1]
                    
            for y in range(pos):
                if obstacleGrid[pos][y] != 1:
                    if y != 0:
                        grid[pos][y] += grid[pos][y-1]
                    grid[pos][y] += grid[pos - 1][y]
            if obstacleGrid[pos][pos] != 1:
                grid[pos][pos] = grid[pos - 1][pos] + grid[pos][pos-1]
            
        for pos in range( short , m):
            for y in range(0 , n):
                if obstacleGrid[pos][y] != 1:
                    if y != 0:
                        grid[pos][y] += grid[pos][y - 1]
                    if pos >= 1:
                        grid[pos][y] += grid[pos - 1][y]
                   
        for pos in range( short , n):
            for x in range(0 , m):
                if obstacleGrid[x][pos] != 1:
                    
                    if x != 0:
                        grid[x][pos] += grid[x-1][pos]
                    if pos >= 1:
                        grid[x][pos] += grid[x][pos-1]
                    
        
        
        return grid[-1][-1]    
    
                
test = Solution()
obstacleGrid = [[0]]#[[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,0]]
print test.uniquePathsWithObstacles(obstacleGrid)
        
            
