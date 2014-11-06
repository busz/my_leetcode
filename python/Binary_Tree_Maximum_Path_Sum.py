'''
Created on 2014.8.17

Leetcode : Binary Tree Maximum Path Sum

Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.

'''

# Definition for a  binary tree node

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        maxV = -1000
        return self.computMaxPath(root, maxV)
        
        
    def computMaxPath(self , root , maxV):
        if root.left == None and root.right == None:
            if maxV < root.val:
                maxV = root.val
        elif root.left != None and root.right != None:
            leftMax = self.computMaxPath(root.left, maxV)
            rightMax = self.computMaxPath(root.right, maxV)
            maxV = max(maxV , root.val , leftMax , rightMax , root.left.val + root.val , \
                       root.right.val + root.val , root.left.val + root.val + root.right.val)
            root.val = max(root.val , root.left.val + root.val , root.right.val + root.val)
            
            
        elif root.left != None:
            levelMax = self.computMaxPath(root.left, maxV)
            maxV = max(maxV , root.val , levelMax , root.val + root.left.val)
            root.val = max(root.left.val + root.val , root.val)
            
            
        else:
            levelMax = self.computMaxPath(root.right, maxV)
            maxV = max(maxV , root.val , levelMax , root.val + root.right.val)
            root.val = max(root.right.val + root.val   , root.val)
            
            
        return maxV
            
test = Solution()
node = TreeNode(1)
node.left = TreeNode(-2)
node.right = TreeNode(3)
print test.maxPathSum(node)    
