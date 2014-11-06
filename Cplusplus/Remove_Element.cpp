/*
Leetcode : Remove_Element.cpp

Given an array and a value, remove all instances

of that value in place and return the new length.

The order of elements can be changed. It doesn't

matter what you leave beyond the new length.
*/

#include <iostream>

using namespace std;

class Solution {
public:
    int removeElement(int A[], int n, int elem) {
        int num = 0;
        for(int i = 0 ; i < n - num ; )
        {
            if(A[i] == elem)
            {
                for(int j = i+1 ; j < n - num ; j++)
                {
                    if(j >= n - num)
                        break;
                    A[j-1] = A[j];
                }
                num++;
            }
            else
                i++;
        }
        return n - num;
    }
};

int main()
{
    Solution test = Solution();
    int A[] = {3,3};
    int n = 2;
    int elem = 3;
    cout<<test.removeElement(A , n , elem)<<endl;

}
