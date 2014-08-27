'''
Created on 2014-8-22

Leetcode : Recover_Binary_Search_Tree

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise 

a constant space solution?

'''

# Definition for a  binary tree node

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        node1 = node2 = None
        pre = None
        pre , node1 , node2 = self.traverse(root , pre , node1 , node2)
        node1.val , node2.val = node2.val , node1.val
        return root

    def traverse(self , root, pre , node1 , node2):
        if root == None:
            return pre , node1 , node2
        self.traverse(root.left, pre, node1, node2)
        if pre and pre.val > root.val:
            node2 = root
            if not node1:
                node1 = pre
        pre = root
        self.traverse(root.right, pre, node1, node2)
        return pre , node1 , node2
        
        
