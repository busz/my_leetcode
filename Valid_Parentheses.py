'''
Created on 2014.7.31

Given a string containing just the characters '(', ')', '{', '}', 
'[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" 
are all valid but "(]" and "([)]" are not.
'''

class Solution:
    # @return a boolean
    def isValid(self, s):
        if s == None or len(s) == 0:
            return False
        if len(s)%2 == 1:
            return False
        stack = [s[0]]
       
        left = ['(','[','{']
        dic = {']':'[' , ')':'(','}':'{'}
        
        for i in range(1,len(s)):
            if s[i] in left:
                stack.append(s[i])
            elif len(stack) == 0 or stack[-1] != dic[s[i]]:
                return False
            else:
                stack.pop();
        if len(stack) != 0:
            return False
        return True
                
test = Solution();
s = "(]{}"
print test.isValid(s)    
            
