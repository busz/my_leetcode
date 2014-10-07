/*
Leetcode : Trapping_Rain_Water.cpp
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
*/
#include <iostream>
using namespace std;
class Solution {
public:
    int trap(int A[], int n) {
        if(n<3)
            return 0;
        int *left = new int[n];
        int *right = new int[n];
        left[0] = 0;
        right[n-1] = 0;
        for(int i = 1 ; i < n ; i++)
        {
            left[i] = max(left[i-1] , A[i-1]);
        }
        for(int i = n - 2 ; i >= 0 ; i--)
        {
            right[i] = max(right[i+1] , A[i+1]);
        }
        int sum = 0;
        for(int i = 1; i < n-1 ; i++)
        {
            int height = min(left[i] , right[i]);
            if(height > A[i])
                sum += height - A[i];
        }
        delete left;
        delete right;
        return sum;
    }
};

int main()
{
    Solution test = Solution();
    int A[] = {2,1,0,2};
    int n = 4;
    cout<<test.trap(A,n)<<endl;
}
