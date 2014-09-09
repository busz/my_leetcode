/*
Leetcode : 4Sum.cpp

Given an array S of n integers, are there elements a, b, c,

and d in S such that a + b + c + d = target? Find all unique

quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending

order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)

*/
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int> > fourSum(vector<int> &num, int target) {
        sort(num.begin() , num.end());
        vector<vector<int> > result;
        if(num.size()<4)
            return result;
        for(int j = 0 ; j < num.size() - 3 ; j++)
        {
            if(j!=0 && num[j] == num[j-1])
                continue;
            for(int i = j+1 ; i < num.size() - 2 ; i++)
            {
                if(i!= j+1  && num[i] == num[i-1])
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
                    if(num[left] + num[right] + num[i] == target - num[j])
                    {

                        vector<int> tmp;
                        tmp.push_back(num[j]);
                        tmp.push_back(num[i]);
                        tmp.push_back(num[left]);
                        tmp.push_back(num[right]);
                        result.push_back(tmp);


                        left ++;
                    }
                    else if (num[left] + num[right] + num[i] < target - num[j])
                        left++;
                    else
                        right--;
                }
            }
        }
        return result;
    }
};

int main()
{
    Solution test = Solution();
    int arr[6] = {1, 0, -1, 0, -2 ,2};
    vector<int> num(arr , arr+6) ;
    int target = 0;
    vector<vector<int> > result = test.fourSum(num , target);
    for(int i = 0 ; i < result.size() ; i++)
    {
        for(int j = 0 ; j < result[0].size() ;j++)
            cout<<result[i][j]<<" ";
        cout<<endl;
    }
}
