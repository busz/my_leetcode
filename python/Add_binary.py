'''
Created on 2014-3-23

Leetcoder : Add binary

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

@author: xqk
'''

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a;
        if len(a) < len(b):
            temp = a
            a = b
            b = temp
        r = [];
        f = 0
        ap = len(a) -1
        bp = len(b) - 1
        while bp>=0:
            sumV = int(b[bp])+int(a[ap])+f
            f = sumV/2
            
            r.append(str(sumV%2) );
            bp = bp - 1
            ap = ap -1 
        while ap >= 0:
            
            sumV = int(a[ap])+f
            f = sumV/2
           
            r.append(str(sumV%2) );
            ap = ap -1
        s = ''
        for i in range(len(r)):
            s= s + r[len(r) -1 -i]
        
        if f == 1:
            s = '1'+s
        return s
        
        
        
        
a = '100'
b='110010'
test = Solution()
print test.addBinary(a, b)
