/*
Leetcode : Single_Number_II.cpp
Given an array of integers, every element appears three 

times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. 

Could you implement it without using extra memory?
*/

#include <iostream>

using namespace std;

class Solution {
public:
    int singleNumber(int A[], int n) {
        int one = 0;
        int two = 0;
        for(int i = 0 ; i < n ; i++)
        {
            int tmp;
            tmp = ((one ^ A[i]) & (~two));
            two = ((one & A[i]) | (two & (~A[i])));
            one = tmp;
        }
        return one;
    }
};

