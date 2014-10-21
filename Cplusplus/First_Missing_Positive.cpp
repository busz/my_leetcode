/*
Leetcode : First_Missing_Positive.cpp
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
*/


class Solution {
public:
    int firstMissingPositive(int A[], int n) {
        if(n == 0)
        {
            return 1;
        }
        int pos = 0;
        while(pos < n)
        {
            if(A[pos] - 1 >= 0 && A[pos] - 1 < n)
            {
                if(A[pos] - 1 <= pos)
                {
                    A[A[pos] - 1] = A[pos];
                    pos++;
                }
                else
                {
                    if(A[pos] == A[A[pos]-1])
                        pos++;
                    else
                    {
                        int tmp = A[pos];
                        A[pos] = A[A[pos] - 1];
                        A[tmp - 1] = tmp;
                    }
                }
            }
            else
                pos++;
        }

        for(int i = 0 ; i < n ; i++)
        {
            if(A[i] != i + 1)
                return i+1;
        }
        return n+1;
    }
};
