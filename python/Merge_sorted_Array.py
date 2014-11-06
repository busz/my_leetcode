'''
Created on 2014-3-19


leetcoder :  merge sorted array

Problem : Given two sorted integer arrays A and B, merge B into A as one sorted
 array.

Note:
You may assume that A has enough space (size that is greater or equal to m + n) 
to hold additional elements from B. The number of elements initialized in A and 
B are m and n respectively.



@author: xqk
'''

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        if A == []:
            return B
        if B == []:
            return A
        num = m + n -1;
        ap = m - 1
        bp = n -1
        while num>= 0 and ap >= 0 and bp >= 0 :
            if A[ap] < B[bp]:
                A[num] = B[bp]
                bp -= 1
            else:
                A[num] = A[ap]
                ap -= 1
            num -=1
        if bp >= 0:
            for i in range(bp+1):
                A[i] = B[i]
                
            
        return A
        
    
A = [4 , 0]
B = [1]
test = Solution()
C = test.merge(A, len(A) - len(B), B, len(B))
print C
                