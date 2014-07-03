'''
Created on 2014-2-21

leetcode : Maximum Depth of Binary Tree

Problem:

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along 
the longest path from the root node down to the 
farthest leaf node.


Solve :




@author: xqk
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
    def maxDepth(self, root):
        #=======================================================================
        #my method 
        #root.val = 1
        # q = [root]
        # lastNode = None
        # while len(q) != 0 :
        #     fNode = q[0]
        #     if fNode.left != None:
        #         fNode.left.val = fNode.val + 1;
        #         q.append(fNode.left)
        #     if fNode.right != None:
        #         fNode.right.val = fNode.val + 1
        #         q.append(fNode.right)
        #     lastNode = q[len(q)-1]
        #     q = q[1:]
        # return lastNode.val
        #=======================================================================
    
        if root == None :
            return 0;
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        
        return  l + 1 if l > r else r + 1
         

    
root = TreeNode(2)
left = TreeNode(2)
leftRight = TreeNode(1)

left.right = leftRight
root.left = left



test = Solution()
print test.maxDepth(root)