/*
Leetcode : Search_Insert_Position.cpp

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5  2
[1,3,5,6], 2  1
[1,3,5,6], 7  4
[1,3,5,6], 0  0
*/
#include <iostream>

using namespace std;

class Solution {
public:
    int searchInsert(int A[], int n, int target) {
        if(target <= A[0])
            return 0;
        for(int i = 1 ; i < n ; i++)
        {
            if(target > A[i-1] && target <= A[i])
            {
            
                return i;
            }

        }
        return n;
    }
};

int main()
{
    Solution test = Solution();
    int A[] = {1,3,5,6};
    int n = 4;
    int target = 0;
    cout<<test.searchInsert(A , n , target)<<endl;
}
