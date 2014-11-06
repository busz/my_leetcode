'''
Created on 2014-2-21


leetcode : Populating next right Pointers in each node

Problem:

Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next 
right node. If there is no next right node, the 
next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary 
tree (ie, all leaves are at the same level, 
and every parent has two children).

Solve:

queue and a number flag

@author: xqk
'''

# Definition for a  binary tree node

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root == None:
            return root
        q = [root]
        num = 1
        pos = 1
        while len(q) != 0 :
            croot = q[0]
            if croot.left != None:
                q.append(croot.left)
            if croot.right != None:
                q.append(croot.right)
            if pos != 1 : 
                q[0].next = q[1]
                pos = pos - 1
            else:
                q[0].next = None
                num = num * 2
                pos = num   
            q = q[1:]
        return root
    
root = TreeNode(1)
left = TreeNode(2)
right = TreeNode(3)
root.left = left
root.right = right

test = Solution()
root = test.connect(root)
print root.next
print root.left.next.val
print root.right.next

 