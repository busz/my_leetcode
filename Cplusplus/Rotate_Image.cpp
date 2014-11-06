/*
Leetcode : Rotate_Image.cpp

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
*/

class Solution {
public:
    void rotate(vector<vector<int> > &matrix) {
        int num = matrix.size() -1;
        int base = 0;
        int n = num+1;
        while(n>1)
        {
            for(int i = 0 ; i < n - 1 ; i++)
            {
                int tmp = matrix[base][base + i];
                matrix[base][base + i] = matrix[num - base - i][base];
                matrix[num - base - i][base] = matrix[num - base][num - base - i];
                matrix[num - base][num - base - i] = matrix[base + i][num - base];
                matrix[base + i][num - base] = tmp;
            }
            n = n - 2;
            base++;
        }
    }
};
