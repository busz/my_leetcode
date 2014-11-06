'''
Created on 2014.7.25

Leetcode : Binary Tree Level Order Traversal 

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

'''

# Definition for a  binary tree node

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        r = []
        if root == None:
            return r;
        queue = [root];
        level = [1]
        current = [];
        while len(queue) != 0:
            node =  queue[0];
            clevel = level[0];
            
            if node.left != None:
                queue.append(node.left);
                level.append(clevel+1);
            if node.right != None :
                queue.append(node.right);
                level.append(clevel+1);
            
            current.append(node.val);
            if len(level) == 1 or level[0] != level[1]:
                r.append(current[:]);
                current = []
            queue = queue[1:]
            level = level[1:]
        r.reverse()
        return r
test = Solution();
root = TreeNode(3)
node21 = TreeNode(9)
node22 = TreeNode(20)
node31 = TreeNode(15)
node32 = TreeNode(7)
node22.left = node31
node22.right = node32
root.left = node21
root.right = node22
print test.levelOrder(root)
                
            
                

