'''
Created on 2014-8-14

Leetcode : Evaluate_Reverse_Polish_Notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
  
'''

class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        #'/' is different between python and C/C++
        dict = { '+':lambda x,y : x+y , '-' : lambda x,y : x - y , '*' : lambda x,y:x*y , \
                 '/':lambda x , y: x/y+1 if x%y != 0 and x*y<0 else x/y }
        numStack = []
       
        for item in tokens:
            if dict.has_key(item):
                y = numStack.pop()
                x = numStack.pop()
               
                numStack.append(dict[item](x,y));
                
            else:
                numStack.append( int(item) )
        return numStack[-1]
    
   
        
test = Solution()
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
#tokens = ["4","-2","/","2","-3","-","-"]
print test.evalRPN(tokens)
                
        
