/*
Leetcode： Search_for_a_Range.cpp

Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
*/
class Solution {
public:
    int search(int A[] ,int n, int left , int right , int target)
    {
        if(left < 0 || right >= n || right < 0 || left >= n)
            return -1;
        while(left <= right)
        {
            int mid = (left + right)/2;
            if(A[mid] == target)
                return mid;
            else if(A[mid] < target)
            {
                left = mid + 1;
            }
            else
                right = mid - 1;
        }
        return -1;
    }
    
    vector<int> searchRange(int A[], int n, int target) {
        vector<int> posVec(2,-1);
        if(n == 0)
            return posVec;
        int left = 0;
        int right = n - 1;
        int pos = search(A , n ,left , right , target);
        if(pos == -1)
            return posVec;
        int start = pos;
        int endP = pos;
        while(1)
        {
            int nPos = search(A , n , left , start-1 , target);
            if(nPos == -1)
                break;
            else
            {
                start = nPos;
            }
        }
        while(1)
        {
            int nPos = search(A , n ,  endP + 1 , right , target);
            if(nPos == -1)
                break;
            else
            {
                endP = nPos;
            }
        }
        posVec[0] = start;
        posVec[1] = endP;
        return posVec;
    }

    
};
