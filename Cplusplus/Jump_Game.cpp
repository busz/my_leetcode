/*
Leetcode : Jump_Game.cpp

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
*/

class Solution {
public:
    bool canJump(int A[], int n) {
        int *dis = new int[n];
        int maxD = 0;
        for(int i = 0 ; i < n ; i++)
        {
            if( i + A[i] > maxD)
                maxD = i + A[i];
            if(maxD < i+1 && i != n-1)
                return false;
        }
        delete[] dis;
        if(maxD >= n-1)
            return true;
        else
            return false;
    }
};
