/*
Leetcode : Integer_to_Roman.cpp

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
*/

#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string intToRoman(int num) {
        int arr[] = {1000,900,500,400,100,90,50,40,10,9,5,4,1};
        string strArr[] = {"M","CM" , "D" , "CD" , "C" , "XC" ,
        "L" , "XL" , "X" , "IX" , "V" , "IV" , "I"} ;
        string result = "";
        for(int i = 0 ; i < 13 ; i++)
        {
            while(num - arr[i]>=0)
            {
                result.append(strArr[i]);
                num = num - arr[i];
            }
        }
        return result;
    }
};

int main()
{
    Solution test = Solution();
    int num = 1491;
    cout<<test.intToRoman(num)<<endl;
}
