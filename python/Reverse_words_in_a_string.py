'''
Created on 2014-3-20


Leetcoder : Reverse words in a string


Problem :

Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

@author: xqk
'''
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        
        start = 0
        str = []
        i = 0
        while i < len(s):
            if s[i] == ' ':
                add = s[start : i]
                if len(add) != 0:
                    str.append(add)
                start = i+1
                
            if i == len(s) - 1:
                add = s[start : i+1]
                if len(add) != 0:
                    str.append(add)
            i = i + 1
        
        news = ""
        num = len(str) - 1;
        for i in range(len(str) ):
            
            news = news + str[num - i]
           
            if i != len(str) - 1:
                news += " ";
        return news;
        
        
        
        
        
        
        
        #=======================================================================
        # str = s.split();
        # news = ""
        # num = len(str) - 1;
        # for i in range(len(str) ):
        #     news = news + str[num - i]
        #     if i != len(str) - 1:
        #         news += " ";
        # return news;
        #=======================================================================
    
s= " 1"
test = Solution()
print "a"+test.reverseWords(s)+'a'