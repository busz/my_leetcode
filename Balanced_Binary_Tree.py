'''
Created on 2014.7.25

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined 
as a binary tree in which the depth of the two subtrees of 
every node never differ by more than 1.


'''

# Definition for a  binary tree node

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root ==None:
            return True
        return self.detectBalance(root)[0]
    def detectBalance(self , root):
        if root.left == None and root.right == None:
            return True , 1
        leftDepth , rightDepth = 0 , 0
        leftFlag , rightFlag = True , True
        if root.left != None:
            leftFlag , leftDepth = self.detectBalance(root.left)
        if root.right != None:
            rightFlag , rightDepth = self.detectBalance(root.right)
        if leftFlag and rightFlag and abs(leftDepth - rightDepth) <= 1:
            return True , max(leftDepth , rightDepth) + 1
        else:
            return False , 0
