/*
Leetcode : Longest_Substring_Without_Repeating_Characters.cpp

Given a string, find the length of the longest substring without

repeating characters. For example, the longest substring without

repeating letters for "abcabcbb" is "abc", which the length is 3.

For "bbbbb" the longest substring is "b", with the length of 1.
*/

#include <iostream>
#include <string>
#include <map>
using namespace std;



class Solution {
public:
    int lengthOfLongestSubstring(string s) {
            int maxL = 0;
            map<char , int> table;
            int pre = 0;
            map<char , int>::iterator iter;
            for(int i = 0 ; i < s.size() ; i++)
            {
                iter = table.find(s[i]);
                if(iter == table.end())
                {
                    table[s[i]] = i;
                }
                else
                {
                    if(table[s[i]] < pre)
                    {
                        table[s[i]] = i;
                    }
                    else
                    {
                        int len = i - pre;
                        maxL = maxL > len ? maxL:len;
                        pre = table[s[i]] + 1;
                        table[s[i]] = i;
                    }

                }
            }
            maxL = maxL > (s.size() - pre) ? maxL : (s.size() - pre);
            return maxL;
    }
};

int main()
{
    Solution test = Solution();
    string s = "qopubjguxhxdipfzwswybgfylqvjzhar";
    cout<<test.lengthOfLongestSubstring(s)<<endl;


    return 0;
}
