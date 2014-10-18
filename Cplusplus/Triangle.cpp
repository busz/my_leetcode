/*
Leetcode : Triangle.cpp
Given a triangle, find the minimum path sum from 

top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, 

where n is the total number of rows in the triangle.
*/

class Solution {
public:
    int minimumTotal(vector<vector<int> > &triangle) {
        if(triangle.size() == 0)
            return 0;
        if(triangle.size() == 1)
        {
            return triangle[0][0];
        }
        for(int i = 1 ; i < triangle.size()  ; i++)
        {
            triangle[i][0] += triangle[i-1][0];
            for(int j = 1 ; j < triangle[i].size() - 1; j++)
                triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j]);
            triangle[i][triangle[i].size()-1] += triangle[i-1][triangle[i].size()-2];
        }
        int xLength = triangle.size()-1;
        int yLength = triangle[xLength].size()-1;
        int minV = triangle[xLength][0];
        for(int i = 1 ; i <= yLength ; i++)
            if(triangle[xLength][i] < minV)
                minV = triangle[xLength][i] ;
        return minV;
    }
};
