/*
Leetcode : Minimum_Path_Sum.cpp

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
*/

class Solution {
public:
    int minPathSum(vector<vector<int> > &grid) {
        int width = grid[0].size();
        int height = grid.size();
        for(int i = 1 ; i < width ; i++)
            grid[0][i] += grid[0][i-1];
        for(int i = 1 ; i < height ; i++)
            grid[i][0] += grid[i-1][0];
        for(int x = 1 ; x < height ; x++)
        {
            for(int y = 1 ; y < width ; y++)
            {
                grid[x][y] += min(grid[x-1][y],grid[x][y-1]);
            }
        }
        return grid[height -1 ][width -1 ];
    }
};
