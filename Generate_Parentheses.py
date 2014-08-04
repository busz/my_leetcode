'''
Created on 2014.8.2

Leetcode : Generate_Parentheses

Given n pairs of parentheses, write a function to generate all combinations 
of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"

'''

class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        if n == 0:
            return []
        if n == 1:
            return ['()']
        r = []
        s = '('
        leftNum = 1 
        rightNum = 0
        return self.generateString(leftNum, rightNum, n, s)
        
        
        
        return r
    def generateString(self , leftNum , rightNum , n , s):
        r = []
        if leftNum == n and rightNum == n -1 :
            s = s + ')'
            r.append(s)
            return r
        else:
            if leftNum > rightNum:
                r = r + self.generateString(leftNum, rightNum+1, n, s+')')
            if leftNum < n:    
                r = r + self.generateString(leftNum+1, rightNum, n, s+'(')
            
        return r
    
test = Solution()
print test.generateParenthesis(4)
            
        
        
        
        
test = Solution()
print test.generateParenthesis(8)
            
            
