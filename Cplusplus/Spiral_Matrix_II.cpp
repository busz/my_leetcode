/*
Leetcode : Spiral_Matrix_II.cpp

Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

*/

class Solution {
public:
    vector<vector<int> > generateMatrix(int n) {
        vector<vector<int>> result(n , vector<int>(n,0));
        int direct[][2] = { {0,1} , {1,0} , {0,-1} , {-1,0} };
        int pos = 1;
        int dir = 0;
        int x = 0 ;
        int y = 0;
        while(pos <= n*n)
        {
            result[x][y] = pos;
            pos++;
            if( x+direct[dir][0] <0 || x+direct[dir][0] >= n
               || y+direct[dir][1] < 0 || y+direct[dir][1] >= n
               || result[x+direct[dir][0]][y+direct[dir][1]] != 0 )
            {
                dir++;
                dir = dir%4;
            }
            x += direct[dir][0];
            y += direct[dir][1];
        }
        return result;
    }
};
