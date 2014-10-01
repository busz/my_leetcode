/*
Leetcode : Plus_One.cpp
Given a non-negative number represented as an array of digits,

plus one to the number.

The digits are stored such that the most significant digit is

at the head of the list.
*/
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    vector<int> plusOne(vector<int> &digits) {
        int carry = 0;
        vector<int> result(digits.size()+1 , 0);
        int len = digits.size()-1;
        digits[len] += 1;

        for(int i = digits.size()-1 ; i>= 0 ; i--)
        {
            int tmp = digits[i] + carry;
            carry = tmp/10;

            if(carry)
                result[len-i] = tmp%10;
            else
                result[len-i] = tmp;

        }

        if(carry)
            result[len+1] = 1;
        else
            result.pop_back();
        reverse(result.begin() , result.end());
        return result;
    }
};

int main()
{
    Solution test = Solution();
    vector<int> n(1,9);
    vector<int> r = test.plusOne(n);
    for(int i = 0 ; i < r.size() ; i++)
        cout<<r[i];
}
