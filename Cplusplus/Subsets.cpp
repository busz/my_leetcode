/*
Leetcode : Subsets

Given a set of distinct integers, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
*/

class Solution {
public:
    vector<vector<int> > subsets(vector<int> &S) {
        sort(S.begin() , S.end());
        int num = pow(2,S.size())
        vector<vector<int> > result;
        for(int i = 0 ; i < num ; i++)
        {
            vector<int> tmp;
            int p = i;
            int pos = 0;
            while(p!=0)
            {
                if(p % 2 == 1)
                {
                    tmp.push_back(S[pos]);
                }
                pos++;
                p /= 2;
            }
            result.push_back(tmp);
        }
        return result;
    }
};
