/*
Leetcode : Longest_Common_Prefix.cpp

Write a function to find the longest common prefix string amongst an array of strings.
*/
#include <iostream>
#include <string>
#include <vector>
using namespace std;
class Solution {
public:
    string longestCommonPrefix(vector<string> &strs) {
        if (!strs.size() )
            return "";
        int pos = 0;
        bool flag = true;
        while(true)
        {
            char c;
            if(pos < strs[0].size())
                c = strs[0][pos];
            else
                break;
                
            for(int i = 1 ; i < strs.size() ; i++)
            {
                if(pos >= strs[i].size() || strs[i][pos] != c)
                {
                    flag = false;
                    break;
                }
            }
            if (!flag)
                break;
            else
                pos++;
        }
        return strs[0].substr(0,pos);
    }
};

int main()
{
    Solution test = Solution();
    
}
