'''
Created on 2014.9.24.
Leetcode : Maximum_Product_Subarray.py

Find the contiguous subarray within an array 

(containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
@author: xqk
'''


class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        maxV = A[0]
        postive = [1 for i in range(len(A))]
        nagetive = [1 for i in range(len(A))]
        
        postive[0] = A[0]
        
        nagetive[0] = A[0]
        for i in range(1,len(A)):
            preMin = nagetive[i-1]*A[i]
            preMax = postive[i-1]*A[i]
            postive[i] = max(A[i] , preMin , preMax);
            nagetive[i] = min(A[i] , preMin , preMax);
            if postive[i] > maxV:
                maxV = postive[i]
            
           
        return maxV
test = Solution()
A = [1,-3,2,0,-1,0,-2,-3,1,2,-3,2]
print test.maxProduct(A)
                 
            
