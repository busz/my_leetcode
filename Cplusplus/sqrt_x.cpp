/*
Leetcode : sqrt_x.cpp
Implement int sqrt(int x).

Compute and return the square root of x.
*/
#include <iostream>
#include <climits>
using namespace std;

class Solution {
public:
    int sqrt(int x) {
        unsigned long long left = 1;
        unsigned long long right = x/2;
        while(left <= right)
        {
            unsigned long long mid = (left+right)/2;
            unsigned long long square = mid*mid;
            if(square == x)
                return mid;
            else if(square > x )
            {
                right = mid - 1;
            }
            else
                left = mid + 1;
            //cout<<mid<<endl;
        }
        return left;
    }
};
int main()
{
    int x = 1579205274;
    Solution test = Solution();
    cout<<test.sqrt(x)<<" "<<INT_MAX<<endl;
}
