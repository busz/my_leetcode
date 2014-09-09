/*

Leetcode : Climbing_Stairs.cpp

You are climbing a stair case. It takes n

steps to reach to the top.

Each time you can either climb 1 or 2 steps.

 In how many distinct ways can you climb to

 the top?
*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int climbStairs(int n) {
        if(n < 3)
            return n;

        vector<int> num(n,0);
        num[0] = 1;
        num[1] = 2;
        for(int i = 2 ; i < n ; i++)
        {
            num[i] = num[i-1]+num[i-2];
        }
        return num[num.size() -1];
    }
};

int main()
{
    Solution test = Solution();
    int n = 10;
    cout<<test.climbStairs(n)<<endl;

}
