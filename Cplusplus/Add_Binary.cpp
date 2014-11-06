/*
Leetcode : Add_Binary.cpp

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
*/
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    string addBinary(string a, string b) {
            int carry = 0;
            string result = "";
            if(a.size() < b.size() )
            {
                string tmp = b;
                b = a;
                a = tmp;
            }
            int lB = b.size();
            int lA = a.size();
            int pos = 0;
            while(pos < lB && pos < lA)
            {
                int value = carry + int(b[lB - 1-pos]) - 48 + int(a[lA - 1 -pos]) - 48;
                pos++;
                switch (value)
                {
                    case 0:
                        result.append("0");
                        break;
                    case 1:
                        result.append("1");
                        carry = 0;
                        break;
                    case 2:
                        carry = 1;
                        result.append("0");
                        break;
                    case 3:
                        carry = 1;
                        result.append("1");
                        break;

                }
            }
            for(int i = pos ; i < lA ; i++)
            {
                if(carry)
                {
                    if(a[lA - 1- pos] == '1')
                    {
                        result.append("0");
                    }
                    else
                    {
                        result.append("1");
                        carry = 0;
                    }
                }
                else
                    result.push_back(a[lA - 1- i]);
            }
            if(carry)
                result.append("1");
            reverse(result.begin() , result.end());
            return result;
    }
};

int main()
{
    Solution test = Solution();
    string a = "11";
    string b = "1";
    cout<<test.addBinary(a,b)<<endl;
}
