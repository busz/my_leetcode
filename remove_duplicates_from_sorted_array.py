'''
Created on 2014-2-26

leetcode : Remove Ducplicates from sorted array

Problem : 

Given a sorted array , remove the duplicates in place such 
that each element appear only once and return the new lenght

Do not allocate extra space for another array.
You must do thos in place with constant memory

for example :
Given input array A = [1,1,2]
Your function should return length = 2 . and A is now [1,2]

@author: xqk
'''

class Solution:
    # @param a list of tintegers
    # @return an integer
    def removeDuplicates(self , A):
        if len(A) <2:
            return len(A)
        num = 0
        key = A[0]
        for i in range(len(A) ):
            if key != A[i]:
                A[num] = key
                num = num + 1
                key = A[i]
        A[num] = key
        return num+1
A = [1,1,2]
test = Solution()
print test.removeDuplicates(A)
       
