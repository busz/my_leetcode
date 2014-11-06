/*
Leetcode : Gray_Code.cpp

The gray code is a binary numeral system where

two successive values differ in only one bit.

Given a non-negative integer n representing the

total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its

gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquel

y defined.

For example, [0,2,3,1] is also a valid gray code

sequence according to the above definition.

For now, the judge is able to judge based on one

instance of gray code sequence. Sorry about that.
*/
#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> result(1<<n , 0);
        if(n == 0)
        {
            return result;
        }
        else
        {
             int p = 0;
             while(p < n)
             {
                int base = 1<<p;
                int num = (1<<(p+1)) - 1;
                for(int i = 0 ; i < base ; i++)
                {
                    result[num-i] = base + result[i];
                }
                p++;
             }


        }
        return result;
    }
};

int main()
{
    Solution test = Solution();
    vector<int> result = test.grayCode(2);
    for(int i = 0 ; i < result.size() ; i++)
    {
        cout<<result[i]<<endl;
    }
}
