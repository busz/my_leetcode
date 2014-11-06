/*
Leetcode : Pow_x_n.cpp
*/
#include <iostream>
#include <cmath>
using namespace std;

class Solution {
public:
    double pow(double x, int n) {
        if(n==0)
            return 1;
        bool postive = true;
        if(n < 0)
        {
            postive = false;
            n = -n;
        }
        bool flag = false;
        if(n%2 == 1 && x/abs(x) == -1)
            flag = true;

        double pre = x;
        int num = 1;
        while(num*2 < n && num*2 >=0 )
        {
            num *= 2;
            pre = pre*pre;
        }
        double result = 1;
        while(n>0)
        {
            result *= pre;
            n = n - num;
            while(num > n)
            {
                num = num/2;
                pre = sqrt(pre);
            }
            //cout<<num<<" "<<n<<endl;
        }
        if(!postive)
            result = 1/result;
        if(flag)
            result *= -1;
        return result;

    }
};
int main()
{
    Solution test = Solution();
    cout<<test.pow(-1,3)<<endl;
}
