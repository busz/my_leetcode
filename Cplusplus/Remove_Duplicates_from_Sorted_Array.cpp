/*
Leetcode : Remove_Duplicates_from_Sorted_Array.cpp

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].

*/

#include <iostream>

using namespace std;

class Solution {
public:
    int removeDuplicates(int A[], int n) {
        int num = 0;
        int pos = 0;
        for(int i = 0; i < n ; i++)
        {
            if(i ==0)
            {
                pos++;
                num++;
                continue;

            }

            if(A[i] != A[i-1])
            {
                A[pos] = A[i];
                pos++;
                num++;
            }
        }
        return num;
    }
};

int main()
{
    Solution test = Solution();
    int A[] = {1,1,2};
    int n = 3;
    cout<<test.removeDuplicates(A , n)<<endl;
}
