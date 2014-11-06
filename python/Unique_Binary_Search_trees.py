'''
Created on 2014-3-19


Leetcoder : Unique Binary Search trees

Problem : 
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


@author: xqk
'''

class Solution:
    # @return an integer
    def numTrees(self, n):
        if n == 0:
            return 0
        
        A = [1 , 1]
        for i in range(n):
            newV = 0
            j = 0;
            while j < i+2:
                left = j
                right = i+2 -1 - j
                newV = newV + A[left]*A[right]
                j = j+1
              
            A.append(newV)
        
        j = 0;
        num = 0;
        while j < n :
            left = j
            right = n -1 - j
            num = num + A[left]*A[right] 
            j = j + 1
           
            
        return num
    
test = Solution();
print test.numTrees(12)