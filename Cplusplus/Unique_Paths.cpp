/*
Leetcode : Unique_Paths.cpp
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.
*/

class Solution {
public:
    int uniquePaths(int m, int n) {
        if(m ==0  || n == 0)
            return 0;
        if( m== 1 || n==1)
            return 1;
        vector<vector<int>> arr;
        arr.push_back(vector<int>(n,1));
        for(int i = 0 ; i < m ; i++)
        {
            vector<int> tmp(n,0);
            tmp[0] =1;
            arr.push_back(tmp);
        }
        for(int i = 1 ; i < m ; i++)
        {
            for(int j = 1 ; j < n ; j++)
                arr[i][j] = arr[i-1][j] + arr[i][j -1];
        }
        return arr[m-1][n-1];
            
            
    }
};
