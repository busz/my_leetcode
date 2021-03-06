/*
Leetcode : Search_a_2D_Matrix.cpp
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
*/


class Solution {
public:
    bool searchMatrix(vector<vector<int> > &matrix, int target) {
        int row = 0;
        int height = matrix.size();
        int col = matrix[0].size() - 1;
        while(row < height && col >= 0)
        {
            if(matrix[row][col] == target)
                return true;
            if(matrix[row][col] < target)
                row++;
            else
                col--;
        }
        return false;
    }
};
