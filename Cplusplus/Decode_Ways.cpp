/*
Decode_Ways.cpp

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

*/
#include <vector>
#include <string>
#include <iostream>

using namespace std;
class Solution {
public:
    int numDecodings(string s) {
        if(!s.size())
            return 0;
        vector<int> num(s.size() , 0);
        if(s[0] != '0')
            num[0] = 1;
        else
            return 0;
        if(s[1] > '0')
            num[1] += 1;
        if((s[0] == '1') || (s[0] == '2' && s[1] < '7'))
            num[1] += 1;
        for(int i = 2; i < s.size() ; i++)
        {
            if(s[i] != '0')
                num[i] += num[i-1];
            if( (s[i-1] == '1') || (s[i-1] == '2' && s[i] < '7') )
                num[i] += num[i-2];
            else if(s[i] == '0')
                return 0;
        }
        
        return num[num.size() - 1];
    }
};

int main()
{
    Solution test = Solution();
    cout<<test.numDecodings("111")<<endl;
}
