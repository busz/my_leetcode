'''
Created on 2014-3-25

Leetcoder  : 3sum

Problem : 

Given an array S of n integers, are there elements a, b, c in S such that a + b 
+ c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)


@author: xqk
'''

import time


class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        
        r = []
        if num == None or len(num)  < 3:
            return r
         
        num = sorted(num)
         
        for i in range(len(num) - 2 ):
            first = num[i]
            left = i + 1
            right = len(num) - 1
            while left < right:
                v = num[left] + num[right]
                if first + v == 0:
                    newr = [first  , num[left] , num[right] ] 
                    if newr not in r:
                        r.append( newr )
                    left = left + 1
                    right = right - 1
                elif first + v > 0:
                    right = right - 1
                else:
                    left = left + 1
        
               
         
         
        return r
     
     
    
      
start = time.clock()
test = Solution();
num = [7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6]
num = [0,0,0]
#num = [1,-1,-1,0]
#num = [0,0,0,0]
print test.threeSum(num)
end = time.clock()
print end - start      
