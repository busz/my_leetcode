'''
Created on 2014-2-19

leetcode reverse integer

Problem :

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

Solve :

str() and int() and cut 


@author: xqk
'''

class Solution:
    # @return an integer
    
    #===========================================================================
    # def reverse(self, x):
    #     x = str(x);
    #     if x[0] == '-':
    #         x = x[1:]
    #         x = x[::-1]
    #         x = '-'+x
    #     else:
    #         x = x[::-1]
    #     return int(x)
    #===========================================================================
    
    
    #or
    
    def reverse(self , x):
        r = 0;
        if x == 0 :
            return 0 
        f = x/abs(x);
        x = x*f
        while(x):
            r = r*10 + x%10
            x = x/10
            
        return r*f
        
        
         
    
a = -123
a = 0



test = Solution()
print test.reverse(a)