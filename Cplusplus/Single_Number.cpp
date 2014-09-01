/*
Leetcode : Single_Number.cpp
Given an array of integers, every element appears twice
except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?


*/

#include <iostream>
using namespace std;

class Solution {
public:
    int singleNumber(int A[], int n) {
        for(int i = 1 ; i < n ; i++)
        {
            A[0] = A[0]^A[i];
        }
        return A[0];
    }
};

int main()
{
    Solution test = Solution();
    int A[] = { 1, 1,0,2,0,3,3};
    cout<<test.singleNumber(A , 7)<<endl;
    return 0;
}
