'''
Created on 2014-2-21

leetcode :  Symmetric Tree

Problem:

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

Solve:



@author: xqk
'''

#Definition for a  binary tree node

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root == None:
            return True
        else:
            
            return self.isReverse(root.left, root.right)
        
   
        
    def isReverse(self , r1 , r2):
        if r1 == None and r2 == None:
            
            return True
        elif r1.val == r2.val and not (bool(r1.left) | bool(r2.right) or bool(r1.right) | bool(r2.left) ):
            
            return True
        elif bool(r1.left) ^ bool(r2.right) or bool(r1.right) ^ bool(r2.left):
           
            return False
        elif r1.right != None and r1.right.val != r2.left.val:
            
            return False
        elif r1.left != None and r2.right.val != r1.left.val:
            
            return False
        else :
            return r1.val == r2.val and self.isReverse(r1.left, r2.right) and self.isReverse(r1.right, r2.left)
        
        
        
          
                
root = TreeNode(1)


left = TreeNode(2)


right = TreeNode(2)


root.left = left
root.right = right

test = Solution()

print test.isSymmetric(root)

            