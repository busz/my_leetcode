/*
Leetcode : Pascal_s_Triangle.cpp

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
*/

class Solution {
public:
    vector<vector<int> > generate(int numRows) {
        vector<vector<int>> result;
        if(numRows == 0)
            return result;
        result.push_back(vector<int> tmp(1,1));
        if(numRows == 1)
        {
            return result;
        }
        result.push_back(vector<int> tmp(2,1));
        if(numRows == 2)
        {
            return result;
        }
        for(int i = 2 ; i < numRows ; i++)
        {
            vector<int> tmp(i+1 , 1);
            int vecSize = result.size() - 1;
            for(int j = 1 ; j < i ; j++)
            {
                tmp[j] = result[vecSize][j-1] + result[vecSize][j];
            }
            result.push_back(tmp);
        }
        return result;
    }
};
