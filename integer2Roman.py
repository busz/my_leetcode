'''
Created on 2014-2-20

leetcode : Integer to roman 

Problem:
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

solve:
directory


@author: xqk
'''


class Solution:
    # @return a string
    def intToRoman(self, num):
        
        dir = ['I' , 'IV' ,'V' , 'IX' , 'X' , 'XL' ,'L' ,'XC' , 'C' , 'CD' , 'D' , 'CM' , 'M']
        n = [1,4,5,9,10,40,50,90,100,400 , 500,900,1000]
        s = ''
        
        pos = len(n) - 1
        for i in range(len(n)):
            while(num>=n[pos-i]):
                s = s + dir[pos-i]
                num = num - n[pos-i]
                     
        return s
    
    
num = 3333
test = Solution()
print test.intToRoman(num)