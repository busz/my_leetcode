/*
Leetcode : ZigZag_Conversion.cpp

The string "PAYPALISHIRING" is written in a zigzag pattern

on a given number of rows like this: (you may want to display

this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion

given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

*/

#include <iostream>
#include <string>

using namespace std;
class Solution {
public:
    string convert(string s, int nRows) {
        if (nRows == 1)
            return s;
        int n = nRows*2 - 2;
        string result = "";
        int len = s.size();
        for(int i = 0 ; i < nRows ; i++)
        {
            int pos = i;
            while( pos < len)
            {
                result.push_back(s[pos]);

                if(i !=0 && i!= nRows - 1 && pos + (nRows - 1 - pos%n)*2<len )
                {
                    result.push_back(s[pos + (nRows - 1 - pos%n)*2]);
                }
                pos += n;
            }
        }
        return result;
    }
};

int main()
{
    Solution test = Solution();
    string s = "PAYPALISHIRING";
    int nRows = 1;
    cout<<test.convert( s , nRows)<<endl;
}
