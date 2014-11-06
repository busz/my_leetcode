'''
Created on 2014.8.3

Leetcode : Count_and_Say

The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

'''

class Solution:
    # @return a string
    def countAndSay(self, n):
        r = '1'
        if n == 1:
            return r
        while n - 1 > 0:
            first = r[0]
            num = 1
            newR = ''
            i = 0
            while i < len(r) - 1:
                if r[i+1] == first:
                     num = num + 1
                     i = i + 1
                else:
                    newR = newR + str(num) + first
                    num = 1
                    first = r[i+1]
                    i = i + 1
            newR = newR + str(num) + first
            r = newR
            n = n -1
            
        return r
        
        
test = Solution()
print test.countAndSay(5)
                
