'''
Created on 2014-3-25

Leetcoder  : 3sum

Problem : 

Given an array S of n integers, are there elements a, b, c in S such that a + b 
+ c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ¡Ü b ¡Ü c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)


@author: xqk
'''

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        r = []
        if num == None or len(num)  < 3:
            return r
        
        for i in range(len(r)):
            