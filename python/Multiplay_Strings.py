'''
Created on 2014-3-24


Leetcoder : Multiplay strings 

Problem : 

Given two numbers represented as strings , return multiplication of the numbers 
as a string .

Note : The numbers can be arbitrarity large and non-negative 
@author: xqk
'''

class Solution:
    #@param num1 , a string
    #@param num2 , a string
    #@return a string
    def multilpply(self , num1, num2):
        if num1 =='0' or num2 =='0':
            return '0'
        flag = ''
        if num1[0] == '-' :
            flag = '-'
            num1 = num1[1:]
        if num2[0] == '-':
            if flag == '':
                flag ='-'
            else:
                flag = ''
            num2 = num2 [1:]
       
        
        num = int(num2)
        
        
        z = int(num1)
            
       
        r = int(z)*num
        
        
       
        return flag+str(r)
            
test = Solution()
   
print test.multilpply('123456789',  '987654321' )     
            
            