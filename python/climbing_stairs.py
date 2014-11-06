'''
Created on 2014-2-26

Leetcode : Climbing stairs

Problem : 

You are climbing a stair case . It takes n steps to 
reach to the top .

Each time you can either climb 1 or 2 steps. in how many
distinct ways you can climb to the top

Solve : DP

@author: xqk
'''

class Solution:
    # @param n , an integer
    # @return an integer
    def climbStairs(self , n):
        arr = [ 0 for i in range(n)]
        arr[0] = 1
        arr[1] = 2
        for i in range(n-2):
            arr[2+i] = arr[1+i] + arr[i]
        return arr[-1]
            
        
n = 100
test = Solution()
print test.climbStairs(n)
