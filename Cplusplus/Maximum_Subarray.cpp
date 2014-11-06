/*
Leetcode : Maximum_Subarray.cpp

Find the contiguous subarray within an array (containing at

least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.
*/

#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int maxSubArray(int A[], int n) {
        vector<int> arr(n,0);
        int maxV = A[0];
        arr[0] = A[0];
        for(int i = 1 ; i < n ; i++)
        {
            if(arr[i-1] > 0 && arr[i-1] + A[i]>0)
            {
                arr[i] = arr[i-1] + A[i];
            }
            else
            {
                arr[i] = A[i];
            }
            if(arr[i] > maxV)
                maxV = arr[i];

        }
        return maxV;
    }
};

int main()
{
    Solution test = Solution();
    int A[] = {-2,1,-3,4,-1,2,1,-5,4};
    int n = 9;
    cout<<test.maxSubArray(A , n)<<endl;
}
