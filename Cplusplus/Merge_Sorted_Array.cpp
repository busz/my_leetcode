/*
Leetcode : Merge_Sorted_Array.cpp

Given two sorted integer arrays A and B, merge B into A as one sorted array.

Note:
You may assume that A has enough space (size that is greater or equal to m + n) 

to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.
*/

class Solution {
public:
    void merge(int A[], int m, int B[], int n) {
        int aP = m - 1;
        int bP = n - 1;
        int p = m + n - 1;
        while( aP >=0 && bP >= 0)
        {
            if(A[aP] > B[bP])
            {
                A[p] = A[aP];
                p--;
                aP--;
            }
            else
            {
                A[p] = B[bP];
                bP--;
                p--;
            }
        }
        if(bP >= 0)
        {
            for(int i = 0 ; i <= bP ; i++)
            {
                A[i] = B[i];
            }
        }
    }
};
