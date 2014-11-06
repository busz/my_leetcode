/*
Leetcode : Count_and_Say.cpp

The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

*/

#include <iostream>
#include <string>
#include <sstream>

using namespace std;

class Solution {
public:
    string countAndSay(int n) {

        string s = "1";

        for(int i = 0 ; i < n - 1  ; i++)
        {
            string nS = "";
            int num = 1;
            char pre = s[0];
            for(int i = 1 ; i < s.size() ; i++)
            {
                if(pre == s[i])
                {
                    num++;
                }
                else
                {
                    ostringstream s1;
                    s1 <<num;
                    string s2 = s1.str();
                    nS += s2;
                    nS += pre;
                    pre = s[i];
                    num = 1;
                }
            }
            ostringstream s1;
            s1 <<num;
            string s2 = s1.str();
            nS += s2;
            nS+=pre;
            s = nS;

        }

        return s;

    }
};

int main()
{
    Solution test = Solution();
    int n = 10;
    for(int i = 1 ;i<n ; i++)
    cout<<test.countAndSay(i)<<endl;
}
