'''
Created on 2014.8.15

Leetcode : Longest_Valid_Parentheses

Given a string containing just the characters '(' and ')', find the length of the 

longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

'''

class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        stack = []
        nStack = []
        arr = [0 for i in range(len(s))]
        
        for  index , item in enumerate(s):
            
            if item == '(':
                stack.append('(')
                nStack.append(index)
            else:
                if stack and stack[-1] == '(':
                    arr[index] = 1
                    arr[nStack[-1]] = 1
                    stack.pop()
                    nStack.pop()
                    
                else:
                    stack.append(')')
                    nStack.append(index)
        maxL = 0
        num = 0
        for item in arr:
            if item == 0:
                if num > maxL:
                    maxL = num
                num = 0
            else:
                num += 1
        maxL = num if num > maxL else maxL
         
        return maxL

test = Solution()
s = '()(()()'
print test.longestValidParentheses(s)
                
