/*
Leetcode : Roman_to_Integer.cpp

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
*/

#include <iostream>
#include <string>
#include <map>
using namespace std;

class Solution {
public:
    int romanToInt(string s) {

        map<char , int> table;
        table['I'] = 1;
        table['V'] = 5;
        table['X'] = 10;
        table['L'] = 50;
        table['C'] = 100;
        table['D'] = 500;
        table['M'] = 1000;
        int result = 0;
        int pos = s.size() - 1;
        int pre = 0;
        while(pos>=0)
        {
            int num = table.find(s[pos])->second;
            if(num >= pre)
            {
                result += num;
                pre = num;
            }
            else
            {
                result -= num;
            }
            pos--;
        }
        return result;
    }
};

int main()
{
    Solution test = Solution();
    string s = "DCXXI";
    cout<<test.romanToInt(s)<<endl;
}
