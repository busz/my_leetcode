'''
Created on 2014-8-4

Leetcode : Letter_Combinations_of_a_Phone_Number

Given a digit string, return all possible letter combinations that the number 

could represent.

A mapping of digit to letters (just like on the telephone buttons) is given 

below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in 

any order you want.


'''

class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        
        r= ['']
        if len(digits) == 0:
            return r
        return self.letterCombin(digits)
        
    def letterCombin(self , digits):
        dic = { '2':['a' , 'b' , 'c'] , '3':['d' , 'e' , 'f'] , \
               '4':['g' , 'h' , 'i'] , '5':['j' , 'k' , 'l'] , \
               '6':['m' , 'n' , 'o'] , '7':['p' , 'q' , 'r' , 's'] , \
               '8':['t' , 'u' , 'v'] , '9':['w' , 'x' , 'y' , 'z']}
        r = []
        if len(digits) == 1:
            r = dic[digits]
        else:
            prefixArr = dic[digits[0]]
            for prefix in prefixArr:
                postfixArr = self.letterCombin(digits[1:])
                for postfix in postfixArr:
                    r.append( prefix + postfix )
        return r
    
test = Solution()
digits = '23'
print test.letterCombinations(digits)
