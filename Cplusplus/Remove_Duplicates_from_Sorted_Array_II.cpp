/*
lEETCODE : Remove_Duplicates_from_Sorted_Array_II.cpp
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].
*/
class Solution {
public:
    int removeDuplicates(int A[], int n) {
        if(n<3)
            return n;
        int pos = 1;
        int num = 1;
        int pre = A[0];
        for(int i = 1 ; i < n ; i++)
        {
            if(A[i] == pre)
            {
                num ++;
                if(num >= 3)
                {
                    continue;
                }
                A[pos] = A[i];
                pos++;
            }
            else
            {
                pre = A[i];
                num = 1;
                A[pos] = A[i];
                pos++;
            }
        }
        return pos;
    }
};
