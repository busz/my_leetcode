'''
Created on 2014-2-20
leeetcode : Roman to Integer

Problem:
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

Solve :

string 


@author: xqk
'''

class Solution:
    # @return an integer
    def romanToInt(self, s):
        dir = { 'I':1, 'V':5 , 'X':10 , 'L':50 , 'C':100 , 'D':500 , 'M':1000}
        num = 0
        for i in range(len(s) - 1 ):
            if dir[s[i]] < dir[s[i+1]]:
                num  = num - dir[s[i]]
            else:
                num = num + dir[s[i]]
        num = num + dir[s[len(s) - 1]]
        return num

s = 'MMMCCCXXXIII'
test = Solution()
print test.romanToInt(s)
