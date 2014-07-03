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
        num = len(A)
        p0 = num - 1
        p1 = num - 1
        p2 = num - 1 
        
        while num > 0:
            num = num - 1
            
            if A[num ] == 0:
                self.swap(A , p0 , num )
                p0 = p0 - 1
            elif A[num ] == 1:
                self.swap(A , p1 , num )
                p1 = p1 - 1
                p0 = p0 - 1
            elif A[num ] == 2 :
                self.swap(A, num , p2)
                p2 = p2 - 1
                p1 = p1 - 1
                p0 = p0 - 1
            print A
        return A
                
    def swap(self , A , i , j):
        temp = A[i]
        A[i] = A[j]
        A[j] = temp
        return A        
    
A = [ 0 , 1, 2, 1, 0 ,2]
test =  Solution();
print test.sortColors(A)
            
        