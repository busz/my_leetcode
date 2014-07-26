"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
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
        
        #Binary Tree Level Order Traversal II
        #r.reverse()
        
        #Binary Tree Zigzag Level Order Traversal 
        
        for i in range(len(r)):
            if i%2 != 0:
                r[i].reverse();
        
        
        return r
