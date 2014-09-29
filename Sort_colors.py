'''
Created on 2014-3-21

Leetcoder : Sort color

Problem : 

Given an array with n objects colored red, white or blue, sort them so that 
objects of the same color are adjacent, with the colors in the order red, white 
and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

click to show follow up.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite 
array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?


@author: xqk
'''


class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        n = len(A)
        zero = 0
        two = n - 1
        pos = 0
        while pos <= two:
            if A[pos] == 0:
                A[pos] , A[zero] = A[zero] , A[pos]
                pos += 1
                zero += 1
            elif A[pos] == 2:
                while two> pos and A[two] == 2:
                    two -= 1
                A[pos] , A[two] = A[two] , A[pos]
                two -= 1 
            else:
                pos += 1    
        
        print A
A = [ 0 , 1, 2, 1, 0 ,2]
A = [2,2]
test =  Solution();
test.sortColors(A)
            
        
