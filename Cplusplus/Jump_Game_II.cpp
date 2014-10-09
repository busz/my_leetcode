/*
Leetcode : Jump_Game_II.cpp

Given an array of non-negative integers, you are initially positioned 

at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step 
                                                           
from index 0 to 1, then 3 steps to the last index.)
*/

class Solution {
public:
    int jump(int A[], int n) {
        int *arr = new int[n];
        int num = 0;
        int maxD = 0;
        int preMax = 0;
        for(int i = 0 ; i < n ; i++)
        {
            if(i + A[i] > maxD)
                maxD = i + A[i];
            if(i+1 > preMax && i != n-1)
            {
                num++;
                preMax = maxD;
            }
        }
        if(maxD > preMax && preMax < n-1)
            num++;
        delete arr;
        return num;
    }
};
