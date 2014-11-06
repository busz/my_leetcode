'''
Created on 2014-3-20


Leetcoder : pow(x,y)

Problem : 

Implement pow(x, n).

@author: xqk
'''

class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n == 0:
            return 1
        
        if n < 0 :
            return self.pow(1.0/x , -n)
        s = 1.0
      
        while n>0:
            if(n&1>0):
                s *= x;
            x *= x
            n>>=1
        return s
    
x = 0.001
n = 10000

#===============================================================================
# x = 0.00001
# n = 2147483647
#===============================================================================

test = Solution()
print test.pow(x, n)