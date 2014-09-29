/*
Sort_Colors.cpp

Given an array with n objects colored red, white

or blue, sort them so that objects of the same

color are adjacent, with the colors in the order

red, white and blue.

Here, we will use the integers 0, 1, and 2 to

represent the color red, white, and blue

respectively.

Note:
You are not suppose to use the library's sort

function for this problem.

*/
#include <iostream>
using namespace std;

class Solution {
public:
    void sortColors(int A[], int n) {
        int left = 0;
        int right = n - 1;
        int pos = 0;
        while(pos <= right)
        {
            if(A[pos] == 0)
            {
                
                int tmp = A[pos];
                A[pos] = A[left];
                A[left] = tmp;
                left++;
                
                pos++;
                

            }
            else if(A[pos] == 2)
            {
                while(right > pos && A[right] == 2)
                {
                    right--;
                }

                int tmp = A[right];
                A[right] = A[pos];
                A[pos] = tmp;
                right--;

            }
            else
                pos++;

        }
    }
};

int main()
{
    Solution test = Solution();
    int A[] = {2,2};
    int n = 2;
    test.sortColors(A,n);
    for(int i = 0 ; i < n ; i++)
    {
        cout<<A[i]<<" ";
    }
    cout<<endl;
}
