'''
Created on 2014-8-8


Leetcode : Validate_Binary_Search_Tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

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
    def isValidBST(self, root):
        if root == None:
            return True
        flag = self.checkBST(root)[2]
        return flag
        
    def checkBST(self , root):
        minV = 0
        maxV = 0
        flag = True
        if root.left == None:
            minV = root.val
        else:
            nextMin , nextMax , nextFlag = self.checkBST(root.left)
            if nextFlag:
                if root.val <= nextMax:
                    flag = False
                else:
                    minV = nextMin
            else:
                flag = nextFlag
        if root.right == None:
            maxV = root.val
        else:
            nextMin , nextMax , nextFlag = self.checkBST(root.right)
            if nextFlag:
                if root.val >= nextMin:
                    flag = False
                else:
                    maxV = nextMax
            else:
                flag = nextFlag
        return minV , maxV , flag
