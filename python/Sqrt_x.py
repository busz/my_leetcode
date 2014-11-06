'''
Created on 2014.8.16

Leetcode : Decode_Ways

Implement int sqrt(int x).

Compute and return the square root of x.

'''

class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x == 0:
            return 0
        cur = 1;  
        while 1: 
          
            pre = cur;  
            cur = x / (2 * pre) + pre / 2.0;  
            if abs(cur - pre) < 0.00001:
                break
        return int(cur);  
    
test = Solution()
x = 9
print test.sqrt(x)
