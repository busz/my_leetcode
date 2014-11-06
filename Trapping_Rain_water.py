'''
Created on 2014-2-26

leetcode : Trapping Rain water

Problem : 

Given n non-negative integers representing an elevation map
where the width of each bar is 1 .  compute how much water 
it is able to trap after raining.

For example,
 given [0,1,0,2,1,0,1,3,2,1,2,1 ],return 6
 
 Solve : 
 

@author: xqk
'''

class Solution:
    # @param A , a list of integers
    # @return an integer
    def trap(self , A):
        if len(A)==0:
            return 0
        leftBar = []
        leftMaxBar = A[0]
        for i in range(1 , len(A)):
            if A[i - 1] > leftMaxBar:
                leftMaxBar = A[i - 1];
            leftBar.append(leftMaxBar)
        rightBar = []
        rightMaxBar = A[len(A) - 1]
        for i in range( 0 , len(A) - 1):
            if A[len(A) - 1 - i] > rightMaxBar:
                rightMaxBar = A[len(A) - 1 - i]
            rightBar.append(rightMaxBar)
        
        rightBar.reverse();
        
      
        sumV = 0
        for i in range(1 , len(A) - 1):
            height = leftBar[i - 1] if leftBar[i-1] < rightBar[i] else rightBar[i]
                    
            height = height - A[i] if A[i] < height else 0
            
            sumV = sumV + height
           
        return sumV
        
        
A = [0,1,0,2,1,0,1,3,2,1,2,1 ]
test = Solution()
print test.trap(A)
