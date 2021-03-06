/*
Leetcode : 3Sum_Closest.cpp
Given an array S of n integers, find three integers in S such

that the sum is closest to a given number, target. Return the

sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
*/
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int threeSumClosest(vector<int> &num, int target) {
        sort(num.begin() , num.end());

        int result = 100000;
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
                int cV = num[left] + num[right] + num[i];
                if(cV == target)
                {
                    result = target;
                    break;

                }
                else if ( cV < target)
                {
                    left++;
                    if(abs(cV - target) < abs(target - result))
                        result = cV;
                }

                else
                {
                    right--;
                    if(abs(cV - target) < abs(target - result))
                        result = cV;
                }
            }
        }
        return result;
    }
};

int main()
{
    Solution test = Solution();
    int arr[4] = {1 ,1 ,1 ,0};
    vector<int> num(arr , arr+4) ;
    int target = 100;

    int result = test.threeSumClosest(num , target);

    cout<<result<<endl;

}
