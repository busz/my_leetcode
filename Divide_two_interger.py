'''
Created on 2014-3-20

Leetcoder  :  divied two integer


Problem : 

Divide two integers without using multiplication, division and mod operator.

@author: xqk
'''
class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        if divisor == 0 : 
            return None
        if dividend == 0:
            return 0;
        sign = 0
        if dividend < 0:
            sign = sign - 1
            dividend = 0 - dividend
        else :
            sign = sign + 1
        if divisor < 0 :
            sign = sign - 1
            divisor = 0 - divisor 
        else:
            sign = sign + 1
        if sign == 0:
            sign = -1
        else:
            sign = 1
            
        divi = dividend
        q = 0
        A = [divisor]
        qA = [1]
        temp = divisor;
        while temp < dividend:
            A.append( A[len(A) - 1] + A[len(A) - 1] );
            qA.append( qA[len(qA) - 1] + qA[len(qA) - 1] );
            temp = A[len(A) - 1]
        if A[len(A) - 1] > dividend:
            A = A[:len(A) - 1]
            qA = qA[:len(qA) - 1]
        
       
        pos = len(A) - 1
        for i in range(len(A) ):
            if divi - A[pos - i] >= 0:
                divi = divi - A[pos - i]
                q = q + qA[pos - i]
            
            
            
            
        if sign == -1:
            q = 0 - q
        
        return q

test = Solution()
print test.divide(2147483647, 3)      
            