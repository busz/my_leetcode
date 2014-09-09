/*
Leetcode : 3Sum.cpp

Given an array S of n integers, are there elements a, b,

c in S such that a + b + c = 0? Find all unique triplets

in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

class Solution {
public:
    vector<vector<int> > threeSum(vector<int> &num) {
        sort(num.begin() , num.end());
        vector<vector<int> > result;
        if(num.size()<3)
            return result;

        for(int i = 0 ; i < num.size() - 2 ; i++)
        {
            if(i!= 0  && num[i] == num[i-1])
                continue;
            int left = i+1;
            int right = num.size() - 1;

            while(left < right)
            {
                if(left > i+1 && num[left] == num[left-1])
                {
                    left++;
                    continue;
                }
                if(num[left] + num[right] + num[i] == 0)
                {

                    vector<int> tmp;
                    tmp.push_back(num[i]);
                    tmp.push_back(num[left]);
                    tmp.push_back(num[right]);
                    result.push_back(tmp);


                    left ++;
                }
                else if (num[left] + num[right] + num[i] < 0)
                    left++;
                else
                    right--;
            }
        }
        return result;
    }
};

int main()
{
    Solution test = Solution();
    int arr[6] = {0 ,0 ,0 ,0,0};
    vector<int> num(arr , arr+6) ;

    vector<vector<int> > result = test.threeSum(num);
    for(int i = 0 ; i < result.size() ; i++)
    {
        for(int j = 0 ; j < result[0].size() ;j++)
            cout<<result[i][j]<<" ";
        cout<<endl;
    }
}
