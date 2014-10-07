/*
Leetcode : Length_of_Last_Word.cpp
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.
*/

class Solution {
public:
    int lengthOfLastWord(const char *s) {
        int length = strlen(s);
        int wordL = 0;
        while(length > 0 && s[length-1] == ' ')
            length--;
        if(length == 0)
            return 0;
        while(length > 0 && s[length-1] != ' ')
        {
            length--;
            wordL++;
        }
        return wordL;
    }
};
