'''
Created on 2014-2-21

leetcode : Plus One

Problem : 

Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

Solve : 

@author: xqk
'''


class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        l = len(digits)
        flag = 1
        for i in range(len(digits) ):
            pos = l - 1 - i ;
            if digits[pos] + flag == 10:
                digits[pos] = 0
                if pos == 0 :
                    digits = [1] + digits
            else:
                digits[pos] = digits[pos] + 1
                flag = 0
                break;
        return digits  
digits = [9,9]
test = Solution()
print test.plusOne(digits)
