'''
Created on 2014-8-4

Leetcode : Construct_Binary_Tree_from_Preorder_and_Inorder_Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

'''

# Definition for a  binary tree node

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        
        return self.buildtree(preorder, inorder)[0]
        
        
    def buildtree(self, preorder, inorder):
        if inorder == None or len(inorder) == 0:
            return None , preorder
        root = TreeNode(preorder[0])
        
        mid = inorder.index(preorder[0])
        
        preorder = preorder[1:]
        
        root.left , preorder = self.buildtree(preorder, inorder[:mid])
        
        root.right , preorder = self.buildtree(preorder, inorder[mid+1:])
        return root , preorder
